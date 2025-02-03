from setting import *

class Level:
    def __init__(self):
       self.display_surface = pygame.display.get_surface()

    def run(self):
       #background = pygame.image.load("data/Aseprite/background.png")
       #self.display_surface.blit(background, (0,0))

       player = pygame.image.load("data/Aseprite/Pirate.png")
       self.display_surface.blit(player, (100,100))

      #crab = pygame.image.load("data/Aseprite/Crab.png")
       #self.display_surface.blit(crab, (200,200))


     