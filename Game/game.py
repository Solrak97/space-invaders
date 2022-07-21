import sys
from enemy_manager import EnemyManager
from player import Player
import pygame as pg


class Game():
    def __init__(self, display, display_size, clock, fps, is_human=False):
        # Game settings
        self.display = display
        self.display_size = display_size
        self.clock = clock
        self.fps = fps
        self.is_human = is_human

        self.player_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.bullet_group = pg.sprite.Group()


        # Enemy manager
        self.enemy_manager = EnemyManager(self.enemy_group, self.bullet_group)


        # Player setup
        self.player = Player((self.display_size[0] / 2, 460), 'Assets/jugador.png', self.bullet_group)
        self.player_group.add(self.player)


        # Score
        self.score = 0

        

    # Graphics update
    def draw_state(self):
        self.enemy_manager.draw(self.display)
        self.player_group.draw(self.display)
        self.bullet_group.draw(self.display)



    # Internal game object state update
    def update_state(self):
        self.enemy_manager.update()
        self.player_group.update()
        self.bullet_group.update()


    # Game logic goes brrrr
    def human_game_loop(self):
        while not self.enemy_manager.enemy_trespasses():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.display.fill((0, 0, 0))
            self.draw_state()
            self.update_state()
            
            pg.display.flip()
            self.clock.tick(self.fps)

    
    def ai_gameloop(self, model):
        while not self.enemy_manager.enemy_trespasses():
            self.display.fill((0, 0, 0))

            # Captura del estado como imagen

            # Petición de predicción

            # Actuador sobre la petición

            # Calculo de la recompensa

            self.draw_state()
            self.update_state()
            
            pg.display.flip()
            self.clock.tick(self.fps)
        pass