import pygame 
pygame.init() #Initialize a pygame class

from car import Car        #How do we impoprt class (exam question)

#Set our screen size
width, height= 400, 400
screen = pygame.display.set_mode((width, height))

GREEN=(100,255,200)
GREY=(210,210,210)
WHITE=(255,255,255)
RED=(255,0,0)
PURPLE=(255,0,255)

#Create a list that will contain all our sprites
all_spirte_list=pygame.sprite.Group()
playerCar1=Car(RED,20,30)

running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()

pygame.quit() #Quits pygame properly

