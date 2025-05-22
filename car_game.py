import pygame 
pygame.init() #Initialize a pygame class

from car import Car        #How do we impoprt class (exam question)

#Set our screen size
width, height= 400, 400
screen = pygame.display.set_mode((width, height))


running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()

pygame.quit() #Quits pygame properly