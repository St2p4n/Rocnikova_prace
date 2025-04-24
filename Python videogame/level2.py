from setting import *
<<<<<<< HEAD

=======
from level import Level
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6

class Level2:
    def __init__(self):
        pygame.init()  
        self.display_surface = pygame.display.get_surface()
        self.player_rect = pygame.Rect(100, 950, 30, 50)
        self.player_color = (255, 0, 0)
        self.player = pygame.image.load("data/Aseprite/Pirate.png")
 
        self.walking_left = pygame.image.load("data/Aseprite/walking_left.png")
        self.walking_left2 = pygame.image.load("data/Aseprite/walking_left2.png")
        self.walking_left3 = pygame.image.load("data/Aseprite/walking_left3.png")

        self.walking_right = pygame.image.load("data/Aseprite/walking_right.png")
        self.walking_right2 = pygame.image.load("data/Aseprite/walking_right2.png")
        self.walking_right3 = pygame.image.load("data/Aseprite/walking_right3.png")

        self.background = pygame.image.load("data/Levels/Level2.png")
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
<<<<<<< HEAD
        self.crab_img3 = pygame.image.load("data/Aseprite/crab2.png")
=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6

        # Crab Enemy 1 
        self.enemy = pygame.Rect(950, 1008, 30, 50)
        self.current_crab_img = self.crab_img
        self.color = (255, 0, 0)
        self.last_hit_time = 0
        self.hit_cooldown = 1000  # 1 second cooldown in milliseconds
<<<<<<< HEAD
        self.enemy_speed = 2
=======
        self.enemy_speed = 3
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.enemy_direction = 1
        self.enemy_move_range = 150
        self.enemy_start_x = 850
        
        # Crab Enemy 2 
<<<<<<< HEAD
        self.enemy2 = pygame.Rect(285, 418, 30, 50) 
        self.current_crab2_img = self.crab_img
        self.last_hit_time2 = 0
        self.hit_cooldown = 1000  
        self.enemy2_speed = 2
        self.enemy2_direction = 1
        self.enemy2_move_range = 120
        self.enemy2_start_x = 385

        # Crab Enemy 3 
        self.enemy3 = pygame.Rect(1515, 130, 30, 50)  
        self.current_crab3_img = self.crab_img
        self.last_hit_time3 = 0
        self.hit_cooldown = 1000  
        self.enemy3_speed = 2
        self.enemy3_direction = 1
        self.enemy3_move_range = 90
        self.enemy3_start_x = 1520
        
        # Lasture enemy
        self.lasture_img = pygame.image.load("data/Aseprite/lasture_attack_opposite.png")
        self.lasture_img2 = pygame.image.load("data/Aseprite/lasture_attack2_opposite.png")
        self.perl = pygame.image.load("data/Aseprite/perl.png")
        # Enemy 4
        self.perl_active = False
        self.perl_rect = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed = 7
=======
        self.enemy2 = pygame.Rect(285, 418, 30, 50)  # Different position
        self.current_crab2_img = self.crab_img
        self.last_hit_time2 = 0
        self.hit_cooldown = 1000  
        self.enemy2_speed = 3
        self.enemy2_direction = 1
        self.enemy2_move_range = 120
        self.enemy2_start_x = 385
        
        # Lasture enemy
        self.lasture_img = pygame.image.load("data/Aseprite/lasture_attack_opposite.png")
        self.perl = pygame.image.load("data/Aseprite/perl.png")
        # Enemy 2
        self.perl_active = False
        self.perl_rect = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed = 9
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.perl_cooldown = 1000 # Time between shots in ms
        self.last_perl_shot = 0
        self.enemy4 = pygame.Rect(1590, 680, 50, 50)
        self.color = (255, 0, 0)
        
        # Flag
        self.flag = pygame.Rect(1580, 130, 50, 50)
        self.flag_color = (255, 255, 0)
        self.level_complete = False
        self.transitioning = False
        self.transition_alpha = 0

        # Platforms
        self.platforms = [
            pygame.Rect(0, WINDOW_HEIGHT - 55, WINDOW_WIDTH, 50), # Ground
            pygame.Rect(WINDOW_WIDTH - 50, 0, 50, WINDOW_HEIGHT), # Right wall
            pygame.Rect(610, 965, 80, 40),
            pygame.Rect(1130, 870, 100, 180),
            pygame.Rect(1035, 950, 100, 50), 
            pygame.Rect(265, 440, 260, 180),
            pygame.Rect(640, 520, 235, 150),
            pygame.Rect(1270, 225, 80, 50), 
            pygame.Rect(1420, 150, 210, 100), 
            pygame.Rect(1270, 725, 360, 100), 
            pygame.Rect(1015, 610, 90, 140), 
            pygame.Rect(1110, 675, 55, 75), 
            pygame.Rect(670, 341, 105, 10), # Moving platform
        ]

        # Moving platform properties
        self.moving_platform_index = 12
<<<<<<< HEAD
        self.moving_platform_speed = 1.5
=======
        self.moving_platform_speed = 2  
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.moving_platform_direction = 1  

        self.frame = 0
        self.animation_speed = 10
        
        self.return_to_map_pos = False

    def update_moving_platform(self):
        platform = self.platforms[self.moving_platform_index]
        platform.x += self.moving_platform_speed * self.moving_platform_direction
        
        if self.moving_platform_index:
            self.display_surface.blit(self.moving_platform_img, platform)
        else:
            pygame.draw.rect(self.display_surface, (100, 100, 100), platform)
        
        if platform.x >= 1090: 
<<<<<<< HEAD
            self.moving_platform_direction = -1.5
=======
            self.moving_platform_direction = -1
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        elif platform.x <= 600:  
            self.moving_platform_direction = 1

        if self.player_rect.colliderect(platform) and self.velocity_y >= 0:
            self.player_rect.x += self.moving_platform_speed * self.moving_platform_direction
    
    def update_enemy(self):
        # Update Crab 1
        self.enemy.x += self.enemy_speed * self.enemy_direction
        if self.enemy.x > self.enemy_start_x + self.enemy_move_range:
            self.enemy_direction = -1
        elif self.enemy.x < self.enemy_start_x - self.enemy_move_range:
            self.enemy_direction = 1
        
        if self.enemy_direction == -1:
            self.current_crab_img = pygame.transform.flip(self.crab_img, True, False)
        else:
            self.current_crab_img = self.crab_img
            
        # Update Crab 2
        self.enemy2.x += self.enemy2_speed * self.enemy2_direction
        if self.enemy2.x > self.enemy2_start_x + self.enemy2_move_range:
            self.enemy2_direction = -1
        elif self.enemy2.x < self.enemy2_start_x - self.enemy2_move_range:
            self.enemy2_direction = 1
        
        if self.enemy2_direction == -1:
            self.current_crab2_img = pygame.transform.flip(self.crab_img, True, False)
        else:
            self.current_crab2_img = self.crab_img
<<<<<<< HEAD
        
        # Update Crab 3
        self.enemy3.x += self.enemy3_speed * self.enemy3_direction
        if self.enemy3.x > self.enemy3_start_x + self.enemy3_move_range:
            self.enemy3_direction = -1
        elif self.enemy3.x < self.enemy3_start_x - self.enemy3_move_range:
            self.enemy3_direction = 1
        
        if self.enemy3_direction == -1:
            self.current_crab3_img = pygame.transform.flip(self.crab_img, True, False)
        else:
            self.current_crab3_img = self.crab_img
=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6

    def animation_enemies(self):
        self.frame += 1
        # Animate Crab 1
        if self.frame // self.animation_speed % 2 == 0:
            self.current_crab_img = self.crab_img
        else:
            self.current_crab_img = self.crab_img2
        self.display_surface.blit(self.current_crab_img, self.enemy)
        
        # Animate Crab 2
        if self.frame // self.animation_speed % 2 == 0:
            self.current_crab2_img = self.crab_img
        else:
            self.current_crab2_img = self.crab_img2
        self.display_surface.blit(self.current_crab2_img, self.enemy2)

<<<<<<< HEAD
        # Animate Crab 3
        if self.frame // self.animation_speed % 2 == 0:
            self.current_crab3_img = self.crab_img
        else:
            self.current_crab3_img = self.crab_img2
        self.display_surface.blit(self.current_crab3_img, self.enemy3)
    
    def animation_lasture(self):
        current_time = pygame.time.get_ticks()
        if self.perl_active and current_time - self.last_perl_shot < 200:
            self.current_lasture_img = self.lasture_img2
        else:
            self.current_lasture_img = self.lasture_img

=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
    def check_enemy_collisions(self):
        current_time = pygame.time.get_ticks()
        # Check Crab 1 collision
        if (self.player_rect.colliderect(self.enemy) and 
            current_time - self.last_hit_time > self.hit_cooldown):
            self.hearts -= 1
            self.last_hit_time = current_time
            if self.player_rect.centerx > self.enemy.centerx:
                self.velocity_y = -15
            else:
                self.velocity_y = -15
                
        # Check Crab 2 collision
        if (self.player_rect.colliderect(self.enemy2) and 
            current_time - self.last_hit_time2 > self.hit_cooldown):
            self.hearts -= 1
            self.last_hit_time2 = current_time
<<<<<<< HEAD
            if self.player_rect.centerx > self.enemy3.centerx:
                self.velocity_y = -15
            else:
                self.velocity_y = -15

          # Check Crab 3 collision
        if (self.player_rect.colliderect(self.enemy3) and 
            current_time - self.last_hit_time3 > self.hit_cooldown):
            self.hearts -= 1
            self.last_hit_time3 = current_time
            if self.player_rect.centerx > self.enemy3.centerx:
=======
            if self.player_rect.centerx > self.enemy2.centerx:
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
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
<<<<<<< HEAD
                return "level_complete"
=======
                if self.return_to_map_pos:
                    # Return to Level but signal we want special position
                    level = Level()
                    level.current_segment = 2  # Set segment directly
                    return level
                return Level()  # Normal transition
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        return self
    
    def update_perl(self):
        current_time = pygame.time.get_ticks()
        
        # Shoot new pearl if cooldown is over
        if not self.perl_active and current_time - self.last_perl_shot > self.perl_cooldown:
            self.perl_active = True
            self.perl_rect.midright = self.enemy4.midleft
            self.last_perl_shot = current_time
        
        if self.perl_active:
            self.perl_rect.x -= self.perl_speed
            
            # Check if pearl is off-screen
            if self.perl_rect.right < 1200:
                self.perl_active = False
            
            # Optional: Check collision with player
            if self.perl_rect.colliderect(self.player_rect):
                self.hearts -= 1
                self.perl_active = False
                if self.player_rect.centerx > self.enemy.centerx:
                    self.velocity_y = -15
                else:
                    self.velocity_y = -15
        
    def run(self):
        keys = pygame.key.get_pressed()
        
        # Handle flag collision first
        self.handle_flag_collision()
        
        if self.transitioning:
            return self.update_transition()
        
        # Game logic
        self.velocity_x = 0
        if keys[pygame.K_a] and not keys[pygame.K_d]:
<<<<<<< HEAD
            self.velocity_x = -4
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.velocity_x = 4
=======
            self.velocity_x = -5
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.velocity_x = 5
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        self.velocity_y += self.gravity
        self.player_rect.x += self.velocity_x
        self.player_rect.y += self.velocity_y

        self.update_moving_platform()
        self.update_enemy()
        self.check_enemy_collisions()
        self.animation_enemies()
<<<<<<< HEAD
        self.animation_lasture()
=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6

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
        if self.player_rect.left < 0:
            self.player_rect.left = 0
        if self.player_rect.right > WINDOW_WIDTH:
            self.player_rect.right = WINDOW_WIDTH
        if self.player_rect.top < 0:
            self.player_rect.top = 0
            self.velocity_y = 1
<<<<<<< HEAD

            
=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        
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
        self.animation_enemies()
        self.update_moving_platform()
<<<<<<< HEAD
        self.display_surface.blit(self.current_lasture_img, self.enemy4)
=======
        self.display_surface.blit(self.lasture_img, self.enemy4)
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.display_surface.blit(self.perl, self.perl_rect)
        self.update_perl()
        pygame.mouse.set_visible(False)

        # Reset level when out of hearts
        if self.hearts <= 0:
<<<<<<< HEAD
            game_over_font = pygame.font.SysFont("Arial", 60)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            self.display_surface.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                                                     WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
            restart_font = pygame.font.SysFont("Arial", 50)
            restart_text = restart_font.render("Press R to restart level", True, (255, 255, 255))
            self.display_surface.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                                                    WINDOW_HEIGHT//2 - restart_text.get_height()//2 + 70))
=======
            game_over_font = pygame.font.SysFont("Arial", 50)
            game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
            self.display_surface.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                                                     WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
            restart_font = pygame.font.SysFont("Arial", 30)
            restart_text = restart_font.render("Press R to restart level", True, (255, 255, 255))
            self.display_surface.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                                                    WINDOW_HEIGHT//2 - restart_text.get_height()//2 + 50))
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.hearts = self.max_hearts
                        self.player_rect = pygame.Rect(100, 950, 30, 50)
                        return Level2()
                    
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return None

        return self