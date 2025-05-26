import pygame

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
    pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], 10, 10))
    
    pygame.display.flip() #Refreshes the screen


    #Moving the snake
    if direction=='RIGHT':
        snake_position[0] += 10
    if direction=='LEFT':
        snake_position[0] -= 10
    if direction=='UP':
        snake_position[1] -= 10
    if direction=='DOWN':
        snake_position[1] += 10
    #Create a a clock
    clock=pygame.time.Clock()
    clock.tick(snake_speed) 


pygame.quit()