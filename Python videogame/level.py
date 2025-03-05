from setting import *
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
      
        self.background = pygame.image.load("data/Levels/background.png")
        self.player = pygame.image.load("data/Aseprite/Pirate.png")
        
        self.move_down = pygame.image.load("data/Aseprite/towards-going1.png")
        self.move_down2 = pygame.image.load("data/Aseprite/towards-going2.png")
        self.move_up = pygame.image.load("data/Aseprite/towards-going1.png")
        self.move_up2 = pygame.image.load("data/Aseprite/towards-going2.png")

        self.player_rect = self.player.get_rect(topleft=(600, 420))
        self.speed = 8

        self.frame = 0
        self.animation_speed = 10
        
        self.zoom_level = 2.1
        self.target_zoom = 2.1
        self.zoom_speed = 0.5

        self.path_segments = [
        ((600, 420), (600, 200)),  # Vertical segment (600, 420) to (600, 200)
        ((600, 200), (350, 200)),  # Horizontal segment (600, 200) to (350, 200)
        ((350, 200), (-770, 200)), 
        ((-770, 200), (-770, 200)), 
        ((-770, 200), (-770, 440)),
        ((-770, 440), (-770, 80)),
        ((-770, 80), (-1005, 80)),
        ((-1005, 80), (-1005, -710)),
        ((-1005, -710), (-1005, -710)),
        ((-1005, -710), (-100, -710))
        ]     
       

        self.current_segment = 0  # Start with the first segment

    def run(self):
        keys = pygame.key.get_pressed()
        moving_down = False
        moving_up = False

        # Get the current segment start and end points
        segment_start, segment_end = self.path_segments[self.current_segment]

        # Player movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move_along_path(segment_start, segment_end, "up")
            moving_up = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move_along_path(segment_start, segment_end, "down")
            moving_down = True

        # Animation 
        if moving_up:
            self.frame += 1
            if self.frame // self.animation_speed % 2 == 0:
                self.player = self.move_up
            else:
                self.player = self.move_up2
        elif moving_down:
            self.frame += 1
            if self.frame // self.animation_speed % 2 == 0:
                self.player = self.move_down
            else:
                self.player = self.move_down2
        else:
            self.player = self.player

        # Zoom level
        if self.zoom_level != self.target_zoom:
            self.zoom_level += (self.target_zoom - self.zoom_level) * self.zoom_speed

        # Calculate the scaled background size
        scaled_width = int(WINDOW_WIDTH * self.zoom_level)
        scaled_height = int(WINDOW_HEIGHT * self.zoom_level)
        scaled_background = pygame.transform.scale(self.background, (scaled_width, scaled_height))

        # Calculate the offset to center the player
        offset_x = self.player_rect.centerx - scaled_width // 4.5
        offset_y = self.player_rect.centery - scaled_height // 4.5

        # Draw the scaled background
        self.display_surface.blit(scaled_background, (offset_x, offset_y))

        # Calculate player's position on the scaled background
        player_scaled_x = self.player_rect.centerx - offset_x
        player_scaled_y = self.player_rect.centery - offset_y

        self.display_surface.blit(self.player, (player_scaled_x, player_scaled_y))

        pygame.display.update()
        self.clock.tick(60)

    def move_along_path(self, segment_start, segment_end, direction):
        if segment_start[0] == segment_end[0]:  # Vertical segment
            if direction == "up":
                self.player_rect.y -= self.speed
            elif direction == "down":
                self.player_rect.y += self.speed
        else:  # Horizontal segment
            if direction == "up":
                self.player_rect.x -= self.speed
            elif direction == "down":
                self.player_rect.x += self.speed

        if segment_start[0] == segment_end[0]:  # Vertical segment
            self.player_rect.y = max(min(self.player_rect.y, max(segment_start[1], segment_end[1])), min(segment_start[1], segment_end[1]))
        else:  # Horizontal segment
            self.player_rect.x = max(min(self.player_rect.x, max(segment_start[0], segment_end[0])), min(segment_start[0], segment_end[0]))

        # Check if the player has reached the end of the current segment
        if self.player_rect.topleft == segment_end:
            if self.current_segment < len(self.path_segments) - 1:
                self.current_segment += 1  # Move to the next segment
            else:
                print("Player has reached the end of the path!")
        elif self.player_rect.topleft == segment_start:
            if self.current_segment > 0:
                self.current_segment -= 1  # Move to the previous segment
            else:
                print("Player has reached the start of the path!")

    def set_zoom(self, zoom_level):
        self.target_zoom = zoom_level

    

    
