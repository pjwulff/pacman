import random
from itertools import count
from queue import PriorityQueue
from .moving_sprite import MovingSprite

GHOST_RADIUS = 9

## Abstract base class for all Ghosts in the game. This class handles duties
## common to all ghosts.
class Ghost(MovingSprite):

    ## Create a new ghost.
    #
    # @param arena The Arena where this ghost will live.
    # @param name The name of this ghost. Should be either "blinky", "clyde",
    # "inky" or "pinky".
    def __init__(self, arena, name):
        MovingSprite.__init__(self, arena, GHOST_RADIUS, name)
        self.alive = True
        self.mode = "scatter"
        self._path = None
    
    ## This abstract function needs to be overridden by sub-classes. It should
    ## calculate the target for the ghost when in chase mode.
    #
    # @param avatar The Avatar object.
    # @param ghosts A dictionary for the ghosts.
    #
    # @return The coordinates of the ghost's target.
    def target(self, avatar, ghosts):
        pass
    
    ## Get the current mode or behaviour for this ghost.
    #
    # @return The current mode or behaviour for this ghost.
    @property
    def mode(self):
        return self._mode
    
    ## Set the current mode or behaviour for this ghost.
    #
    # @param mode The current mode or behaviour for this ghost. Should only be
    # "scatter", "chase" or "frighten".
    @mode.setter
    def mode(self, mode):
        self._mode = mode

    ## Get whether or not this ghost is currently "scared" (because the Avatar
    ## has consumed a power pill). Equivalently, if this ghost's current mode
    ## is "frighten".
    #
    # @return True if this ghost is frightened.
    @property
    def scared(self):
        return self._mode == "frighten"

    ## Returns whether or not this ghost is currently `alive'; that is, if has
    ## has not been eaten by the Avatar.
    #
    # @return True if the ghost is alive.
    @property
    def alive(self):
        return self._alive

    ## Sets whether or not this ghost is currently `alive'. This should be set
    ## to False when the ghost is eaten by the Avatar.
    #
    # @param alive Whether or not the ghost is alive.
    @alive.setter
    def alive(self, alive):
        self._alive = alive
    
    ## Perform an A*-search to find the shortest path between some source
    ## node and target coordinate. This function takes into account the fact
    ## that ghosts cannot reverse direction.
    #
    # @param source The source node from which to start the search.
    # @param target The target coordinates.
    # @param prev The previously visited node. This node will be excluded from
    # the search as ghosts cannot reverse direction.
    #
    # @return A list of nodes representing the shortest path between the source
    # and the target.
    def path(self, source, target, prev = None):
        target_node = self._arena.closest_node(target.x, target.y)
        unique = count()
        queue = PriorityQueue()
        if source == target_node:
            return None
        for neighbour in source.neighbours:
            if neighbour == prev:
                continue
            g = source.distance(neighbour)
            h = self._arena.heuristic(neighbour, target_node)
            if h is None:
                h = target_node.distance(neighbour)
            f = g + h
            queue.put((f,
                       (next(unique), g, neighbour,
                        [prev, source, neighbour])))
        while not queue.empty():
            elem = queue.get()
            cost = elem[1][1]
            node = elem[1][2]
            path = elem[1][3][:]
            prev = path[-1]
            if node == target_node:
                return path
            for neighbour in node.neighbours:
                if neighbour == prev:
                    continue
                g = cost + node.distance(neighbour)
                h = self._arena.heuristic(neighbour, target_node)
                if h is None:
                    h = target_node.distance(neighbour)
                f = g + h
                queue.put((f, (next(unique), g, neighbour, path + [neighbour])))
