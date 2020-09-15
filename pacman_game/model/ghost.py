import random
from itertools import count
from queue import PriorityQueue
from .moving_sprite import MovingSprite

GHOST_RADIUS = 9

class Ghost(MovingSprite):
    """! Base class for all Ghost types. Handles duties common to all ghosts,
    including moving around the maze. This class expects the 'target' method
    to be overridden by subclasses to find where the ghost should head during
    'chase' mode."""
    def __init__(self, arena, name):
        """! Construct a new Ghost.

        @param arena The arena to which this ghost belongs.
        @param name The name of the ghost. This is used to extract relevant information
        from the arena object."""
        MovingSprite.__init__(self, arena, GHOST_RADIUS, name)
        self.alive = True
        self.mode = "scatter"
        self._path = None
    
    def target(self, avatar, ghosts):
        pass
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, mode):
        self._mode = mode

    @property
    def scared(self):
        return self._mode == "frighten"

    @property
    def alive(self):
        """! Gets the status of whether or not the ghost is alive; ie., can be
        interacted with by the avatar.

        @returns True if the ghost is alive, False otherwise."""
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive
    
    @property
    def return_position(self):
        return self._arena.ghost_return_position()
    
    @property
    def scatter_target(self):
        return self._arena.scatter_target(self.name)
    
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
            queue.put((f, (next(unique), g, neighbour, [prev, source, neighbour])))
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
