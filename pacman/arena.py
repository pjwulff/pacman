import json
import pygame
from .dot import *
from .node import *

class Arena:
    def __init__(self):
        with open("data/square-board.json") as f:
            self.arena_data = json.load(f)
        self.image = pygame.image.load(self.arena_data['image']).convert()
        self.screen_rect = self.image.get_rect()
        self.create_nodes()

    def create_nodes(self):
        self.nodes_ = {}
        self.dots_ = []
        for node_id in self.arena_data['nodes']:
            node = self.arena_data['nodes'][node_id]
            x = node['x']
            y = node['y']
            new_node = Node(x, y)
            self.nodes_[node_id] = new_node
            if node['contents'] == "dot":
                self.dots_ += [Dot(self, x, y)]

        for node_id in self.arena_data['nodes']:
            node = self.arena_data['nodes'][node_id]
            for direction in node['neighbours']:
                neighbour = node['neighbours'][direction]
                self.nodes_[node_id].set_neighbour(direction, neighbour)

    def draw(self, screen, rect = None):
        if rect is None:
            screen.fill((0, 0, 0))
            screen.blit(self.image, self.screen_rect)
        else:
            screen.blit(self.image, self.screen_rect, rect)

    def start_pos(self):
        return self.nodes_[self.arena_data['start']]

    def dots(self):
        return self.dots_
