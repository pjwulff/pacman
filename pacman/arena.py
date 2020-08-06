import json
import pygame
from .dot import *
from .node import *
from .power import *
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky

class Arena:
    def __init__(self):
        with open("data/square-board.json") as f:
            self.arena_data = json.load(f)
        self.image = pygame.image.load(self.arena_data['image']).convert()
        self.screen_rect = self.image.get_rect()
        self.create_nodes()
        self.create_ghosts()

    def create_nodes(self):
        self.nodes_ = {}
        self.dots_ = []
        self.powers_ = []
        for node_id in self.arena_data['nodes']:
            node = self.arena_data['nodes'][node_id]
            x = node['x']
            y = node['y']
            new_node = Node(self, x, y)
            if 'contents' in node:
                if node['contents'] == "dot":
                    dot = Dot(self, x, y)
                    self.dots_ += [dot]
                    new_node.set_contents(dot)
                elif node['contents'] == "power":
                    power = Power(self, x, y)
                    self.powers_ += [power]
                    new_node.set_contents(power)
            self.nodes_[node_id] = new_node

        for node_id in self.arena_data['nodes']:
            node = self.arena_data['nodes'][node_id]
            for direction in node['neighbours']:
                neighbour = self.nodes_[node['neighbours'][direction]]
                self.nodes_[node_id].set_neighbour(direction, neighbour)
            if 'portals' in node:
                for direction in node['portals']:
                    portal = self.nodes_[node['portals'][direction]]
                    self.nodes_[node_id].set_portal(direction, portal)

    def create_ghosts(self):
        self._ghosts = {
            "blinky": Blinky(self),
            "pinky": Pinky(self),
            "iinky": Inky(self),
        }

    def ghosts(self):
        return self._ghosts

    def draw(self, screen, rect = None):
        if rect is None:
            screen.fill((0, 0, 0))
            screen.blit(self.image, self.screen_rect)
        else:
            screen.blit(self.image, rect, rect)

    def eat(self, contents):
        if contents.name() is "dot":
            self.dots_.remove(contents)
        elif contents.name() is "power":
            self.powers_.remove(contents)

    def scatter_target(self, name):
        return self.arena_data['scatter-target'][name]

    def start_pos(self, name):
        pos = self.arena_data['start'][name]
        return (self.nodes_[pos[0]], self.nodes_[pos[1]])

    def dots(self):
        return self.dots_

    def powers(self):
        return self.powers_

    def rect(self):
        return self.screen_rect
