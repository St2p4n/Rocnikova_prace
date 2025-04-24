from setting import *
<<<<<<< HEAD
=======
from level import Level
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6

class Level1:
    def __init__(self):
        pygame.init()  
        self.display_surface = pygame.display.get_surface()
        self.player_rect = pygame.Rect(100, 600, 30, 50)
        self.player_color = (255, 0, 0)
        self.player = pygame.image.load("data/Aseprite/Pirate.png")
 
        self.walking_left = pygame.image.load("data/Aseprite/walking_left.png")
        self.walking_left2 = pygame.image.load("data/Aseprite/walking_left2.png")
        self.walking_left3 = pygame.image.load("data/Aseprite/walking_left3.png")

        self.walking_right = pygame.image.load("data/Aseprite/walking_right.png")
        self.walking_right2 = pygame.image.load("data/Aseprite/walking_right2.png")
        self.walking_right3 = pygame.image.load("data/Aseprite/walking_right3.png")

        self.background = pygame.image.load("data/Levels/Level1.3.png")
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
<<<<<<< HEAD
=======
        # Load pirate attack sprites
        self.attack_img_left = pygame.image.load("data/Aseprite/Pirate_attack2.png")
        self.attack_img_right = pygame.image.load("data/Aseprite/Pirate_attack_right.png")
        
        # Attack attributes
        self.attacking = False
        self.attack_cooldown = 500  # milliseconds
        self.last_attack_time = 0
        
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
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
        
        # Moving platform image
        self.moving_platform_img = pygame.image.load("data/Aseprite/moving_platform.png")
        self.moving_platform_img = pygame.transform.scale(self.moving_platform_img, (140, 70))

        # Crab enemy
        self.crab_img = pygame.image.load("data/Aseprite/crab.png")
        self.crab_img2 = pygame.image.load("data/Aseprite/crab2.png")
        self.current_crab_img = self.crab_img

        # Enemy 
        self.enemy = pygame.Rect(580, 750, 30, 60)
        self.color = (255, 0, 0)
        self.last_hit_time = 0
        self.hit_cooldown = 1000  # 1 second cooldown in milliseconds
        self.enemy_speed = 2
        self.enemy_direction = 1
        self.enemy_move_range = 90  # How far the crab walks left/right
        self.enemy_start_x = 470  # Starting X position
        
        # Lasture enemy
        self.lasture_img = pygame.image.load("data/Aseprite/lasture_attack_opposite.png")
<<<<<<< HEAD
        self.lasture_img2 = pygame.image.load("data/Aseprite/lasture_attack2_opposite.png")
=======
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.perl = pygame.image.load("data/Aseprite/perl.png")
        # Enemy 2
        self.perl_active = False
        self.perl_rect = pygame.Rect(0, 0, 20, 20) 
<<<<<<< HEAD
        self.perl_speed = 6
=======
        self.perl_speed = 9
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.perl_cooldown = 1000 # Time between shots in ms
        self.last_perl_shot = 0
        self.enemy2 = pygame.Rect(1350, 355, 50, 50)
        self.color = (255, 0, 0)
        
        # Flag
        self.flag = pygame.Rect(1830, 550, 50, 50)
        self.flag_color = (0, 255, 0)
        self.level_complete = False
        self.transitioning = False
        self.transition_alpha = 0

        # Platforms
        self.platforms = [
            pygame.Rect(0, WINDOW_HEIGHT - 30, WINDOW_WIDTH, 50), # Ground
            pygame.Rect(50, 680, 250, 30),
            pygame.Rect(380, 774, 200, 250),
            pygame.Rect(340, 526, 110, 80),
            pygame.Rect(540, 426, 200, 100),
            pygame.Rect(870, 400, 200, 100),
            pygame.Rect(1200, 400, 200, 100),
            pygame.Rect(1370, 650, 200, 100),
            pygame.Rect(1670, 580, 220, 100),
            pygame.Rect(670, 720, 105, 10),
        ]

        # Moving platform properties
        self.moving_platform_index = 9  
<<<<<<< HEAD
        self.moving_platform_speed = 1.5
=======
        self.moving_platform_speed = 2  
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.moving_platform_direction = 1  

        self.frame = 0
        self.animation_speed = 10

    def update_moving_platform(self):
        platform = self.platforms[self.moving_platform_index]
        platform.x += self.moving_platform_speed * self.moving_platform_direction
        
        if self.moving_platform_index:
            self.display_surface.blit(self.moving_platform_img, platform)
        else:
            pygame.draw.rect(self.display_surface, (100, 100, 100), platform)
        
        if platform.x >= 1200: 
<<<<<<< HEAD
            self.moving_platform_direction = -1.5
=======
            self.moving_platform_direction = -1
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        elif platform.x <= 680:  
            self.moving_platform_direction = 1

        if self.player_rect.colliderect(platform) and self.velocity_y >= 0:
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
<<<<<<< HEAD

    def animation_lasture(self):
        current_time = pygame.time.get_ticks()
        # When shooting, show attack image for (200ms)
        if self.perl_active and current_time - self.last_perl_shot < 200:
            self.current_lasture_img = self.lasture_img2
        else:
            self.current_lasture_img = self.lasture_img
     
    def update_perl(self):
        current_time = pygame.time.get_ticks()
        
        # Shoot new pearl if cooldown is over
        if not self.perl_active and current_time - self.last_perl_shot > self.perl_cooldown:
            self.perl_active = True
            self.perl_rect.midright = self.enemy2.midleft
            self.last_perl_shot = current_time
        
        if self.perl_active:
            self.perl_rect.x -= self.perl_speed
            
            # Check if pearl is off-screen
            if self.perl_rect.right < 400:
                self.perl_active = False
            
            # Optional: Check collision with player
            if self.perl_rect.colliderect(self.player_rect):
                self.hearts -= 1
                self.perl_active = False
                if self.player_rect.centerx > self.enemy.centerx:
                    self.velocity_y = -15
                else:
                    self.velocity_y = -15

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

=======
        
    def update_perl(self):
        current_time = pygame.time.get_ticks()
        
        # Shoot new pearl if cooldown is over
        if not self.perl_active and current_time - self.last_perl_shot > self.perl_cooldown:
            self.perl_active = True
            self.perl_rect.midright = self.enemy2.midleft
            self.last_perl_shot = current_time
        
        if self.perl_active:
            self.perl_rect.x -= self.perl_speed
            
            # Check if pearl is off-screen
            if self.perl_rect.right < 400:
                self.perl_active = False
            
            # Optional: Check collision with player
            if self.perl_rect.colliderect(self.player_rect):
                self.hearts -= 1
                self.perl_active = False
                if self.player_rect.centerx > self.enemy.centerx:
                    self.velocity_y = -15
                else:
                    self.velocity_y = -15
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

>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
    def draw_hearts(self):
        heart_spacing = 35
        for i in range(self.max_hearts):
            pos = (10 + i * heart_spacing, 10)
            if i < self.hearts:
                self.display_surface.blit(self.heart_img, pos)
            else:
                self.display_surface.blit(self.empty_heart_img, pos)
    # Flag collision
    def handle_flag_collision(self):
        if not self.transitioning and self.player_rect.colliderect(self.flag):
            self.transitioning = True
            self.transition_alpha = 0
    
    def update_transition(self):
        if self.transitioning:
            self.transition_alpha += 15
            if self.transition_alpha >= 255:
<<<<<<< HEAD
                return "level_complete"
=======
                return Level()  # Transition complete, return new level
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        return self
    
    def run(self):
        keys = pygame.key.get_pressed()
        
        # Flag collision 
        self.handle_flag_collision()
        
<<<<<<< HEAD
        if self.transitioning:
            return self.update_transition()
        
        self.velocity_x = 0
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity_x = -4
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.velocity_x = 4
=======
        # If transitioning, skip normal game logic
        if self.transitioning:
            return self.update_transition()
        
        # Normal game logic
        self.velocity_x = 0
        if keys[pygame.K_a] and not keys[pygame.K_d]:
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
        self.check_enemy_collision()
        self.animation_enemy()
        self.update_perl()
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
        
        # Check if player hits the deadly platform
        killing_platform = pygame.Rect(0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50)
        if self.player_rect.colliderect(killing_platform):
            self.hearts -= 1 
            self.player_rect.topleft = (100, 600)

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
<<<<<<< HEAD
        self.display_surface.blit(self.current_lasture_img, self.enemy2)
=======
        self.display_surface.blit(self.lasture_img, self.enemy2)
>>>>>>> ec4858a9a66ad9964f3c91a5bbe78b27c7932fc6
        self.display_surface.blit(self.perl, self.perl_rect)
        self.update_moving_platform()
        pygame.mouse.set_visible(False)

        # Reset level when out of hearts
        if self.hearts <= 0:
            pygame.image.load("data/Aseprite/death_pirate.png")
<<<<<<< HEAD
            game_over_font = pygame.font.SysFont("Arial", 70)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            self.display_surface.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                                                     WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
            restart_font = pygame.font.SysFont("Arial", 50)
            restart_text = restart_font.render("Press R to restart level", True, (255, 255, 255))
            self.display_surface.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                                                    WINDOW_HEIGHT//2 - restart_text.get_height()//2 + 80))
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
                        self.player_rect = pygame.Rect(100, 590, 30, 50)
                        return Level1()
                    
                    
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return None

        return self