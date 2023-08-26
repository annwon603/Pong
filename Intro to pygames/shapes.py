# Importing the pygame library
import pygame

# initializing the pygame library
pygame.init()

# Creat a window for our game to take place, we pass in a set of pixels
game_window = pygame.display.set_mode((600, 600))

# Lets set the background color for our window
game_window.fill((0, 0, 0))

# Square
# rect ( where do you want me to draw this in? What color? left, top, width height)

pygame.draw.rect(game_window, (255, 255, 255), [240, 300, 150, 10], 0)
pygame.draw.line(game_window, (255,255,255), [50,100], [200,150], width=1)
pygame.draw.line(game_window, (255,255,255), [550,100], [450,150], width=1)
#eyes
pygame.draw.circle(game_window, (255,255,255), [100,200], 20, 0)
pygame.draw.circle(game_window, (255,255,255), [500,200], 20, 0)



pygame.display.update()

#Circle
# pygame.draw.circle(game_window, (255, 255, 255), [300, 300], 200, 0)
# pygame.display.update()

#Triangle
# pygame.draw.polygon(game_window, (255, 255, 255), [[300, 300], [100, 400], [100, 300]], 5)
# pygame.display.update()

#Line
# pygame.draw.line(game_window, (255, 255, 255), [0, 300], [600, 300], width=1)
# pygame.display.update()


run_game = True

while run_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run_game = False