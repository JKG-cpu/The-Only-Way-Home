import pygame

from ..utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from ..utils import cc
from ..entities import Player, Entity


class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Only Way Home")

        self.running: bool = True
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.ground = Entity((0, SCREEN_HEIGHT - 100), (SCREEN_WIDTH, 100), (self.all_sprites, self.collision_sprites), self.collision_sprites)
        self.ground.image.fill("blue")

        self.player = Player((100, 100), (self.all_sprites), self.collision_sprites)

    # Handle pygame events
    def handle_events(self, events: list[pygame.Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            
        self.player.handle_events(events)

    # Run Game Loop
    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            events = pygame.event.get()

            self.handle_events(events)
            self.update(dt)
            self.draw()

        cc()
        pygame.quit()

    # Update objects
    def update(self, dt: float) -> None:
        self.player.update(dt)

    # Draw Objects
    def draw(self) -> None:
        self.screen.fill("black")

        self.player.draw()
        self.ground.draw()

        pygame.display.update()
