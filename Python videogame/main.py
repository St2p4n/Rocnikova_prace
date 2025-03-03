from setting import *
from level import Level
from level1 import Level1

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pirates")

        self.current_stage = Level() 

    def switch_level(self):
        keys = pygame.key.get_pressed()
        if hasattr(self.current_stage, "player_rect"):
            if self.current_stage.player_rect.topleft == (600, 420) and keys[pygame.K_SPACE]:
                self.current_stage = Level1()  # Switch level
        else:
            print("Error!")  # Debugging output

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.switch_level()  #Kontrola přepnutí levelu
            self.current_stage.run() 
            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
