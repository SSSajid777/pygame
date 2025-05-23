import pygame 
pygame.init() #Initialize a pygame class

from car import Car        #How do we import class (exam question)

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
playerCar1.rect.x=200
playerCar1.rect.y=300

playerCar2=Car(PURPLE,20,30)
playerCar2.rect.x=100
playerCar2.rect.y=100

#Add our sprites to the list
all_spirte_list.add(playerCar1)
all_spirte_list.add(playerCar2)

running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #Draw some grass
    screen.fill(GREEN)

    #Find all keys that are pressed
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerCar1.moveLeft(1)
    if keys[pygame.K_RIGHT]:
        playerCar1.moveRight(1)
    if keys[pygame.K_UP]:
        playerCar1.moveUp(1)
    if keys[pygame.K_DOWN]:
        playerCar1.moveDown(1)

    if keys[pygame.K_LEFT]:
        playerCar2.moveLeft(1)
    if keys[pygame.K_RIGHT]:
        playerCar2.moveRight(1)
    if keys[pygame.K_UP]:
        playerCar2.moveUp(1)
    if keys[pygame.K_DOWN]:
        playerCar2.moveDown(1)


    #Draw all our sprites
    all_spirte_list.draw(screen)
    
    pygame.display.flip()

    #Createa a clock
    clock=pygame.time.Clock()
    clock.tick(60) 

pygame.quit() #Quits pygame properly

