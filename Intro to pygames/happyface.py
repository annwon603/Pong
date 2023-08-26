# Importing the pygame library
import pygame

# initializing the pygame library
pygame.init()

# Creat a window for our game to take place, we pass in a set of pixels
game_window = pygame.display.set_mode((600, 600))

# Lets set the background color for our window
game_window.fill((0, 0, 0))

#Circle
# pygame.draw.circle(game_window, (255, 255, 255), [300, 300], 200, 0)
# pygame.display.update()

pygame.draw.circle(game_window, (255,255,255),[300,300],250,5)


#Line
# pygame.draw.line(game_window, (255, 255, 255), [0, 300], [600, 300], width=1)
# pygame.display.update()

pygame.draw.line(game_window,(255,255,255),[200,175],[200,225],2)
pygame.draw.line(game_window,(255,255,255),[400,175],[400,225],2)

pygame.draw.circle(game_window,(255,255,255),[300,300],100,2)
# rect ( where do you want me to draw this in? What color? left, top, width height)
pygame.draw.rect(game_window,(0,0,0),[203,200,194,100],0)
pygame.display.update()








run_game = True

while run_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run_game = False