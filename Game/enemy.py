import pygame as pg

class Enemy(pg.sprite.Sprite):

    def __init__(self, pos, image, scale=(32, 32), movement_pattern = 0):
        super().__init__()

        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, scale)
        self.image = pg.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center=pos)

    
    def bullet_collision(self, point):
        return self.rect.collidepoint(point)

    
    def update(self):
        self.rect.y += 1