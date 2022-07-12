import pygame as pg


class Bullet(pg.sprite.Sprite):

    def __init__(self, image, pos, scale = (32, 32), limits = (640, 480)):
        super().__init__()

        # Sprite
        (self.wl, self.hl) = limits
        (self.w, self.h) = scale
        
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=pos)
        
        pass


    def update(self):
        self.rect.y -= 3
    pass