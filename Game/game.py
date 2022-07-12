import pygame as pg
import sys

from enemy import Enemy
from player import Player

SCREEN_SIZE = (640, 480)
FPS = 60

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_SIZE)




# Refactorizar la generación de enemigos
e1 = Enemy((100, 200), 'Assets/orange.png')
e2 = Enemy((200, 200), 'Assets/green.png')
e3 = Enemy((300, 200), 'Assets/purple.png')
e4 = Enemy((400, 200), 'Assets/red.png')
e5 = Enemy((500, 200), 'Assets/yellow.png')


enemy_group = pg.sprite.Group()
enemy_group.add(e1)
enemy_group.add(e2)
enemy_group.add(e3)
enemy_group.add(e4)
enemy_group.add(e5)



# Refactorizar la generación de player
player = Player((240, 300), 'Assets/player.png')
player_group = pg.sprite.Group()
player_group.add(player)


# Graphics update, kinda like a global draw
def draw_state():
    enemy_group.draw(screen)
    player_group.draw(screen)


# Gameloop
while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    draw_state()
    
    player.update()
    pg.display.flip()
     
    clock.tick(FPS)