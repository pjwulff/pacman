import json
import pkg_resources
from .coordinate import Coordinate
from .dot import Dot
from .node import Node
from .power import Power
from .rect import Rect

class Arena:
    """! The Arena class is responsible for loading mazes from JSON files.
    It also spawns the dots and power pills contained in the maze. This class
    extracts information from the JSON maze file and makes it available to
    other objects."""
    def __init__(self):
        """! Constructs an Arena object."""
        path = pkg_resources.resource_filename(__name__, "../data/boards/square-board.json")
        with open(path) as f:
            self._arena_data = json.load(f)
        self.create_nodes()
        self._width = self._arena_data['width']
        self._height = self._arena_data['height']

    def image(self):
        return self._arena_data['image']

    def create_nodes(self):
        self._nodes = {}
        self._dots = []
        self._powers = []
        for node_id in self._arena_data['nodes']:
            node = self._arena_data['nodes'][node_id]
            x = node['x']
            y = node['y']
            coordinate = Coordinate(x, y)
            new_node = Node(self, coordinate)
            if 'contents' in node:
                if node['contents'] == "dot":
                    dot = Dot(self, coordinate)
                    self._dots += [dot]
                elif node['contents'] == "power":
                    power = Power(self, coordinate)
                    self._powers += [power]
            self._nodes[node_id] = new_node

        for node_id in self._arena_data['nodes']:
            node = self._arena_data['nodes'][node_id]
            for direction in node['neighbours']:
                neighbour = self._nodes[node['neighbours'][direction]]
                self._nodes[node_id].set_neighbour(direction, neighbour)
            if 'portals' in node:
                for direction in node['portals']:
                    portal = self._nodes[node['portals'][direction]]
                    self._nodes[node_id].set_portal(direction, portal)

    def scatter_target(self, name):
        """! Extracts the 'scatter-target' information from the maze JSON file.

        @param name The name of the object to which the scatter target is associated.
        @returns The coordinates of the scatter target."""
        s = self._arena_data['scatter-target'][name]
        return Coordinate(s[0], s[1])

    def start_pos(self, name):
        """! Extracts the start position information from the maze JSON file.

        @param name The name of the object to which the start position is associated.
        @returns The start position of the object."""
        pos = self._arena_data['start'][name]
        return (self._nodes[pos[0]], self._nodes[pos[1]])

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
    def rect(self):
        return Rect(self._width, self._height)
