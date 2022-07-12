import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self, pos, image, scale=(32, 32)):
        super().__init__()

        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=pos)

        self.move = 0


    def control(self, x):
        self.movex += x


    def update(self):
        self.rect.x = self.rect.x + 1