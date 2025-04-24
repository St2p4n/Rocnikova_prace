from setting import *

class Level3:
    def __init__(self):
        pygame.init()  
        self.display_surface = pygame.display.get_surface()
        self.player_rect = pygame.Rect(100, 100, 30, 50)
        self.player_color = (255, 0, 0)
        self.player = pygame.image.load("data/Aseprite/Pirate.png")
 
        self.walking_left = pygame.image.load("data/Aseprite/walking_left.png")
        self.walking_left2 = pygame.image.load("data/Aseprite/walking_left2.png")
        self.walking_left3 = pygame.image.load("data/Aseprite/walking_left3.png")

        self.walking_right = pygame.image.load("data/Aseprite/walking_right.png")
        self.walking_right2 = pygame.image.load("data/Aseprite/walking_right2.png")
        self.walking_right3 = pygame.image.load("data/Aseprite/walking_right3.png")

        self.background = pygame.image.load("data/Levels/Level3.png")
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))

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

        # Load crab enemy sprites
        self.crab_img = pygame.image.load("data/Aseprite/crab.png")
        self.crab_img2 = pygame.image.load("data/Aseprite/crab2.png")
        self.crab_img3 = pygame.image.load("data/Aseprite/crab2.png")

        # Crab Enemy 1 
        self.enemy = pygame.Rect(930, 964, 30, 50)
        self.current_crab_img = self.crab_img
        self.color = (255, 0, 0)
        self.last_hit_time = 0
        self.hit_cooldown = 1000  # 1 second cooldown in milliseconds
        self.enemy_speed = 2
        self.enemy_direction = 1
        self.enemy_move_range = 410
        self.enemy_start_x = 1330
        
        # Crab Enemy 2 
        self.enemy2 = pygame.Rect(285, 548, 30, 50) 
        self.current_crab2_img = self.crab_img
        self.last_hit_time2 = 0
        self.hit_cooldown = 1000  
        self.enemy2_speed = 2
        self.enemy2_direction = 1
        self.enemy2_move_range = 240
        self.enemy2_start_x = 545

        # Crab Enemy 3 
        self.enemy3 = pygame.Rect(515, 180, 30, 50)  
        self.current_crab3_img = self.crab_img
        self.last_hit_time3 = 0
        self.hit_cooldown = 1000  
        self.enemy3_speed = 2
        self.enemy3_direction = 1
        self.enemy3_move_range = 130
        self.enemy3_start_x = 680
        
        # Lasture enemy
        self.lasture_img = pygame.image.load("data/Aseprite/lasture_attack_opposite.png")  # Right-facing default
        self.lasture_img2 = pygame.image.load("data/Aseprite/lasture_attack2_opposite.png")  # Left-facing attack
        self.lasture_img_left = pygame.image.load("data/Aseprite/lasture_attack.png")  # Left-facing default
        self.lasture_img_left2 = pygame.image.load("data/Aseprite/lasture_attack2.png")  # Left-facing attack
        self.current_lasture_img4 = self.lasture_img
        self.current_lasture_img5 = self.lasture_img
        self.current_lasture_img6 = self.lasture_img
        self.current_lasture_img7 = self.lasture_img_left
        self.current_lasture_img8 = self.lasture_img_left
       
        # Enemy 4
        self.perl = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active = False
        self.perl_rect = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed = 9
        self.perl_cooldown = 1000 # Time between shots in ms
        self.last_perl_shot = 0
        self.enemy4 = pygame.Rect(1840, 155, 50, 50)

        # Enemy 5
        self.perl2 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active2 = False
        self.perl_rect2 = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed2 = 9
        self.perl_cooldown2 = 1000 # Time between shots in ms
        self.last_perl_shot2 = 0
        self.enemy5 = pygame.Rect(1840, 525, 50, 50)

        # Enemy 6
        self.perl3 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active3 = False
        self.perl_rect3 = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed3 = 9
        self.perl_cooldown3 = 1000 # Time between shots in ms
        self.last_perl_shot3 = 0
        self.enemy6 = pygame.Rect(1840, 905, 50, 50)

        # Enemy 7
        self.perl4 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active4 = False
        self.perl_rect4 = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed4 = 9
        self.perl_cooldown4 = 1000 # Time between shots in ms
        self.last_perl_shot4 = 0
        self.enemy7 = pygame.Rect(0, 925, 50, 50)

        # Enemy 8
        self.perl5 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active5 = False
        self.perl_rect5 = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed5 = 9
        self.perl_cooldown5 = 1000 # Time between shots in ms
        self.last_perl_shot5 = 0
        self.enemy8 = pygame.Rect(0, 525, 50, 50)
        
        # Flag
        self.flag = pygame.Rect(1755, 950, 50, 50)
        self.flag_color = (255, 255, 0)
        self.level_complete = False
        self.transitioning = False
        self.transition_alpha = 0
        
        # Platforms
        self.platforms = [
            pygame.Rect(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 70), # Ground
            pygame.Rect(WINDOW_WIDTH - 30, 0, 50, WINDOW_HEIGHT), # Right wall
            pygame.Rect(0, 570, 130, 200), 
            pygame.Rect(460, 130, 70, 50),
            pygame.Rect(840, 145, 70, 5),
            pygame.Rect(300, 565, 495, 200),
            pygame.Rect(700, 765, 1000, 10),
            pygame.Rect(1680, 195, 210, 170), 
            pygame.Rect(0, 195, 1530, 170), 
            pygame.Rect(930, 565, 1000, 180), 
            pygame.Rect(1080, 515, 110, 50), 
            pygame.Rect(800, 945, 80, 50), 
        ]

        self.spikes = [
            pygame.Rect(800, 600, 10, 150),
            pygame.Rect(150, 600, 10, 160),
            pygame.Rect(270, 600, 10, 160),
            pygame.Rect(920, 600, 10, 150),
            pygame.Rect(800, 700, 150, 10)
        ]

        self.frame = 0
        self.animation_speed = 10

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

        # Animate Crab 3
        if self.frame // self.animation_speed % 2 == 0:
            self.current_crab3_img = self.crab_img
        else:
            self.current_crab3_img = self.crab_img2
        self.display_surface.blit(self.current_crab3_img, self.enemy3)
    
    def animation_lasture(self):
        current_time = pygame.time.get_ticks()

        # Lasture 1 (enemy4)
        if self.perl_active and current_time - self.last_perl_shot < 200:
            self.current_lasture_img4 = self.lasture_img2
        else:
            self.current_lasture_img4 = self.lasture_img
        
        # Lasture 2 (enemy5)
        if self.perl_active2 and current_time - self.last_perl_shot2 < 200:
            self.current_lasture_img5 = self.lasture_img2
        else:
            self.current_lasture_img5 = self.lasture_img
        
        # Lasture 3 (enemy6)
        if self.perl_active3 and current_time - self.last_perl_shot3 < 200:
            self.current_lasture_img6 = self.lasture_img2
        else:
            self.current_lasture_img6 = self.lasture_img
        
        # Lasture 4 (enemy7)
        if self.perl_active4 and current_time - self.last_perl_shot4 < 200:
            self.current_lasture_img7 = self.lasture_img_left2
        else:
            self.current_lasture_img7 = self.lasture_img_left
        
        # Lasture 5 (enemy8) 
        if self.perl_active5 and current_time - self.last_perl_shot5 < 200:
            self.current_lasture_img8 = self.lasture_img_left2
        else:
            self.current_lasture_img8 = self.lasture_img_left

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
    
    def update_transition(self):
        if self.transitioning:
            self.transition_alpha += 15
            if self.transition_alpha >= 255:
                return "level_complete"  # Signal that level is complete
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
            if self.perl_rect.right < 950:
                self.perl_active = False
            # Optional: Check collision with player
            if self.perl_rect.colliderect(self.player_rect):
                self.hearts -= 1
                self.perl_active = False
                if self.player_rect.centerx > self.enemy.centerx:
                    self.velocity_y = -15
                else:
                    self.velocity_y = -15
        # Shoot new pearl if cooldown is over (for enemy5)
        if not self.perl_active2 and current_time - self.last_perl_shot2 > self.perl_cooldown2:
            self.perl_active2 = True
            self.perl_rect2.midright = self.enemy5.midleft
            self.last_perl_shot2 = current_time

        if self.perl_active2:
            self.perl_rect2.x -= self.perl_speed2

            # Check if pearl is off-screen
            if self.perl_rect2.right < 1220:
                self.perl_active2 = False

            # Check collision with player
            if self.perl_rect2.colliderect(self.player_rect):
                self.hearts -= 1
                self.perl_active2 = False
                if self.player_rect.centerx > self.enemy5.centerx:
                    self.velocity_y = -15
                else:
                    self.velocity_y = -15
        # Shoot new pearl if cooldown is over (for enemy 6)
        if not self.perl_active3 and current_time - self.last_perl_shot3 > self.perl_cooldown3:
                self.perl_active3 = True
                self.perl_rect3.midright = self.enemy6.midleft
                self.last_perl_shot3 = current_time

        if self.perl_active3:
            self.perl_rect3.x -= self.perl_speed3
                
                # Check if pearl is off-screen
            if self.perl_rect3.right < 0:  
                self.perl_active3 = False
                
                # Check collision with player
            if self.perl_rect3.colliderect(self.player_rect):
                    self.hearts -= 1
                    self.perl_active3 = False
                    if self.player_rect.centerx > self.enemy6.centerx: 
                        self.velocity_y = -15
                    else:
                        self.velocity_y = -15

        # Shoot new pearl if cooldown is over (for enemy 7)
        if not self.perl_active4 and current_time - self.last_perl_shot4 > self.perl_cooldown4:
                self.perl_active4 = True
                self.perl_rect4.midright = self.enemy7.midleft
                self.last_perl_shot4 = current_time

        if self.perl_active4:
            self.perl_rect4.x += self.perl_speed4
                
                # Check if pearl is off-screen
            if self.perl_rect4.left > 750:  
                self.perl_active4 = False
                
                # Check collision with player
            if self.perl_rect4.colliderect(self.player_rect):
                    self.hearts -= 1
                    self.perl_active4 = False
                    if self.player_rect.centerx > self.enemy7.centerx:  
                        self.velocity_y = -15
                    else:
                        self.velocity_y = -15
        # Shoot new pearl if cooldown is over (for enemy 8)
        if not self.perl_active5 and current_time - self.last_perl_shot5 > self.perl_cooldown5:
                self.perl_active5 = True
                self.perl_rect5.midright = self.enemy8.midleft
                self.last_perl_shot5 = current_time

        if self.perl_active5:
            self.perl_rect5.x += self.perl_speed5
                
                # Check if pearl is off-screen
            if self.perl_rect5.left > 1050:  
                self.perl_active5 = False
                
                # Check collision with player
            if self.perl_rect5.colliderect(self.player_rect):
                    self.hearts -= 1
                    self.perl_active5 = False
                    if self.player_rect.centerx > self.enemy8.centerx:  
                        self.velocity_y = -15
                    else:
                        self.velocity_y = -15

    def spike_collisions(self):
        for spike in self.spikes:
            if self.player_rect.colliderect(spike):
                self.hearts -= 3

    def run(self):
        keys = pygame.key.get_pressed()
        
        # Handle flag collision first
        self.handle_flag_collision()
        
        if self.transitioning:
            if self.transitioning:
                self.transition_alpha += 15
            if self.transition_alpha >= 255:
                return "level_complete"  
            return self
        
        # Game logic
        self.velocity_x = 0
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity_x = -4
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.velocity_x = 4

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        self.velocity_y += self.gravity
        self.player_rect.x += self.velocity_x
        self.player_rect.y += self.velocity_y

        self.update_enemy()
        self.check_enemy_collisions()
        self.animation_enemies()
        self.spike_collisions()
        self.animation_lasture()

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
        if self.player_rect.left < -10:
            self.player_rect.left = -10
        if self.player_rect.right > WINDOW_WIDTH:
            self.player_rect.right = WINDOW_WIDTH
        if self.player_rect.top < -20:
            self.player_rect.top = -20
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

        # Drawing
        self.display_surface.blit(self.background, (0, 0))
        self.draw_hearts()
        self.display_surface.blit(self.player, self.player_rect.topleft)
        self.animation_enemies()
        self.display_surface.blit(self.current_lasture_img4, self.enemy4)
        self.display_surface.blit(self.current_lasture_img5, self.enemy5)
        self.display_surface.blit(self.current_lasture_img6, self.enemy6)
        self.display_surface.blit(self.current_lasture_img7, self.enemy7)
        self.display_surface.blit(self.current_lasture_img8, self.enemy8)
        self.display_surface.blit(self.perl, self.perl_rect)
        self.display_surface.blit(self.perl2, self.perl_rect2)
        self.display_surface.blit(self.perl3, self.perl_rect3)
        self.display_surface.blit(self.perl4, self.perl_rect4)
        self.display_surface.blit(self.perl5, self.perl_rect5)
        self.update_perl()
        pygame.mouse.set_visible(False)
        pygame.display.update()

        # Reset level when out of hearts
        if self.hearts <= 0:
            game_over_font = pygame.font.SysFont("Arial", 60)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            self.display_surface.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                                                     WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
            restart_font = pygame.font.SysFont("Arial", 50)
            restart_text = restart_font.render("Press R to restart level", True, (255, 255, 255))
            self.display_surface.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                                                    WINDOW_HEIGHT//2 - restart_text.get_height()//2 + 70))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.hearts = self.max_hearts
                        self.player_rect = pygame.Rect(100, 100, 30, 50)
                        return Level3()
                    
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return None

        return self