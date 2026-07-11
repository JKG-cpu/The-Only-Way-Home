import pygame
from pygame.math import Vector2 as vector

from .entity import Entity

class Player(Entity):
    def __init__(self, pos: tuple[int, int], groups: pygame.sprite.Group, collision_sprites: pygame.sprite.Group) -> None:
        super().__init__(pos, (50, 100), groups, collision_sprites)
        self.image.fill("red")

        self.jump_speed = 600

    def handle_events(self, events: list[pygame.Event]) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump()

    def input(self) -> None:
        keys = pygame.key.get_pressed()
        temp_vector = vector()

        if keys[pygame.K_a]:
            temp_vector.x -= 1
        
        if keys[pygame.K_d]:
            temp_vector.x += 1
    
        self.direction = temp_vector

    def jump(self) -> None:
        if self.on_floor:
            self.velocity.y = -self.jump_speed

    def update(self, dt: float) -> None:
        self.input()
        self.move(dt)
        self.draw()
