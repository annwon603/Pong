# Importing the pygame library
import pygame

BLACK = (0 , 0 , 0)

class Ball(pygame.sprite.Sprite):
    
    def __initi__(self, color, width, height):
        
        super().__init__()
        #creating a hit box for the ball
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        #creating a drawing on top of the hitbox
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
        
    
        
    
        