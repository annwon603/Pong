# Importing the pygame library
import pygame

#importing the Paddle class from paddle.py
from paddle import Paddle
#importing the Ball class from ball.py
from ball import Ball
# initializing the pygame library
pygame.init()

# defining colors based on RGB
NAVY_BLUE = (32 , 42 , 68)
WHITE = (255, 255, 255)

#size of the game window
#700 is width,500 is height
size = (700 , 500)
#created the screen
game_window = pygame.display.set_mode(size)
#gave the screen a title
pygame.display.set_caption("Pong")

#Creating new paddles
paddle1 = Paddle(WHITE, 10, 100)
#x and y coordinates represent the top-left of the paddle
paddle1.rect.x = 20
paddle1.rect.y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 670
paddle2.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x=345
ball.rect.y=245

sprite_list = pygame.sprite.Group()
sprite_list.add(paddle1)
sprite_list.add(paddle2)
sprite_list.add(ball)

run_game = True
# in-game clock to keep track of time intervals
# counts every ms, 1000 ms= 1 sec
clock = pygame.time.Clock()

score_player_1 = 0
score_player_2 = 0

while run_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run_game = False
    
    keys = pygame.key.get_pressed()
    #pygames.K_s is a static variable where K stands for key and s stands for the key s
    if keys[pygame.K_s]:
        paddle1.moveDown(5)
    if keys[pygame.K_w]:
        paddle1.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(5)
    if keys[pygame.K_UP]:
        paddle2.moveUp(5)
    
    sprite_list.update()
    
    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]
        score_player_1 += 1
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        score_player_2 += 1
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]    
    
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()
    
    
    #things I want to be consistent throughtout the game
    game_window.fill(NAVY_BLUE)
    #drawing the net in the middle       [top]     [bottom]  [width]
    pygame.draw.line(game_window, WHITE, [349, 0], [349, 500], 5)
    
    sprite_list.draw(game_window)
    
    font = pygame.font.Font(None, 75)
    text = font.render(str(score_player_1), 1, WHITE)
    game_window.blit(text, (250,10) )
    text = font.render(str(score_player_2), 1, WHITE)
    game_window.blit(text, (420,10) )
    
    #updates the screen
    pygame.display.flip()
    #clock is ticking 60x per second
    clock.tick(60)
    
pygame.quit()            
