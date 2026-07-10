import pygame
from ..utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from ..utils import cc

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Only Way Home")

        self.running: bool = True
        self.clock = pygame.time.Clock()
    
    # Handle pygame events
    def handle_events(self, events: list[pygame.Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

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
        pass

    # Draw Objects
    def draw(self) -> None:
        self.screen.fill("black")
        
        pygame.display.update()
