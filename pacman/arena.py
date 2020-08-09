import json
import pygame
from .dot import *
from .node import *
from .power import *

class Arena:
    def __init__(self):
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
        if rect is None:
            screen.fill((0, 0, 0))
            screen.blit(self._image, self._screen_rect)
        else:
            screen.blit(self._image, rect, rect)

    def scatter_target(self, name):
        return self._arena_data['scatter-target'][name]

    def start_pos(self, name):
        pos = self._arena_data['start'][name]
        return (self._nodes[pos[0]], self._nodes[pos[1]])

    def dots(self):
        return self._dots

    def powers(self):
        return self._powers

    def rect(self):
        return self._screen_rect

    def ghost_return_position(self):
        return self._arena_data['ghost-return']
