import pygame
import time

pygame.init() #Initialize a pygame class

#Set our screen size
width, height= 400, 400
screen = pygame.display.set_mode((width, height))

background_color= 0, 119, 214  #Set the background color in RGB

#Load in our image
sad=pygame.image.load("sadface.jfif")
sad= pygame.transform.scale(sad, (80, 60))
sad_rect= sad.get_rect()

#Load in our crosshair image
crosshairs=pygame.image.load("crosshair.webp")
crosshairs= pygame.transform.scale(crosshairs, (30, 30))
crosshairs_rect= crosshairs.get_rect()
pos=[0,0]

#Sets pikachu's speed
sad_speed=[1,1]


#Main running loop
running=True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(background_color)
    
    screen.blit(sad, sad_rect)  #Adds pikachu image to the rectangle
    screen.blit(crosshairs, pos, crosshairs_rect)   
    """
    sad_rect=sad_rect.move(sad_speed)
    
    #Bound pikachu in our screen
    if sad_rect.left < 0 or sad_rect.right > width:
        sad_speed[0]= -sad_speed[0]
    if sad_rect.top < 0 or sad_rect.bottom > height:
        sad_speed[1]= -sad_speed[1]
    """

    pygame.display.flip() #Refreshes the screen

    time.sleep(10/1000)  #Slowed down pikachu

pygame.quit() #Quits pygame properly

