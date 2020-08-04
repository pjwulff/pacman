import pygame

class Sprite:
    def __init__(self, arena, x, y, name):
        self._name = name
        self._arena = arena
        self._x = x
        self._y = y
        self._image = pygame.image.load(f"data/{name}.png").convert()
        self._rect = self._image.get_rect()

    def erase(self, screen):
        self._arena.draw(screen, self.rect())

    def draw(self, screen):
        screen.blit(self._image, self.rect())

    def position(self):
        return (self._x, self._y)

    def rect(self):
        (x, y) = self.position()
        x -= self._rect.width/2
        y -= self._rect.height/2
        return self._rect.move(x, y)

    def name(self):
        return self._name
