import pygame

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
#Define a rectangle colour
rect_colour= 10, 120, 120

#Define a circular color
circle_colour= 255,0,100

#Define line colour
line_colour= 255,255,100

#Main running loop
running=True
while running:
#Create an event in game    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #Draw a rectangle
    pygame.draw.rect(screen, rect_colour, pygame.Rect(30, 30, 60, 60))
    #Draw a circle
    pygame.draw.circle(screen, circle_colour, (200,200),(20))
    #Draw a line
    pygame.draw.line(screen, line_colour, (300,10), (300,300), 10)

    pygame.display.flip() #Refreshes the screen

pygame.quit() #Quits pygame properly

