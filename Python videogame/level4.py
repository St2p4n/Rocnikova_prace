from setting import *
from level import Level

class Level4:
    def __init__(self):
        pygame.init()  
        self.display_surface = pygame.display.get_surface()
        self.player_rect = pygame.Rect(1705, 930, 30, 50)
        self.player_color = (255, 0, 0)
        self.player = pygame.image.load("data/Aseprite/Pirate.png")
 
        self.walking_left = pygame.image.load("data/Aseprite/walking_left.png")
        self.walking_left2 = pygame.image.load("data/Aseprite/walking_left2.png")
        self.walking_left3 = pygame.image.load("data/Aseprite/walking_left3.png")

        self.walking_right = pygame.image.load("data/Aseprite/walking_right.png")
        self.walking_right2 = pygame.image.load("data/Aseprite/walking_right2.png")
        self.walking_right3 = pygame.image.load("data/Aseprite/walking_right3.png")

        self.background = pygame.image.load("data/Levels/Level4.png")
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Load moving platform image
        self.moving_platform_img = pygame.image.load("data/Aseprite/moving_platform.png")
        self.moving_platform_img = pygame.transform.scale(self.moving_platform_img, (100, 10))

        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 1.2
        self.jump_strength = -20
        self.on_ground = False
        
        # Heart-based health system (3 hearts)
        self.max_hearts = 3
        self.hearts = self.max_hearts
        self.heart_img = pygame.image.load("data/Aseprite/heart.png")  
        self.heart_img = pygame.transform.scale(self.heart_img, (50, 50))
        self.empty_heart_img = pygame.image.load("data/Aseprite/empty_heart.png")
        self.empty_heart_img = pygame.transform.scale(self.empty_heart_img, (50, 50))
        
        # Load moving platform image
        self.moving_platform_img = pygame.image.load("data/Aseprite/moving_platform.png")
        self.moving_platform_img = pygame.transform.scale(self.moving_platform_img, (140, 70))

        # Load crab enemy sprites
        self.crab_img = pygame.image.load("data/Aseprite/crab.png")
        self.crab_img2 = pygame.image.load("data/Aseprite/crab2.png")
        self.current_crab_img = self.crab_img

        # Enemy 
        self.enemy = pygame.Rect(700, 1008, 30, 50)
        self.color = (255, 0, 0)
        self.last_hit_time = 0
        self.hit_cooldown = 1000  # 1 second cooldown in milliseconds
        self.enemy_speed = 3
        self.enemy_direction = 1
        self.enemy_move_range = 320  # How far the crab walks left/right (half of the full range from 650 to 1290)
        self.enemy_start_x = 970  # Midpoint between 650 and 1290
        
        # Flag
        self.flag = pygame.Rect(930, 460, 50, 50)
        self.flag_color = (255, 255, 0)
        self.level_complete = False
        self.transitioning = False
        self.transition_alpha = 0

        # Platforms
        self.platforms = [
            pygame.Rect(0, WINDOW_HEIGHT - 55, WINDOW_WIDTH, 50), # Ground
            pygame.Rect(WINDOW_WIDTH - 30, 0, 50, WINDOW_HEIGHT), # Right wall
            pygame.Rect(510, 995, 110, 40), # done
            pygame.Rect(1325, 995, 110, 50), # done
            pygame.Rect(425, 450, 70, 70), # done
            pygame.Rect(425, 150, 70, 70), # done
            pygame.Rect(510, 150, 365, 350), # done 
            pygame.Rect(1780, 145, 80, 80), # done
            pygame.Rect(870, 242, 850, 105), # done
            pygame.Rect(510, 500, 1560, 290), # done
            pygame.Rect(0, 290, 30, 70), # done 
            pygame.Rect(0, 610, 30, 70), # done 
            pygame.Rect(0, 930, 30, 70), # done
            pygame.Rect(211, 41, 105, 10), # Moving platform
        ]

        # Moving platform properties
        self.moving_platform_index = 13
        self.moving_platform_speed = 3  
        self.moving_platform_direction = 1  

        self.frame = 0
        self.animation_speed = 10
        
        self.return_to_map_pos = False

    def update_moving_platform(self):
        platform = self.platforms[self.moving_platform_index]
        platform.y += self.moving_platform_speed * self.moving_platform_direction
        
        if self.moving_platform_index:
            self.display_surface.blit(self.moving_platform_img, platform)
        else:
            pygame.draw.rect(self.display_surface, (100, 100, 100), platform)
        
        if platform.y >= 950: 
            self.moving_platform_direction = -1
        elif platform.y <= 100:  
            self.moving_platform_direction = 1

        if self.player_rect.colliderect(platform) and self.velocity_y >= 2:
            self.player_rect.x += self.moving_platform_speed * self.moving_platform_direction
    
    def update_enemy(self):
        self.enemy.x += self.enemy_speed * self.enemy_direction
        if self.enemy.x > self.enemy_start_x + self.enemy_move_range:
            self.enemy_direction = -1
        elif self.enemy.x < self.enemy_start_x - self.enemy_move_range:
            self.enemy_direction = 1
        
        if self.enemy_direction == -1:
            self.current_crab_img = pygame.transform.flip(self.crab_img, True, False)
        else:
            self.current_crab_img = self.crab_img
    
    def animation_enemy(self):
        self.frame += 1
        if self.frame // self.animation_speed % 2 == 0:
            self.current_crab_img = self.crab_img
        else:
            self.current_crab_img = self.crab_img2
        self.display_surface.blit(self.current_crab_img, self.enemy)

    def check_enemy_collision(self):
        current_time = pygame.time.get_ticks()
        if (self.player_rect.colliderect(self.enemy) and 
            current_time - self.last_hit_time > self.hit_cooldown):
            self.hearts -= 1
            self.last_hit_time = current_time
            if self.player_rect.centerx > self.enemy.centerx:
                self.velocity_y = -15
            else:
                self.velocity_y = -15

    def draw_hearts(self):
        heart_spacing = 35
        for i in range(self.max_hearts):
            pos = (10 + i * heart_spacing, 10)
            if i < self.hearts:
                self.display_surface.blit(self.heart_img, pos)
            else:
                self.display_surface.blit(self.empty_heart_img, pos)
    
    def handle_flag_collision(self):
        if not self.transitioning and self.player_rect.colliderect(self.flag):
            self.transitioning = True
            self.transition_alpha = 0
            self.return_to_map_pos = True  # Set flag for special return position
    
    def update_transition(self):
        if self.transitioning:
            self.transition_alpha += 15
            if self.transition_alpha >= 255:
                if self.return_to_map_pos:
                    # Return to Level but signal we want special position
                    level = Level()
                    level.current_segment = 7  # Set segment directly
                    return level
                return Level()  # Normal transition
        return self
    def run(self):
        keys = pygame.key.get_pressed()
        
        # Handle flag collision first
        self.handle_flag_collision()
        
        if self.transitioning:
            return self.update_transition()
        
        # Game logic
        self.velocity_x = 0
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity_x = -5
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.velocity_x = 5

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        self.velocity_y += self.gravity
        self.player_rect.x += self.velocity_x
        self.player_rect.y += self.velocity_y

        self.update_moving_platform()
        self.update_enemy()
        self.check_enemy_collision()
        self.animation_enemy()

        # Collision detection with platforms
        self.on_ground = False
        for platform in self.platforms:
            if self.player_rect.colliderect(platform):
                if (self.velocity_y > 0 and 
                    self.player_rect.bottom > platform.top and 
                    self.player_rect.top < platform.top):
                    self.player_rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif (self.velocity_y < 0 and 
                      self.player_rect.top < platform.bottom and 
                      self.player_rect.bottom > platform.bottom):
                    self.player_rect.top = platform.bottom
                    self.velocity_y = 0
                elif (self.velocity_x > 0 and 
                      self.player_rect.right > platform.left and 
                      self.player_rect.left < platform.left):
                    self.player_rect.right = platform.left
                    self.velocity_y = 11
                elif (self.velocity_x < 0 and 
                      self.player_rect.left < platform.right and 
                      self.player_rect.right > platform.right):
                    self.player_rect.left = platform.right
                    self.velocity_y = 11

        # Screen boundaries
        if self.player_rect.left < -20:
            self.player_rect.left = -20
        if self.player_rect.right > WINDOW_WIDTH:
            self.player_rect.right = WINDOW_WIDTH
        if self.player_rect.top < 0:
            self.player_rect.top = 0
            self.velocity_y = 1
        
        # Animation handling
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.frame += 1.5
            if self.frame // self.animation_speed % 3 == 0:
                self.player = self.walking_left
            elif self.frame // self.animation_speed % 3 == 1:
                self.player = self.walking_left2
            else:
                self.player = self.walking_left3
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.frame += 1.5
            if self.frame // self.animation_speed % 3 == 0:
                self.player = self.walking_right
            elif self.frame // self.animation_speed % 3 == 1:
                self.player = self.walking_right2
            else:
                self.player = self.walking_right3
        pygame.display.update()

        # Drawing
        self.display_surface.blit(self.background, (0, 0))
        self.draw_hearts()
        self.display_surface.blit(self.player, self.player_rect.topleft)
        self.display_surface.blit(self.current_crab_img, self.enemy)
        self.update_moving_platform()
        pygame.mouse.set_visible(False)

        # Reset level when out of hearts
        if self.hearts <= 0:
            game_over_font = pygame.font.SysFont("Arial", 50)
            game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
            self.display_surface.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                                                     WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
            restart_font = pygame.font.SysFont("Arial", 30)
            restart_text = restart_font.render("Press R to restart level", True, (255, 255, 255))
            self.display_surface.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                                                    WINDOW_HEIGHT//2 - restart_text.get_height()//2 + 50))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.hearts = self.max_hearts
                        self.player_rect = pygame.Rect(100, 950, 30, 50)
                        return Level4()
                    
                    
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return None

        return self