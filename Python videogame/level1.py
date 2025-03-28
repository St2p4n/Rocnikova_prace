from setting import *
from level import Level
class Level1:
    def __init__(self):
        pygame.init()  
        self.player_rect = pygame.Rect(100, 600, 50, 50)
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
        self.current_crab_img = self.crab_img

        # Enemy 
        self.enemy = pygame.Rect(500, 750, 50, 80)
        self.color = (255, 0, 0)
        self.last_hit_time = 0
        self.hit_cooldown = 1000  # 1 second cooldown in milliseconds
        self.enemy_speed = 2
        self.enemy_direction = 1
        self.enemy_move_range = 300  # How far the crab walks left/right
        self.enemy_start_x = 500  # Starting X position
        
        # Flag
        self.flag = pygame.Rect(1850, 550, 50, 50)
        self.flag_color = (0, 255, 0)
        self.level_complete = False

        # Platforms
        self.platforms = [
            pygame.Rect(0, WINDOW_HEIGHT - 30, WINDOW_WIDTH, 50), # Ground
            pygame.Rect(70, 680, 230, 30),
            pygame.Rect(400, 774, 180, 250),
            pygame.Rect(360, 526, 90, 80),
            pygame.Rect(560, 426, 180, 100),
            pygame.Rect(890, 400, 180, 100),
            pygame.Rect(1220, 420, 180, 100),
            pygame.Rect(1390, 650, 180, 100),
            pygame.Rect(1690, 580, 200, 100),
            pygame.Rect(690, 720, 85, 10),
        ]

        # Moving platform properties
        self.moving_platform_index = 9  
        self.moving_platform_speed = 2  
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
            self.moving_platform_direction = -1
        elif platform.x <= 680:  
            self.moving_platform_direction = 1

        if self.player_rect.colliderect(platform) and self.velocity_y >= 0:
            self.player_rect.x += self.moving_platform_speed * self.moving_platform_direction
    
    def update_enemy(self):
        # Move crab enemy left to right within its range
        self.enemy.x += self.enemy_speed * self.enemy_direction
        
        # Reverse direction at boundaries
        if self.enemy.x > self.enemy_start_x + self.enemy_move_range:
            self.enemy_direction = -1
        elif self.enemy.x < self.enemy_start_x - self.enemy_move_range:
            self.enemy_direction = 1
        
        # Flip crab image based on direction
        if self.enemy_direction == -1:
            self.current_crab_img = pygame.transform.flip(self.crab_img1, True, False)
        else:
            self.current_crab_img = self.crab_img1

    def check_enemy_collision(self):
        current_time = pygame.time.get_ticks()
        if (self.player_rect.colliderect(self.enemy) and 
            current_time - self.last_hit_time > self.hit_cooldown):
            self.hearts -= 1
            self.last_hit_time = current_time
            # Knockback effect
            if self.player_rect.centerx > self.enemy.centerx:
                self.player_rect.x += 50
                self.velocity_y = -5  # Small upward knockback
            else:
                self.player_rect.x -= 50
                self.velocity_y = -5  # Small upward knockback

    def draw_hearts(self):
        heart_spacing = 35
        for i in range(self.max_hearts):
            pos = (10 + i * heart_spacing, 10)
            if i < self.hearts:
                self.display_surface.blit(self.heart_img, pos)
            else:
                self.display_surface.blit(self.empty_heart_img, pos)
        
    def run(self):
        self.display_surface = pygame.display.get_surface()
        keys = pygame.key.get_pressed()
        self.velocity_x = 0
        if keys[pygame.K_a]:
            self.velocity_x = -5
        if keys[pygame.K_d]:
            self.velocity_x = 5

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        self.velocity_y += self.gravity
        self.player_rect.x += self.velocity_x
        self.player_rect.y += self.velocity_y

        self.update_moving_platform()
        self.check_enemy_collision()

        # Collision detection with platforms
        self.on_ground = False
        for platform in self.platforms:
            if self.player_rect.colliderect(platform):
                # Check if collision is from above (landing on platform)
                if (self.velocity_y > 0 and 
                    self.player_rect.bottom > platform.top and 
                    self.player_rect.top < platform.top):
                    self.player_rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True
                # Check if collision is from below (hitting head)
                elif (self.velocity_y < 0 and 
                      self.player_rect.top < platform.bottom and 
                      self.player_rect.bottom > platform.bottom):
                    self.player_rect.top = platform.bottom
                    self.velocity_y = 0
                # Check if collision is from the left side
                elif (self.velocity_x > 0 and 
                      self.player_rect.right > platform.left and 
                      self.player_rect.left < platform.left):
                    self.player_rect.right = platform.left
                    # Add slight downward push to make player slide down
                    self.velocity_y = 8
                
                # Check if collision is from the right side
                elif (self.velocity_x < 0 and 
                      self.player_rect.left < platform.right and 
                      self.player_rect.right > platform.right):
                    self.player_rect.left = platform.right
                    # Add slight downward push to make player slide down
                    self.velocity_y = 8

        # Screen boundaries
        if self.player_rect.left < 0:
            self.player_rect.left = 0
        if self.player_rect.right > WINDOW_WIDTH:
            self.player_rect.right = WINDOW_WIDTH
        if self.player_rect.top < 0:
            self.player_rect.top = 0
        
        # Check if player hits the deadly platform
        killing_platform = pygame.Rect(0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50)  # Floor
        if self.player_rect.colliderect(killing_platform):
            self.hearts -= 1 
            self.player_rect.topleft = (100, 600)

        # Animation handling
        if keys[pygame.K_a]:
            self.frame += 1.5
            if self.frame // self.animation_speed % 3 == 0:
                self.player = self.walking_left
            elif self.frame // self.animation_speed % 3 == 1:
                self.player = self.walking_left2
            else:
                self.player = self.walking_left3
        elif keys[pygame.K_d]:
            self.frame += 1.5
            if self.frame // self.animation_speed % 3 == 0:
                self.player = self.walking_right
            elif self.frame // self.animation_speed % 3 == 1:
                self.player = self.walking_right2
            else:
                self.player = self.walking_right3

        # Drawing
        self.display_surface.blit(self.background, (0, 0))
        pygame.draw.rect(self.display_surface, self.flag_color, self.flag)
        #pygame.draw.rect(self.display_surface, self.color, self.enemy)
        #pygame.draw.rect(self.display_surface, self.player_color, self.player_rect)
        
        # Draw 
        self.draw_hearts()
        self.display_surface.blit(self.player, self.player_rect.topleft)
        self.display_surface.blit(self.current_crab_img, self.enemy)
        self.update_moving_platform()
        # Draw platform
        #for platform in self.platforms:
            #pygame.draw.rect(self.display_surface, (100, 100, 100), platform)        
        
        pygame.display.update()
        # Reset level when out of hearts
        if self.hearts <= 0:
            game_over_font = pygame.font.SysFont("Arial", 50)
            game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
            self.display_surface.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))
            restart_font = pygame.font.SysFont("Arial", 30)
            restart_text = restart_font.render("Press R to restart level", True, (255, 255, 255))
            self.display_surface.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 - restart_text.get_height() // 2 + 50))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.hearts = self.max_hearts  # Reset hearts to full
                        self.player_rect = pygame.Rect(100, 600, 50, 50) # Port me to start
                        return Level1()  # Restart level with full hearts
        
        pygame.display.update()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return None

        return self  # Continue current level