import pygame
import time
import random

#Define colours
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0

score = 0 #Set the initial score
background = pygame.image.load('grid_background.png')

#Initial screen stuff
pygame.init()
width, height = 720, 480
pygame.display.set_caption('ICS3U/C1 Snake Game')
screen = pygame.display.set_mode((width, height))

#Sound Effect Stuff
pygame.mixer.init()
munch = pygame.mixer.Sound('munch.wav')
game_background_music=pygame.mixer.Sound('game_background_sound.mp3')
game_over_sound=pygame.mixer.Sound('game_over.mp3')

#Snake Information
snake_position = [360, 240]
snake_speed = 10
direction = 'RIGHT'
snake_body = [[360,240],[350,240],[340,240],[330,240]]

#FRUIT!
apple_image = pygame.image.load('apple.png')
apple_image = pygame.transform.scale(apple_image, (10, 10))
fruit_position = [random.randrange(0, (width//10))*10,
                  random.randrange(0, (height//10))*10]

def endgame():
    #Create a font object
    my_font = pygame.font.SysFont('comicsansms', 50)

    #Create text surface
    game_over_surface = my_font.render('GAME OVER', True, red)

    #Create a rectangle object for the surface
    game_over_rect = game_over_surface.get_rect()

    #Position our game over object
    game_over_rect.center = [(width/2), (height/2)]

    #blit = draw the surface onto the rectangle
    screen.blit(game_over_surface, game_over_rect)

    pygame.display.flip() #Update the screen

    time.sleep(2)

    #Deactivate the quit
    game_background_music.stop()
    pygame.quit()
    quit()

#Display the score
def scoring(score):
    #Create a font object
    score_font = pygame.font.SysFont('comicsansms', 20)

    #Create text surface
    score_surface = score_font.render('Score: '+str(score), True, red)

    #Create a rectangle object for the surface
    score_rect = score_surface.get_rect()

    #blit = draw the surface onto the rectangle
    screen.blit(score_surface, score_rect)

    pygame.display.flip() #Update the screen

game_background_music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    #screen.fill(black) #Fill in the screen
    screen.blit(background, (0,0))

    #Set the snake on the screen
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    #Draw my fruit
    #pygame.draw.circle(screen, red, (fruit_position[0]+5,fruit_position[1]+5),5)
    screen.blit(apple_image, (fruit_position[0], fruit_position[1]))

    #Moving the snake
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    snake_body.insert(0, list(snake_position))

    #Eat the fruit
    if snake_position==fruit_position:
        fruit_position = [random.randrange(0, (width//10))*10,
                        random.randrange(0, (height//10))*10]
        score += 10
        snake_speed += 3
        munch.play()
    else:
        snake_body.pop()

    scoring(score)#Display the score

    pygame.display.flip()

    #Create a clock
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

    #Endgame conditions
    if snake_position[0] < 0 or snake_position[0] >= width:
        game_background_music.stop()
        game_over_sound.play()
        endgame() 
    if snake_position[1] < 0 or snake_position[1] >= height:
        game_background_music.stop()
        game_over_sound.play() 
        endgame() 
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_background_music.stop()
            game_over_sound.play() 
            endgame()  

pygame.quit()