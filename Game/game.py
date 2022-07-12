import pygame as pg
import sys

from enemy_manager import EnemyManager
from player import Player

# Setup
SCREEN_SIZE = (640, 480)
FPS = 60

pg.init()

clock = pg.time.Clock()
icon = pg.image.load('Assets/green.png')
pg.display.set_caption('Space Invaders')
pg.display.set_icon(icon)

screen = pg.display.set_mode(SCREEN_SIZE)


# Gameobject Groups
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()

# Enemy manager
enemy_manager = EnemyManager(enemy_group, bullet_group)

# Player setup
# Fix player pos and movement bugs
player = Player((SCREEN_SIZE[0] / 2, 460), 'Assets/jugador.png', bullet_group)
player_group.add(player)



# Graphics update, kinda like a global draw
def draw_state():
    enemy_manager.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)


def update_state():
    enemy_manager.update()
    player_group.update()
    bullet_group.update()


# Gameloop
while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    draw_state()
    update_state()

    pg.display.flip()
    clock.tick(FPS)