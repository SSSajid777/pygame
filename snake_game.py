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
snake_speed=15
direction='RIGHT'
#Main running loop
running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #Set the snake on the screen
    pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], 10, 10))
    
    pygame.display.flip() #Refreshes the screen

pygame.quit()