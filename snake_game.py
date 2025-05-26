import pygame

pygame.init()
#Set our screen size
width, height= 720, 480
pygame.display.set_caption("ICS3U/C Snake Game")
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