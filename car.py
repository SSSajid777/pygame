import pygame
WHITE=(255,255,255)

class Car(pygame.sprite.Sprite):   #init is called constructor (exam question)

    def __init__(self, colour, width, height):
        #Call Sprite constructor
        super().__init__()  

        #Set the background colour and set it to be transparent
        self.image=pygame.Surface([width, height])  #Create out pygame surface
        self.image.fill(WHITE) #Fill the surface with a colour
        self.image.set_colorkey(WHITE) 

        #Draw a rectangle
        pygame.draw.rect(self.image, colour, [0,0, width, height])
        #Instead we could load a proper picture of a car..
        #self.image=pygame.image.load("car.png").convert_alpha()
        self.rect=self.image.get_rect()  #Get the rectangle of the image
 
     