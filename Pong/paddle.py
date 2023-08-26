# Importing the pygame library
import pygame

BLACK = (0, 0,0)

class Paddle(pygame.sprite.Sprite):
    #creating a constructor  self is the "this" keyword in java
    def __init__(self, color, width, height):
        #similar to java, use keyword super to access to parent construtor method
        super().__init__()
        #define what the paddle looks like. self.image is the imaginary hitbox
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        #set_colorkey helps see the background so that the white won't cover the whole screen
        self.image.set_colorkey(BLACK)
        #creating a drawing on top of the hitbox
        pygame.draw.rect(self.image, color, [0, 0, width, height], 0)
        #fetching the rectangle and set it equal to the sprite 
        self.rect = self.image.get_rect()
    
    def moveDown(self, pixel):
        if self.rect.y < 400:
            self.rect.y += pixel
        
    
    def moveUp(self, pixel):
        if self.rect.y > 0:
            self.rect.y -= pixel
    
    