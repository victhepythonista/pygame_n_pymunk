import pygame, colors, standards, scoremanager


class Start_prompt_screen:
    def __init__(self):
        pass

    def run(self):
        screen = pygame.display.set_mode((standards.screen_width, standards.screen_height))
        screen.fill((12,100,201))
        scoremanager.Scoreboard().text_to_gamer('S to start', (200,200), screen, colors.dark_olive_green, 30)