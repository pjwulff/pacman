import pygame
from .moving_sprite import MovingSprite

class Avatar(MovingSprite):
    def __init__(self, arena):
        MovingSprite.__init__(self, arena, "avatar")

    def _new_direction(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self._from_pos.neighbour("left") is not None:
            return "left"
        elif keys_pressed[pygame.K_RIGHT] and self._from_pos.neighbour("right") is not None:
            return "right"
        elif keys_pressed[pygame.K_UP] and self._from_pos.neighbour("up") is not None:
            return "up"
        elif keys_pressed[pygame.K_DOWN] and self._from_pos.neighbour("down") is not None:
            return "down"
        if self._from_pos.neighbour(self._direction) is not None:
            return self._direction
        else:
            return None

    def _turn_around(self):
        keys_pressed = pygame.key.get_pressed()
        if self._direction == "left" and keys_pressed[pygame.K_RIGHT]:
            return True
        if self._direction == "right" and keys_pressed[pygame.K_LEFT]:
            return True
        if self._direction == "up" and keys_pressed[pygame.K_DOWN]:
            return True
        if self._direction == "down" and keys_pressed[pygame.K_UP]:
            return True
        return False

    def _eat(self):
        contents = self._from_pos.contents()
        if contents is not None:
            self._from_pos.set_contents(None)
            self._arena.eat(contents)

    def _pick_initial_direction(self):
        self._direction = self._new_direction()
        if self._direction is not None:
            self._start = False
            if self._from_pos.neighbour(self._direction) != self._to_pos:
                temp = self._from_pos
                self._from_pos = self._to_pos
                self._to_pos = temp
            self._calculate_speed()

    def _update_arrived(self):
        self._eat()
