import pygame as pg

from bullet import Bullet


class Player(pg.sprite.Sprite):

    def __init__(self, pos, image, bullet_group, scale=(32, 32), limits = (640, 480)):
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

        # Bullet group
        self.bullet_group = bullet_group

        # Frames
        self.shoot_frame = 0
        self.shoot_thresh = 20

    
    def move(self, velocity):
        self.movement += velocity
        self.movement = max(-self.max_speed, min(self.movement, self.max_speed))

        if (self.rect.x + self.movement) < 0:
            self.rect.x = self.w/2

        elif (self.rect.x + self.movement) > self.wl:
            self.rect.x = self.wl - self.w
        
        else:
            self.rect.x += self.movement
        

    def shoot(self):
        if self.shoot_frame >= self.shoot_thresh:
            self.bullet_group.add(Bullet('Assets/bala1.png', pos=(self.rect.x + self.w / 2, self.rect.y), scale=(10, 10)))
            self.shoot_frame = 0


    def update(self):
        self.controller(pg.key.get_pressed())
        self.shoot_frame += 1


    def controller(self, keystate):
        if keystate[pg.K_a]:
            self.move(-self.velocity)
        
        if keystate[pg.K_d]:
            self.move(self.velocity)

        # Shoot
        if keystate[pg.K_SPACE]:
            self.shoot()

        if not keystate[pg.K_a] and not keystate[pg.K_d] :
            self.movement = 0
           