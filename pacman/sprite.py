import pygame

class Sprite:
    def __init__(self, arena, x, y, image):
        self.arena = arena
        self.x_ = x
        self.y_ = y
        self.image = pygame.image.load(image).convert()
        self.rect_ = self.image.get_rect()

    def erase(self, screen):
        self.arena.draw(screen, self.rect())

    def draw(self, screen):
        screen.blit(self.image, self.rect())

    def position(self):
        return (self.x_, self.y_)

    def rect(self):
        (x, y) = self.position()
        x -= self.rect_.width/2
        y -= self.rect_.height/2
        r = self.rect_.move(x, y)
        return r
