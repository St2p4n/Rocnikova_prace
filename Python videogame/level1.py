from setting import *


class Level1():
    def __init__(self):
        super().__init__()
        self.block = pygame.image.load("data/Levels/level1.png")
        self.block_rect = self.block.get_rect(topleft=(0, 0))