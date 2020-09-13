import random
from .coordinate import Coordinate
from .direction import Direction
from .dot import Dot
from .node import Node
from .power import Power
from .rect import Rect

class Arena:
    """! The Arena class is responsible for loading mazes from JSON files.
    It also spawns the dots and power pills contained in the maze. This class
    extracts information from the JSON maze file and makes it available to
    other objects."""
    def __init__(self, rect):
        width = rect.width
        height = rect.height
        self._width = width * 24 + 48
        self._height = height * 24 + 120
        self._logical_width = width
        self._logical_height = height
        self.generate()
    
    def generate(self):
        width = self.logical_width
        height = self.logical_height
        self._nodes = self._generate_nodes(width, height)
        self._generate_maze()
        self._dots = self._generate_dots()
        self._powers = self._generate_powers()
    
    def _join(self, node_a, node_b):
        for direction in node_a.geoneighbours:
            if node_b == node_a.geoneighbour(direction):
                node_a.set_neighbour(direction, node_b)
        for direction in node_b.geoneighbours:
            if node_a == node_b.geoneighbour(direction):
                node_b.set_neighbour(direction, node_a)
    
    def _generate_maze(self):
        walls = []
        nodes = self._nodes
        node = nodes[self._logical_width//2][self._logical_height-1]
        for direction in node.geoneighbours:
            walls += [(node, node.geoneighbour(direction))]
        for i in range(self._logical_width):
            for j in range(self._logical_height):
                nodes[i][j].visited = False
        node.visited = True
        
        while len(walls):
            wall = random.choice(walls)
            a = wall[0]
            b = wall[1]
            if not b.visited:
                self._join(a, b)
                b.visited = True
                for direction in b.geoneighbours:
                    neighbour = b.geoneighbour(direction)
                    if neighbour is not None and not neighbour.visited:
                        walls += [(b, b.geoneighbour(Direction(direction)))]
            walls.remove(wall)
        self._remove_dead_ends()
    
    def _remove_dead_ends(self):
        for i in range(self._logical_width):
            for j in range(self._logical_height):
                node = self._nodes[i][j]
                while len(node.neighbours) < 2:
                    lst = list(node.geoneighbours.keys())
                    direction = random.choice(lst)
                    if node.neighbour(direction) is None:
                        neighbour = node.geoneighbour(direction)
                        if neighbour is not None:
                            self._join(node, neighbour)
    
    def _generate_dots(self):
        dots = []
        for i in range(self._logical_width):
            for j in range(self._logical_height):
                node = self._nodes[i][j]
                dot = Dot(self, node.coordinate)
                dots += [dot]
        return dots
    
    def _generate_powers(self):
        return []
        
    def scatter_target(self, name):
        targets = {
            "blinky": Coordinate(self.width, 0),
            "pinky": Coordinate(0, 0),
            "inky": Coordinate(self.width, self.height),
            "clyde": Coordinate(0, self.height)
        }
        return targets[name]

    def start_pos(self, name):
        if name == "avatar":
            return self._avatar_start
        else:
            return self._ghost_start

    @property
    def logical_width(self):
        return self._logical_width

    @property
    def logical_height(self):
        return self._logical_height

    @property
    def dots(self):
        """! Get all the dots in the arena.

        @returns A list of all the dots in the arena."""
        return self._dots

    @property
    def powers(self):
        """! Get all the power pills in the arena.

        @returns A list of all the power pills in the arena."""
        return self._powers

    def ghost_return_position(self):
        """! Get the return position for the ghosts.

        @returns The return position for the ghosts."""
        pos = self._arena_data['ghost-return']
        return self._nodes[pos]

    @property
    def nodes(self):
        return self._nodes

    @property
    def rect(self):
        return Rect(self._width, self._height)
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height