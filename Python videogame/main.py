
from setting import *
from level import Level
from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4 
from level5 import Level5

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pirates")
        self.clock = pygame.time.Clock()
        self.current_stage = Level()
        self.transitioning = False  
        self.transition = 0

    def handle_transition(self):                      
        if self.transitioning:
            self.transition += 15                        
            if self.transition >= 255:
                self.transitioning = False 
                self.transition = 0     
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
                    # Handle return from different levels with specific positions
                    if isinstance(self.current_stage, Level1):
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):
                            self.current_stage.player_rect.topleft = (600, 420)
                            self.current_stage.current_segment = 0
                    elif isinstance(self.current_stage, Level2):
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):
                            self.current_stage.player_rect.topleft = (360, 200)
                            self.current_stage.current_segment = 2
                    elif isinstance(self.current_stage, Level3):
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):
                            self.current_stage.player_rect.topleft = (-770, 440)
                            self.current_stage.current_segment = 4
                    elif isinstance(self.current_stage, Level4):        
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'): 
                            self.current_stage.player_rect.topleft = (-1005, 80)
                            self.current_stage.current_segment = 7 
                    elif isinstance(self.current_stage, Level5):      
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):     
                            self.current_stage.player_rect.topleft = (600, 420)       
                            self.current_stage.current_segment = 0
                    else: 
                        self.current_stage = result  
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
                    # Switch to Level2
                    if 360 >= player_pos[0] >= 350 and player_pos[1] == 200 and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level2()           
                    # Switch to Level3
                    elif player_pos == (-770, 440) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level3()
                    # Switch to Level4
                    elif -1010 <= player_pos[0] <= -990 and player_pos[1] == 80 and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level4()
                    # Switch to Level5
                    elif player_pos == (-100, -710) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level5()
                            
            pygame.display.update()
            self.clock.tick(45) 

        pygame.quit()      
        sys.exit()

if __name__ == '__main__':  
    game = Game()
    game.run()