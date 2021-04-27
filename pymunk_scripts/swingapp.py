import pygame
from app import App

from swing import Swing
from ball import Ball
from box import EnclosedBox


app = App(name = "Swing animation", SIZE = (500,500))

Swing(app.space, (250,0), (200,200))
Ball(app.space, 250,0, 30  , elasticity = .7)
EnclosedBox(app.space,0,0,500,500,color = pygame.Color("blue"))


app.run()
