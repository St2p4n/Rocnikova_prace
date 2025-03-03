from setting import *
from level import Level
class Level1:
    def __init__(self):
        self.player_rect = pygame.Rect(50, 620, 10, 10)  
        self.background = pygame.image.load("data/Levels/Level1.png")
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.player = pygame.image.load("data/Aseprite/Pirate.png")

    def run(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.blit(self.background, (0, 0))
        self.display_surface.blit(self.player, self.player_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.current_stage = Level()

