import pygame

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
#Define a rectangle colour
rect_colour= 10, 120, 120
#Main running loop
running=True
while running:
#Create an event in game
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.draw.rect(screen, rect_colour, pygame.Rect(30, 30, 60, 60))
    pygame.draw.circle(screen, (200,0,0), (60,60),(10))

    pygame.display.flip() #Refreshes the screen

pygame.quit() #Quits pygame properly

