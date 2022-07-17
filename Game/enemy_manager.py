import pygame as pg
import random

from enemy import Enemy


class EnemyManager:

    def __init__(self, enemy_group, bullet_group, limits=(640, 480)):
        # Sprite groups
        self.enemy_group = enemy_group
        self.bullet_group = bullet_group

        # Limits
        self.x_limit, self.y_limit = limits

        # Spawntime
        self.last_spawn = 0
        self.wave_thresh = 240

        # Enemy Scale
        self.enemy_widht, self.enemy_height = (32, 32)
        pass

    def wave_t1(self):
        for x in range(int(self.x_limit / self.enemy_widht)):
            for y in range(4):
                enemy = Enemy((x * self.enemy_widht + self.enemy_widht / 2, -y *
                              self.enemy_height), 'Assets/enemigo0.png', self.y_limit, scale=(self.enemy_widht, self.enemy_height))
                self.enemy_group.add(enemy)

    def wave_t2(self):
        for x in range(int(self.x_limit / self.enemy_widht)):
            for y in range(4):
                enemy = Enemy((x * self.enemy_widht + self.enemy_widht / 2, -y *
                              self.enemy_height), 'Assets/enemigo1.png', self.y_limit, scale=(self.enemy_widht, self.enemy_height))
                self.enemy_group.add(enemy)

    def wave_t3(self):
        for x in range(int(self.x_limit / self.enemy_widht)):
            for y in range(4):
                enemy = Enemy((x * self.enemy_widht + self.enemy_widht / 2, -y *
                              self.enemy_height), 'Assets/enemigo2.png', self.y_limit, scale=(self.enemy_widht, self.enemy_height))
                self.enemy_group.add(enemy)

    def wave_t4(self):
        for x in range(int(self.x_limit / self.enemy_widht)):
            for y in range(4):
                enemy = Enemy((x * self.enemy_widht + self.enemy_widht / 2, -y *
                              self.enemy_height), 'Assets/enemigo3.png', self.y_limit, scale=(self.enemy_widht, self.enemy_height))
                self.enemy_group.add(enemy)
    
    def wave_t5(self):
        for x in range(int(self.x_limit / self.enemy_widht)):
            for y in range(4):
                enemy = Enemy((x * self.enemy_widht + self.enemy_widht / 2, -y *
                              self.enemy_height), 'Assets/enemigo4.png', self.y_limit, scale=(self.enemy_widht, self.enemy_height))
                self.enemy_group.add(enemy)

    def create_wave(self):
        waves = [self.wave_t1, self.wave_t2, self.wave_t3, self.wave_t4, self.wave_t5]
        if self.last_spawn >= self.wave_thresh:

            random.choice(waves)()

            self.last_spawn = 0

        pass

    def draw(self, screen):
        self.enemy_group.draw(screen)

    def update(self):
        self.create_wave()
        self.check_downs()
        self.enemy_group.update()

        self.last_spawn += 1
        pass

    def check_downs(self):
        for enemy in self.enemy_group:
            for bullet in self.bullet_group:
                if enemy.bullet_collision((bullet.rect.x, bullet.rect.y)):
                    enemy.kill()
                    bullet.kill()

    pass
