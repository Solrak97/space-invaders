import pygame as pg

from enemy import Enemy

class EnemyManager:

    def __init__(self, enemy_group, bullet_group):
        self.enemy_group = enemy_group
        self.bullet_group = bullet_group

        
        # Spawntime
        self.last_spawn = 0
        self.wave_thresh = 120

        pass


    def wave_t1(self):

        # Refactorizar la generación de enemigos
        e1 = Enemy((100, 0), 'Assets/enemigo0.png')
        e2 = Enemy((200, 0), 'Assets/enemigo1.png')
        e3 = Enemy((300, 0), 'Assets/enemigo2.png')
        e4 = Enemy((400, 0), 'Assets/enemigo3.png')
        e5 = Enemy((500, 0), 'Assets/enemigo4.png')

        self.enemy_group.add(e1)
        self.enemy_group.add(e2)
        self.enemy_group.add(e3)
        self.enemy_group.add(e4)
        self.enemy_group.add(e5)

        pass

    def wave_t2(self):
        pass

    def wave_t3(self):
        pass

    def wave_t4(self):
        pass

    def wave_t5(self):
        pass

    def create_wave(self):
        if self.last_spawn >= self.wave_thresh:
            self.wave_t1()
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