import random
from itertools import count
from queue import PriorityQueue
from .coordinate import Coordinate
from .dot import Dot
from .node import Node
from .power import Power
from .rect import Rect

## The Arena represents the maze in the game, including the location of all
## the vertices, the edges between them, and the locations of objects (such as,
## dots, powers, and spawn locations).
## This is an abstract base class to be inherited by actual maze shapes
## (such as square or hexagonal).
class Arena:

    ## Create a new Arena.
    #
    # @param logical_width The logical width of the maze in terms of number
    # of vertices.
    # @param logical_height The logical height of the maze in terms of number
    # of vertices.
    # @param width The actual width of the maze in some units.
    # @param height The actual height of the maze in some units.
    # @param shape The shape of the maze.
    def __init__(self, logical_width, logical_height, width, height, shape):
        self._shape = shape
        self._width = width
        self._height = height
        self._logical_width = logical_width
        self._logical_height = logical_height
        self.generate()
    
    ## Get the shape of this maze.
    #
    # @return The shape of this maze.
    @property
    def shape(self):
        return self._shape

    ## Generate a new random maze. This function ultimately calls the abstract
    ## protected `_generate_nodes', overridden by sub-classes, to generate the
    ## the nodes of the maze according to some rules (such as the shape),
    ## but also handles duties like deciding where spawn locations should be,
    ## and creating the dots and powers of the maze.
    def generate(self):
        width = self.logical_width
        height = self.logical_height
        while (True):
            self._nodes = self._generate_nodes(width, height)
            self._avatar_start = self._most_middle()
            self._ghost_return = self._nodes[0]
            self._pinky_start = self._most_top_left()
            self._blinky_start = self._most_top_right()
            self._inky_start = self._most_bottom_right()
            self._clyde_start = self._most_bottom_left()
            if self._generate_maze():
                break
        self._dots = self._generate_dots()
        self._powers = self._generate_powers()
        self._generate_heuristics()
    
    ## Used by the `_generate_heuristics' function, this calculates the shortest
    ## path to this node from every other node.
    #
    # @param target The target node.
    #
    # @return A list of the lengths of the shortest possible path from every
    # node to the target.
    def _generate_heuristic(self, target):
        unique = count()
        cost = {}
        queue = PriorityQueue()
        cost[target] = 0.0
        for neighbour in target.neighbours:
            g = target.distance(neighbour)
            queue.put((g, (next(unique), neighbour, g)))
        while not queue.empty():
            elem = queue.get()
            node = elem[1][1]
            cost_ = elem[1][2]
            if node in cost:
                if cost[node] > cost_:
                    raise
                continue
            cost[node] = cost_
            for neighbour in node.neighbours:
                g = cost_ + node.distance(neighbour)
                queue.put((g, (next(unique), neighbour, g)))
        return cost
    
    ## Some sprites in the game will require the use of an A*-search to find the
    ## best path through the maze. This requires a suitable heuristic in order
    ## to perform at a reasonable speed. This function precalculates the
    ## heuristic by performing Dijkstra's algorithm from every node to every
    ## other node to calculate the length of the shortest possible path between
    ## every pair of nodes.
    def _generate_heuristics(self):
        self._heuristics = {}
        for node in self._nodes:
            self._heuristics[node] = self._generate_heuristic(node)
    
    ## Returns the length of the shortest possible path from the source node
    ## to the target.
    #
    # @param source The source node.
    # @param target The target node.
    #
    # @return The length of the shortest path between them.
    def heuristic(self, source, target):
        if target in self._heuristics[source]:
            return self._heuristics[source][target]
    
    ## Get the node in the graph which is the closest towards the centre;
    ## this is where the Avatar will spawn.
    #
    # @return The most middle node.
    def _most_middle(self):
        return self._most_target(self._width/2, self._height/2)

    ## Get the node in the graph that is the most top-left; this is where
    ## "Pinky" will spawn.
    #
    # @return The most top-left node.
    def _most_top_left(self):
        return self._most_target(0, 0)

    ## Get the node in the graph that is the most top-right; this is where
    ## "Blinky" will spawn.
    #
    # @return The most top-right node.
    def _most_top_right(self):
        return self._most_target(self._width, 0)

    ## Get the node in the graph that is the most bottom-left; this is where
    ## "Clyde" will spawn.
    #
    # @return The most bottom-left node.
    def _most_bottom_left(self):
        return self._most_target(0, self._height)

    ## Get the node in the graph that is the most bottom-right; this is where
    ## "Inky" will spawn.
    #
    # @return The most bottom-right node.
    def _most_bottom_right(self):
        return self._most_target(self._width, self._height)

    ## Get the node in the graph that is the closest to some arbitrary
    ## coordinates.
    #
    # @param x The target x coordinate.
    # @param y The target y coordinate.
    #
    # @return The node in the graph that is closest to the target coordinates.
    def _most_target(self, x, y):
        target = Node(Coordinate(x, y))
        best_node = None
        best_distance = 100000.0
        for node in self._nodes:
            if len(node.geoneighbours) < 2:
                continue
            distance = node.distance(target)
            if distance < best_distance:
                best_distance = distance
                best_node = node
        return best_node

    ## Get the node in the graph that is the closest to some arbitrary
    ## coordinates. This public function is a wrapper for the internal
    ## `_most_target' function.
    #
    # @param x The target x coordinate.
    # @param y The target y coordinate.
    #
    # @return The node in the graph that is closest to the target coordinates.
    def closest_node(self, x, y):
        return self._most_target(x, y)

    ## Join two nodes in the graph together by creating an edge between them.
    #
    # @param node_a The first node.
    # @param node_b The second node.
    def _join(self, node_a, node_b):
        node_a.add_neighbour(node_b)
        node_b.add_neighbour(node_a)
    
    ## Generate a maze. When the nodes are generated by the abstract
    ## `_generate_nodes' function, we only know which nodes are `next to'
    ## other nodes. We need to join them together by creating edges to create
    ## a complete maze, free from dead ends. The maze structure is generated
    ## randomly, but sometimes the nodes in the graph do not allow a maze
    ## structure.
    #
    # @return True if a maze was successfully generated, false otherwise.
    def _generate_maze(self):
        walls = []
        nodes = self._nodes
        for node in nodes:
            if len(node.geoneighbours) < 2:
                while len(node.geoneighbours) > 0:
                    neighbour = node.geoneighbours[0]
                    node.remove_geoneighbour(neighbour)
                    neighbour.remove_geoneighbour(node)
        node = None
        for n in nodes:
            if len(n.geoneighbours) > 2:
                node = n
                break
        if node is None:
            return False
        for neighbour in node.geoneighbours:
            walls += [(node, neighbour)]
        for node in nodes:
            node.visited = False
        nodes[0].visited = True
        
        while len(walls) > 0:
            wall = random.choice(walls)
            a = wall[0]
            b = wall[1]
            if not b.visited:
                self._join(a, b)
                b.visited = True
                for neighbour in b.geoneighbours:
                    if not neighbour.visited:
                        walls += [(b, neighbour)]
            walls.remove(wall)
        self._remove_dead_ends()
        return True
    
    ## Remove any dead ends remaining in the maze. Dead ends are not a part of
    ## the original game, and would make the ghosts misbehave, as under normal
    ## circumstances they cannot turn around.
    def _remove_dead_ends(self):
        for node in self._nodes:
            if len(node.geoneighbours) > 1:
                while len(node.neighbours) < 2:
                    neighbour = random.choice(node.geoneighbours)
                    self._join(node, neighbour)
    
    ## Having generated a maze we need to create all the dots that will
    ## exist in the maze.
    #
    # @return A list of dots.
    def _generate_dots(self):
        dots = []
        starts = [
            self._avatar_start,
            self._blinky_start,
            self._clyde_start,
            self._inky_start,
            self._pinky_start,
        ]
        for node in self._nodes:
            if len(node.neighbours) > 0:
                if node in starts:
                    continue
                dot = Dot(node.coordinate)
                dots += [dot]
        return dots
    
    ## Generate a list of powers that will exist in the maze.
    #
    # @return A list of power pills.
    def _generate_powers(self):
        powers = []
        while len(powers) < 4:
            dot = random.choice(self._dots)
            power = Power(dot.coordinate)
            self._dots.remove(dot)
            powers += [power]
        return powers

    ## Get the starting location for a particular sprite.
    #
    # @param name The name of the sprite. Should be "avatar", "blinky",
    # "pinky", "inky" or "clyde".
    #
    # @return The node where the sprite will start.
    def start_pos(self, name):
        if name == "avatar":
            return self._avatar_start
        elif name == "blinky":
            return self._blinky_start
        elif name == "pinky":
            return self._pinky_start
        elif name == "inky":
            return self._inky_start
        elif name == "clyde":
            return self._clyde_start
        else:
            raise ValueError(f"sprite name {name} not recognised")

    ## Get the logical width of the Arena.
    #
    # @return The logical width of the Arena.
    @property
    def logical_width(self):
        return self._logical_width

    ## Get the logical height of the Arena.
    #
    # @return The logical height of the Arena.
    @property
    def logical_height(self):
        return self._logical_height

    ## Get the dots in the Arena.
    #
    # @return A list of dots.
    @property
    def dots(self):
        return self._dots

    ## Get the power pills in the Arena.
    #
    # @return A list of powers.
    @property
    def powers(self):
        return self._powers

    ## Get the nodes in the Arena.
    #
    # @return A list of nodes.
    @property
    def nodes(self):
        return self._nodes

    ## Get a rectangle describing the Arena in terms of width and height.
    #
    # @return A rectangle.
    @property
    def rect(self):
        return Rect(self._width, self._height)
    
    ## Get the actual width of the Arena.
    #
    # @return The width of the Arena.
    @property
    def width(self):
        return self._width
    
    ## Get the actual height of the Arena.
    #
    # @return The height of the Arena.
    @property
    def height(self):
        return self._height
