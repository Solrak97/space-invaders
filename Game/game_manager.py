import pygame as pg
from game import Game

# Setup
SCREEN_SIZE = (640, 480)
FPS = 60

pg.init()

clock = pg.time.Clock()
icon = pg.image.load('Assets/green.png')
pg.display.set_caption('Space Invaders')
pg.display.set_icon(icon)

screen = pg.display.set_mode(SCREEN_SIZE)
pg.mixer.music.load("music.wav")
pg.mixer.music.play()

       
game = Game(screen, SCREEN_SIZE, clock, FPS)
game.human_game_loop()