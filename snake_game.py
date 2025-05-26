import pygame

pygame.init()
#Set our screen size
width, height= 400, 400
screen = pygame.display.set_mode((width, height))

#Main running loop
running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    pygame.display.flip() #Refreshes the screen

pygame.quit()