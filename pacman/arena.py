import json
import pygame
from .dot import *
from .node import *
from .power import *

class Arena:
    """! The Arena class is responsible for loading mazes from JSON files.
    It also spawns the dots and power pills contained in the maze. This class
    extracts information from the JSON maze file and makes it available to
    other objects."""
    def __init__(self):
        """! Constructs an Arena object."""
        with open("data/square-board.json") as f:
            self._arena_data = json.load(f)
        self._image = pygame.image.load(self._arena_data['image']).convert()
        self._screen_rect = self._image.get_rect()
        self._create_nodes()

    def _create_nodes(self):
        self._nodes = {}
        self._dots = []
        self._powers = []
        for node_id in self._arena_data['nodes']:
            node = self._arena_data['nodes'][node_id]
            x = node['x']
            y = node['y']
            new_node = Node(self, x, y)
            if 'contents' in node:
                if node['contents'] == "dot":
                    dot = Dot(self, x, y)
                    self._dots += [dot]
                    new_node.set_contents(dot)
                elif node['contents'] == "power":
                    power = Power(self, x, y)
                    self._powers += [power]
                    new_node.set_contents(power)
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

    def draw(self, screen, rect = None):
        """! Draws the entire arena background to the screen, or optionally
        just a section of it. This is used to erase a sprite.

        @param screen The PyGame screen object on which to draw.
        @param rect An optional Rect object to specify which part of the Arena
        to drawn. If not given, this method draws the entire arena."""
        if rect is None:
            screen.fill((0, 0, 0))
            screen.blit(self._image, self._screen_rect)
        else:
            screen.blit(self._image, rect, rect)

    def scatter_target(self, name):
        """! Extracts the 'scatter-target' information from the maze JSON file.

        @param name The name of the object to which the scatter target is associated.
        @returns The coordinates of the scatter target."""
        return self._arena_data['scatter-target'][name]

    def start_pos(self, name):
        """! Extracts the start position information from the maze JSON file.

        @param name The name of the object to which the start position is associated.
        @returns The start position of the object."""
        pos = self._arena_data['start'][name]
        return (self._nodes[pos[0]], self._nodes[pos[1]])

    def dots(self):
        """! Get all the dots in the arena.

        @returns A list of all the dots in the arena."""
        return self._dots

    def powers(self):
        """! Get all the power pills in the arena.

        @returns A list of all the power pills in the arena."""
        return self._powers

    def ghost_return_position(self):
        """! Get the return position for the ghosts.

        @returns The return position for the ghosts."""
        return self._arena_data['ghost-return']
