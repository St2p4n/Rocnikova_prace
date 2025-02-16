from setting import *
class Level:
   def __init__(self):
      self.display_surface = pygame.display.get_surface()
      self.clock = pygame.time.Clock()

      self.background = pygame.transform.scale(pygame.image.load("data/Levels/background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
      self.player = pygame.image.load("data/Aseprite/Pirate.png")

      self.move_down = pygame.image.load("data/Aseprite/towards-going1.png")
      self.move_down2 = pygame.image.load("data/Aseprite/towards-going2.png")

      self.player_rect = self.player.get_rect(topleft=(600, 400))
      self.speed = 3

      self.frame = 0  
      self.animation_speed = 10  

   def run(self):
      keys = pygame.key.get_pressed()
      moving_down = False

      if keys[pygame.K_LEFT] or keys[pygame.K_a]:
         self.player_rect.x -= self.speed
      if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
         self.player_rect.x += self.speed
      if keys[pygame.K_UP] or keys[pygame.K_w]:
         self.player_rect.y -= self.speed
      if keys[pygame.K_DOWN] or keys[pygame.K_s]:
         self.player_rect.y += self.speed
         moving_down = True  
    
      if moving_down:
         self.frame += 1
         if self.frame // self.animation_speed % 2 == 0:
            self.player = self.move_down
         else:
            self.player = self.move_down2
      else:
         self.player = self.player  
      
      self.display_surface.blit(self.background, (0, 0))
      self.display_surface.blit(self.player, self.player_rect.topleft)

      pygame.display.update()
      self.clock.tick(60) 


     
