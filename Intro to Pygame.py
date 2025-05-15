import pygame

pygame.init() #Initialize a pygame class

#Set our screen size
width, height= 400, 400
screen = pygame.display.set_mode((width, height))

#Main running loop
running=True
while running:
    pygame.display.flip() #Refreshes the screen

pygame.quit() #Quits pygame properly