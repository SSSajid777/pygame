import pygame
import time
import random

#Define colors
black=-0,0,0
green=0,255,0
red=255,0,0

pygame.init()
#Set our screen size
width, height= 720, 480
pygame.display.set_caption("ICS3U/C Snake Game")
screen = pygame.display.set_mode((width, height))


#Snake Information 
snake_position=[360, 240] 
snake_speed=10
direction='RIGHT'
snake_body=[[360,240],[350, 240], [340, 240], [330, 240]]


#FRUIT!
fruit_position = [random.randrange(0, (width//10))*10,
                  random.randrange(0, (height//10))*10]
def endgame():
    #Create a font object
    my_font=pygame.font.SysFont('comicsansms', 50)

    #Create text surface
    game_over_surface=my_font.render('GAME OVER', True, red)

    #Create a rectangle object for the surface
    game_over_rect=game_over_surface.get_rect()

    #Position our game over object
    game_over_rect.center=[(width/2),(height/2)]

    #blit= draw the surface on the rectangle
    screen.blit(game_over_surface, game_over_rect)

    #Update the screen
    pygame.display.flip()  #Update the screen

    time.sleep(2)

    #Deactivate the quit
    pygame.quit()
    quit()

#Main running loop
running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and direction != 'DOWN':
                direction='UP'
            if event.key==pygame.K_DOWN and direction != 'UP':
                direction='DOWN'
            if event.key==pygame.K_LEFT and direction != 'RIGHT':
                direction='LEFT'
            if event.key==pygame.K_RIGHT and direction != 'LEFT':
                direction='RIGHT'


    screen.fill(black) #Fill in the screen

    #Set the snake on the screen
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    #Draw my fruit
    pygame.draw.circle(screen, red, (fruit_position[0]+5, fruit_position[1]+5),5)
    
    


    #Moving the snake
    if direction=='RIGHT':
        snake_position[0] += 10
    if direction=='LEFT':
        snake_position[0] -= 10
    if direction=='UP':
        snake_position[1] -= 10
    if direction=='DOWN':
        snake_position[1] += 10

    snake_body.insert(0, list(snake_position))
    
    #Eat the fruit
    if snake_position[0]==fruit_position[0]and snake_position[1]==fruit_position[1]:
        fruit_position = [random.randrange(0, (width//10))*10,
                  random.randrange(0, (height//10))*10]
    else:
     snake_body.pop()                                                  #how do you remove the last element of the list? ((pop))  (exam question)

    
    pygame.display.flip() #Refreshes the screen
    #Create a a clock
    clock=pygame.time.Clock()
    clock.tick(snake_speed) 

#Endgame conditions
    if snake_position[0] < 0 or snake_position[0] > width:
     endgame()
    if snake_position[1] < 0 or snake_position[1] > height:
     endgame()
     for block in snake_body[1:]:
         if snake_position[0]== block[0] and snake_position[1]==block[1]:
             endgame()
        


pygame.quit()