import pygame, standards,  colors, time
from scoremanager import  Scoreboard



class Game_over_screen:
    def __init__(self, score, message):
       self.score = score
       self.results_message = message
       self.restart_message = '    R    T O   R E S T A R T'
       self.quit_message = '   X    T O     E X I T'
       pass


    def run(self):
        screen = pygame.display.set_mode((standards.screen_width, standards.screen_height))
        screen.fill(colors.white)
        Scoreboard().text_to_gamer('G A M E    O V E R ', (180, 59), screen, colors.red, 50)
        Scoreboard().text_to_gamer(self.results_message, (210, 100), screen, colors.yellow, 50)
        Scoreboard().text_to_gamer(f'SCORE  :   {self.score}', (260, 150), screen, colors.black, 30 )
        Scoreboard().text_to_gamer(f'{self.quit_message}', (250, standards.screen_height/2), screen, colors.purple, 20)
        Scoreboard().text_to_gamer(f'{self.restart_message}',
                                   (230, standards.screen_height / 2 + 40), screen, colors.midnightblue,
                                   20)
        pygame.draw.rect(screen, colors.red, pygame.Rect(50, 50, standards.screen_width-100, standards.screen_height- 100 ), 2)
        pygame.display.update()
        pygame.time.Clock().tick(10)
