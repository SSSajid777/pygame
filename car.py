import pygame

class Car(pygame.sprite.Sprite):   #init is called constructor (exam question)


    def __init__(self, colour, width, height):
        #Call Sprite constructor
        super().__init__

        self.image=pygame.surface((width, height))
        self.image.fill(255,255,255)   
     