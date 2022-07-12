import pygame as pg
from pygame.locals import *

class Player(pg.sprite.Sprite):

    def __init__(self, pos, image, scale=(32, 32), limits = (640, 480)):
        super().__init__()

        # Sprite
        (self.wl, self.hl) = limits
        (self.w, self.h) = scale
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=pos)

        # Movement
        self.velocity = 5
        self.movement = 0
        self.max_speed = 10
    
    def move(self, velocity):
        self.movement += velocity
        self.movement = max(-self.max_speed, min(self.movement, self.max_speed))
        

    def shoot():
        pass


    def update(self):
        
        if (self.rect.x + self.movement) < 0:
            self.rect.x = self.w/2

        elif (self.rect.x + self.movement) > self.wl:
            self.rect.x = self.wl - self.w
        
        else:
            self.rect.x += self.movement
        


    def controller(self, keystate):
        if keystate[pg.K_a]:
            self.move(-self.velocity)
        
        if keystate[pg.K_d]:
            self.move(self.velocity)

        # Shoot
        if keystate[pg.K_SPACE]:
            self.move(-self.step)

        if not any(keystate):
            self.movement = 0
           