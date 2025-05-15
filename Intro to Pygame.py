import pygame

pygame.init() #Initialize a pygame class

#Set our screen size
width, height= 400, 400
screen = pygame.display.set_mode((width, height))

background_color= 34, 92, 186  #Set the background color in RGB

#Load in our image

sad=pygame.image.load("sadface.jfif")
pikachu= pygame.transform.scale(sad, (50, 40))

#Main running loop
running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(background_color)   
    pygame.display.flip() #Refreshes the screen

pygame.quit() #Quits pygame properly

