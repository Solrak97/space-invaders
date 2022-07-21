import pygame as pg

class Enemy(pg.sprite.Sprite):

    def __init__(self, pos, image, y_limit, scale=(32, 32), movement_pattern = 0):
        super().__init__()

        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, scale)
        self.image = pg.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center=pos)

        # Lifetime
        self.lifetime = 0

        # Speed
        self.speed = 2
        self.frame_speed = 15

        # Space limits
        self.y_limit = y_limit

        # Movement patterns
        self.movement_pattern = movement_pattern
        self.pattern_state = 0

    
    def bullet_collision(self, point):
        return self.rect.collidepoint(point)

    
    def down_move(self):
        if self.lifetime % self.frame_speed == 0:
            self.rect.y += self.speed


    
    def on_floor(self):
        if self.rect.y > self.y_limit:
            self.kill()
            return True
        
        else:
            return False
        

    def update(self):
        self.down_move()
        self.lifetime += 1