from setting import *
from level import Level
class Level1:
    def __init__(self):
        self.player_rect = pygame.Rect(50, 620, 10, 10)  
        self.background = pygame.image.load("data/Levels/Level1.png")
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.player = pygame.image.load("data/Aseprite/Pirate.png")

        self.walking_left = pygame.image.load("data/Aseprite/walking_left.png")
        self.walking_left2 = pygame.image.load("data/Aseprite/walking_left2.png")
        self.walking_left3 = pygame.image.load("data/Aseprite/walking_left3.png")

        self.walking_right = pygame.image.load("data/Aseprite/walking_right.png")
        self.walking_right2 = pygame.image.load("data/Aseprite/walking_right2.png")
        self.walking_right3 = pygame.image.load("data/Aseprite/walking_right3.png")

        self.zoom_level = 1.8
        self.target_zoom = 1.8
        self.zoom_speed = 5

        self.frame = 0
        self.animation_speed = 10


    def run(self):
        self.display_surface = pygame.display.get_surface()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_rect.y += 10
        if keys[pygame.K_s]:
            self.player_rect.y -= 10
        if keys[pygame.K_a]:
            self.player_rect.x += 10
        if keys[pygame.K_d]:
            self.player_rect.x -= 10       

        # Animation 
        if  keys[pygame.K_a]:
            self.frame += 1.5
            if self.frame // self.animation_speed % 2 == 0:
                self.player = self.walking_left
            elif self.frame // self.animation_speed % 2 == 1:
                self.player = self.walking_left2
            elif self.frame // self.animation_speed % 3 == 2:
                self.player = self.walking_left3
        elif keys[pygame.K_d]:
            self.frame += 1.5
            if self.frame // self.animation_speed % 2 == 0:
                self.player = self.walking_right
            elif self.frame // self.animation_speed % 2 == 1:
                self.player = self.walking_right2
            elif self.frame // self.animation_speed % 3 == 2:
                self.player = self.walking_right3

        # Zoom level
        if self.zoom_level != self.target_zoom:
            self.zoom_level += (self.target_zoom - self.zoom_level) * self.zoom_speed
        
        # Calculate the scaled background size
        scaled_width = int(WINDOW_WIDTH * self.zoom_level)
        scaled_height = int(WINDOW_HEIGHT * self.zoom_level)
        scaled_background = pygame.transform.scale(self.background, (scaled_width, scaled_height))
        
        # Calculate the offset to center the player
        offset_x = self.player_rect.centerx - scaled_width // 4
        offset_y = self.player_rect.centery - scaled_height // 4
        
        # Draw the scaled background
        self.display_surface.blit(scaled_background, (offset_x, offset_y))
        
        # Calculate player's position on the scaled background
        player_scaled_x = self.player_rect.centerx - offset_x
        player_scaled_y = self.player_rect.centery - offset_y
        
        self.display_surface.blit(self.player, (player_scaled_x, player_scaled_y))
        
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.current_stage = Level()

