import pygame, standards, scoremanager, colors, time

class Pause_screen:
    def run(self, score):
        screen = pygame.display.set_mode((standards.screen_width, standards.screen_height))
        screen.fill(colors.skyblue)
        scoremanager.Scoreboard().text_to_gamer(f'SCORE : {score}', (200, 100), screen, colors.goldenrod,30 )
        scoremanager.Scoreboard().text_to_gamer(f'ESCAPE  to resume', (200, 200), screen, colors.goldenrod,30)
        pygame.draw.rect(screen, colors.yellow, pygame.Rect(50, 50, standards.screen_width - 100, standards.screen_height - 100), 2)
        pygame.display.update()



