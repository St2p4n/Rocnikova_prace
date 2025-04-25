from setting import *

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
        self.hit_cooldown = 1000  
        self.enemy_speed = 2
        self.enemy_direction = 1
        self.enemy_move_range = 320  # How far the crab walks left/right (half of the full range from 650 to 1290)
        self.enemy_start_x = 970  # Midpoint between 650 and 1290

        # Lasture enemy
        self.lasture_img = pygame.image.load("data/Aseprite/lasture_attack_opposite.png")  
        self.lasture_img2 = pygame.image.load("data/Aseprite/lasture_attack2_opposite.png")  
        self.lasture_img_left = pygame.image.load("data/Aseprite/lasture_attack.png")  
        self.lasture_img_left2 = pygame.image.load("data/Aseprite/lasture_attack2.png")  
        self.current_lasture_img4 = self.lasture_img
        self.current_lasture_img5 = self.lasture_img
        self.current_lasture_img6 = self.lasture_img_left
        self.current_lasture_img7 = self.lasture_img_left
        self.current_lasture_img8 = self.lasture_img_left
        self.perl = pygame.image.load("data/Aseprite/perl.png")
        
        # Enemy 4
        self.perl_active = False
        self.perl_rect = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed = 9
        self.perl_cooldown = 1000 # Time between shots in ms
        self.last_perl_shot = 0
        self.enemy4 = pygame.Rect(1820, 105, 50, 50)

        # Enemy 5
        self.perl2 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active2 = False
        self.perl_rect2 = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed2 = 9
        self.perl_cooldown2 = 1000 # Time between shots in ms
        self.last_perl_shot2 = 0
        self.enemy5 = pygame.Rect(465, 410, 50, 50)

        # Enemy 6
        self.perl3 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active3 = False
        self.perl_rect3 = pygame.Rect(0, 0, 25, 25) 
        self.perl_speed3 = 9
        self.perl_cooldown3 = 1000 # Time between shots in ms
        self.last_perl_shot3 = 0
        self.enemy6 = pygame.Rect(0, 255, 50, 50)

        # Enemy 7
        self.perl4 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active4 = False
        self.perl_rect4 = pygame.Rect(100, 0, 25, 25) 
        self.perl_speed4 = 9
        self.perl_cooldown4 = 1000 # Time between shots in ms
        self.last_perl_shot4 = 0
        self.enemy7 = pygame.Rect(0, 947, 50, 50)

        # Enemy 8
        self.perl5 = pygame.image.load("data/Aseprite/perl.png")
        self.perl_active5 = False
        self.perl_rect5 = pygame.Rect(100, 0, 25, 25) 
        self.perl_speed5 = 9
        self.perl_cooldown5 = 1000 # Time between shots in ms
        self.last_perl_shot5 = 0
        self.enemy8 = pygame.Rect(0, 575, 50, 50)
        
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
            pygame.Rect(510, 995, 110, 40), 
            pygame.Rect(1325, 995, 110, 50), 
            pygame.Rect(425, 450, 70, 70), 
            pygame.Rect(425, 150, 70, 70), 
            pygame.Rect(510, 150, 365, 350),  
            pygame.Rect(1810, 145, 50, 80), 
            pygame.Rect(870, 242, 850, 105), 
            pygame.Rect(510, 500, 1560, 290), 
            pygame.Rect(0, 290, 30, 70), 
            pygame.Rect(0, 610, 30, 70), 
            pygame.Rect(0, 942, 30, 70),
            pygame.Rect(0, 575, 25, 50),
            pygame.Rect(0, 255, 25, 50),
            pygame.Rect(465, 410, 50, 50),
            pygame.Rect(1820, 105, 50, 50),
            pygame.Rect(211, 41, 105, 10) # Moving platform
        ]

        # Moving platform properties
        self.moving_platform_index = 17
        self.moving_platform_speed = 2 
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
    
    def update_transition(self):
        if self.transitioning:
            self.transition_alpha += 15
            if self.transition_alpha >= 255:
                return "level_complete"  
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
            if self.perl_rect.right < 10:
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
            if self.perl_rect2.right < 0:
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
                self.perl_rect3.midright = (self.enemy6.midleft[0] + 30, self.enemy6.midleft[1])
                self.last_perl_shot3 = current_time

        if self.perl_active3:
            self.perl_rect3.x += self.perl_speed3
                
                # Check if pearl is off-screen
            if self.perl_rect3.left > 465:  
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
                self.perl_rect4.midright = (self.enemy7.midleft[0] + 30, self.enemy7.midleft[1])
                self.last_perl_shot4 = current_time

        if self.perl_active4:
            self.perl_rect4.x += self.perl_speed4
                
                # Check if pearl is off-screen
            if self.perl_rect4.left > 1830:  
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
                self.perl_rect5.midright = (self.enemy8.midleft[0] + 30, self.enemy8.midleft[1])
                self.last_perl_shot5 = current_time

        if self.perl_active5:
            self.perl_rect5.x += self.perl_speed5
                
                # Check if pearl is off-screen
            if self.perl_rect5.left > 465:  
                self.perl_active5 = False
                
                # Check collision with player
            if self.perl_rect5.colliderect(self.player_rect):
                    self.hearts -= 1
                    self.perl_active5 = False
                    if self.player_rect.centerx > self.enemy8.centerx:  
                        self.velocity_y = -15
                    else:
                        self.velocity_y = -15
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
            self.current_lasture_img6 = self.lasture_img_left2  
        else:
            self.current_lasture_img6 = self.lasture_img_left   
        
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
    
    def music_off(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
                pygame.mixer.music.set_volume(0)
                
    def music_on(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_n]:
                pygame.mixer.music.load("data/Songs/8-bit.mp3")
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)

    def run(self):
        keys = pygame.key.get_pressed()
        
        # Handle flag collision first
        self.handle_flag_collision()
        
        if self.transitioning:
            return self.update_transition()
        
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

        self.update_moving_platform()
        self.update_enemy()
        self.check_enemy_collision()
        self.animation_enemy()
        self.animation_lasture()
        self.music_off()
        self.music_on()

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
        if self.player_rect.right > WINDOW_WIDTH - 50:
            self.player_rect.right = WINDOW_WIDTH - 50
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
        self.update_moving_platform()
        pygame.mouse.set_visible(False)

        # How to play 
        instructions = pygame.font.SysFont("Math Bold", 25)
        instructions = instructions.render("Move: A/D | Jump: Space | Music: N to Play and M to Stop", True, (255, 255, 255))
        self.display_surface.blit(instructions, (WINDOW_WIDTH - instructions.get_width() - 25, 30))

        # Reset level when out of hearts
        if self.hearts <= 0:
            pygame.mixer.music.stop()
            pygame.image.load("data/Aseprite/death_pirate.png")
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
                        if pygame.mixer.music.get_volume() > 0:
                           pygame.mixer.music.load("data/Songs/8-bit.mp3")
                           pygame.mixer.music.set_volume(0.1)
                           pygame.mixer.music.play(-1)
                        self.hearts = self.max_hearts
                        self.player_rect = pygame.Rect(1705, 930, 30, 50)
                        return Level4()
                    
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return None

        return self