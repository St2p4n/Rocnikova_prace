from setting import *
from level import Level

class Game:
    def run(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption(("Pirates"))

        self.current_stage = Level()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.current_stage.run()

            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()

