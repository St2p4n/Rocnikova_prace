from setting import *
from level import Level
from level1 import Level1
from level2 import Level2
from level3 import Level3

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pirates")
        self.clock = pygame.time.Clock()
        self.current_stage = Level() 
        self.transitioning = False
        self.transition_alpha = 0

    def handle_transition(self):
        if self.transitioning:
            self.transition_alpha += 15
            if self.transition_alpha >= 255:
                self.transitioning = False
                self.transition_alpha = 0
                return True  # Transition complete 
        return False

    def run(self):
        running = True
        while running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
            
            # Run current stage and check for level completion
            result = self.current_stage.run()
            if result is not None and not isinstance(result, type(self.current_stage)):
                self.transitioning = True
                if self.handle_transition():
                    self.current_stage = result  # Switch to the new level
                continue
            
            # Level switching
            if isinstance(self.current_stage, Level):
                keys = pygame.key.get_pressed()
                if hasattr(self.current_stage, 'player_rect'):
                    player_pos = self.current_stage.player_rect.topleft
                    
                    # Switch to Level1
                    if player_pos == (600, 420) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level1()
                    
                     # Switch to Level1
                    if 360 >= player_pos[0] >= 350 and player_pos[1] == 200 and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level2()             
                                      
                    # Switch to Level3
                    elif player_pos == (-770, 440) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level3()
            
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()      
        sys.exit()

if __name__ == '__main__':  
    game = Game()
    game.run()