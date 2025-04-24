from setting import *
from level import Level
from level1 import Level1
from level2 import Level2
from level3 import Level3
<<<<<<< HEAD
from level4 import Level4 
from level5 import Level5
=======
from level4 import Level4
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
      
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pirates")
        self.clock = pygame.time.Clock()
        self.current_stage = Level()
        self.transitioning = False  
        self.transition = 0

<<<<<<< HEAD
    def handle_transition(self):                      
        if self.transitioning:
            self.transition += 15                        
            if self.transition >= 255:
                self.transitioning = False 
                self.transition = 0     
                return True  # Transition complete       
        return False                        
=======
    def handle_transition(self):
        if self.transitioning:
            self.transition += 15
            if self.transition >= 255:
                self.transitioning = False 
                self.transition = 0
                return True  # Transition complete 
        return False 
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
             
    def run(self):           
        running = True
        while running:     
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
<<<<<<< HEAD
                    running = False       
            # Run current stage and check for level completion
            result = self.current_stage.run()         
=======
                    running = False
            
            # Run current stage and check for level completion
            result = self.current_stage.run()
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
            if result is not None and not isinstance(result, type(self.current_stage)):
                self.transitioning = True
                if self.handle_transition(): 
                    # Handle return from different levels with specific positions
                    if isinstance(self.current_stage, Level2):
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):
                            self.current_stage.player_rect.topleft = (360, 200)
                            self.current_stage.current_segment = 2
                    elif isinstance(self.current_stage, Level3):
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):
                            self.current_stage.player_rect.topleft = (-770, 440)
                            self.current_stage.current_segment = 4
<<<<<<< HEAD
                    elif isinstance(self.current_stage, Level4):        
=======
                    elif isinstance(self.current_stage, Level4):
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'): 
                            self.current_stage.player_rect.topleft = (-1005, 80)
                            self.current_stage.current_segment = 7 
<<<<<<< HEAD
                    elif isinstance(self.current_stage, Level5):      
                        self.current_stage = Level()
                        if hasattr(self.current_stage, 'player_rect'):     
                            self.current_stage.player_rect.topleft = (600, 420)       
                            self.current_stage.current_segment = 0
                    else: 
                        self.current_stage = result  
=======
                    else: 
                        self.current_stage = result  # Normal level switch
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
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
<<<<<<< HEAD
=======
                    
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
                    # Switch to Level2
                    if 360 >= player_pos[0] >= 350 and player_pos[1] == 200 and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level2()           
<<<<<<< HEAD
=======
                                      
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
                    # Switch to Level3
                    elif player_pos == (-770, 440) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level3()
                    # Switch to Level4
                    elif player_pos == (-1005, 80) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level4()
<<<<<<< HEAD
                    # Switch to Level5
                    elif player_pos == (-100, -710) and keys[pygame.K_SPACE]:
                        self.transitioning = True
                        if self.handle_transition():
                            self.current_stage = Level5()
=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
                            
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()      
        sys.exit()

if __name__ == '__main__':  
    game = Game()
    game.run()