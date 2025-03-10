from setting import *
from level import Level
class Level1:
    def __init__(self):
        pygame.init()  
        self.player_rect = pygame.Rect(100, 600, 50, 50) 
        self.player = pygame.image.load("data/Aseprite/Pirate.png")

        # Animace 
        self.walking_left = pygame.image.load("data/Aseprite/walking_left.png")
        self.walking_left2 = pygame.image.load("data/Aseprite/walking_left2.png")
        self.walking_left3 = pygame.image.load("data/Aseprite/walking_left3.png")

        self.walking_right = pygame.image.load("data/Aseprite/walking_right.png")
        self.walking_right2 = pygame.image.load("data/Aseprite/walking_right2.png")
        self.walking_right3 = pygame.image.load("data/Aseprite/walking_right3.png")

        self.background = pygame.image.load("data/Levels/Level1.png")
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.on_ground = False

        self.platforms = [
            pygame.Rect(0, WINDOW_HEIGHT - 30, WINDOW_WIDTH, 50),  # Zem
            pygame.Rect(70, 680, 230, 30),
            pygame.Rect(400, 784, 180, 250)
        ]

        self.frame = 0
        self.animation_speed = 10

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
        # Gravitace
        self.velocity_y += self.gravity

        # Aktualizace pozice hráče
        self.player_rect.x += self.velocity_x
        self.player_rect.y += self.velocity_y

        # Detekce kolizí s platformami
        self.on_ground = False
        for platform in self.platforms:
            if self.player_rect.colliderect(platform):
                if self.velocity_y > 0:  # Padání dolů
                    self.player_rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Náraz hlavou do platformy
                    self.player_rect.top = platform.bottom
                    self.velocity_y = 0

    
        if self.player_rect.left < 0:
            self.player_rect.left = 0
        if self.player_rect.right > WINDOW_WIDTH:
            self.player_rect.right = WINDOW_WIDTH
        if self.player_rect.top < 0:
            self.player_rect.top = 0

        if keys[pygame.K_a]:
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

        for platform in self.platforms:
            pygame.draw.rect(self.display_surface, (0, 0, 0), platform)

        self.display_surface.blit(self.background, (0, 0))
        self.display_surface.blit(self.player, self.player_rect.topleft)


        pygame.display.update()
        if keys[pygame.K_ESCAPE]:
            self.current_stage = Level()
