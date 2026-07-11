import pygame
from pygame.math import Vector2 as vector

from ..utils.constants import GRAVITY

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], groups: pygame.sprite.Group, collision_sprites: pygame.sprite.Group) -> None:
        super().__init__(groups)
        self.screen = pygame.display.get_surface()

        # self.sprites: dict[str, list[pygame.Surface]] = sprites
        # self.image = self.sprites["idle"][0]

        self.image = pygame.Surface(size)
        self.rect = self.image.get_frect(topleft = pos)

        self.collision_sprites = collision_sprites

        self.direction = vector() # Input
        self.velocity = vector() #  Physics
        self.speed = 250
        self.on_floor = False

    def move(self, dt: float) -> None:
        self.rect.x += self.direction.x * dt * self.speed
        self.collisions("Horizontal")

        self.on_floor = False
        self.velocity.y += GRAVITY * dt
        self.rect.y += self.velocity.y * dt
        self.collisions("Vertical")

    def collisions(self, axis: str) -> None:
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == "Horizontal":
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    
                    elif self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                
                elif axis == "Vertical":
                    if self.velocity.y > 0:
                        self.on_floor = True
                        self.rect.bottom = sprite.rect.top
                    
                    elif self.velocity.y < 0:
                        self.rect.top = sprite.rect.bottom

    def draw(self) -> None:
        self.screen.blit(self.image, self.rect)
    
    def update(self, dt) -> None:
        self.move(dt)