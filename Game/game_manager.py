import pygame as pg
from game import Game
from agent import Agent

# Setup
SCREEN_SIZE = (640, 480)
FPS = 60

pg.init()

clock = pg.time.Clock()
icon = pg.image.load('Assets/green.png')
pg.display.set_caption('Space Invaders')
pg.display.set_icon(icon)

screen = pg.display.set_mode(SCREEN_SIZE)
pg.mixer.music.load("Assets/music.wav")
pg.mixer.music.play()


# Creación del modelo
agent = Agent()   

game = Game(screen, SCREEN_SIZE, clock, FPS, is_human=False, agent=agent)

game.gameloop()