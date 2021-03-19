import pygame, colors, sys, standards, time, game_over

from pygame import Rect
from flappy import  Flappy
from scoremanager import  Scoreboard
from pipe_manager import  Pipe_manager
from  pause_screen import Pause_screen
from start_prompt_screen import  Start_prompt_screen
pygame.init()


PAUSE = False
GAME_OVER = False
HIGH_SCORE = False
RUNNING = True
CLOCK = pygame.time.Clock()
SCORE = 0
screen_height = 400
screen_width = 700
START = False


flap = Flappy(100,100)
scoreboard = Scoreboard()
pipe_manager = Pipe_manager(4, flap.rect)






def restart_game():
    global  GAME_OVER, SCORE, HIGH_SCORE, flap, START
    GAME_OVER = False
    SCORE = 0
    #START = False

    flap = Flappy(100,100)
    pipe_manager.flappy = flap.rect
    pipe_manager.clear_cache()
    HIGH_SCORE = False


def get_key(key):
    keyed = pygame.key.get_pressed()
    if keyed[key]:

        return True
    else:
        return False
def get_game_over_events():

    restart_game()
    global  GAME_OVER, SCORE, flap
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if get_key(pygame.K_r):
        time.sleep(.2)

        restart_game()

    elif get_key(pygame.K_x):
        pygame.quit()
        sys.exit()




def get_start_button():
    global START
    if get_key(pygame.K_s):
        START = True
        print(START)



def get_pause():
    global  PAUSE
    if get_key(pygame.K_ESCAPE):
        time.sleep(.1)
        PAUSE = True


def process_game_over_results():
    global GAME_OVER, HIGH_SCORE
    GAME_OVER = True
    if scoreboard.check_if_highscore(SCORE) == True:
        HIGH_SCORE = True


def get_exit():
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def get_key_press():
    global START
    # space to go up
    key  = pygame.key.get_pressed()
    if START == True and  key[pygame.K_SPACE]:

        flap.go_up()
    
def manage_pipes(window):
    global  SCORE
    pipe_manager.flappy = flap.rect
    SCORE =int(abs( pipe_manager.pipes_passed/2))

    pipe_manager.move_pipes(window)


def pipe_collision():
    global RUNNING, SCORE, GAME_OVER
    if pipe_manager.get_collision():

        print('[ YOU HIT A PIPE]')
        process_game_over_results()
    else:
        for pipe in pipe_manager.pipes_list:
            if flap.body.colliderect(pipe.rect):
                process_game_over_results()


def top_bottom_collision(flap):
    global  RUNNING, GAME_OVER
    if flap.rect.y == 0:
        process_game_over_results()
        print('[HIT THE TOP]')

    elif flap.rect.bottomleft[1] > screen_height-30:
        process_game_over_results()
        print(flap.rect.bottomleft[1])
        print('[HIT THE BOTTOM]')
        



def scoreboard_functions(screen):
    pygame.draw.rect(screen, colors.white, pygame.Rect(0,(screen_height-30), screen_width, 30))
    scoreboard.text_to_gamer(f'SCORE : {SCORE} ', (screen_width-300, screen_height- 20 ), screen, colors.midnightblue, 30)
    scoreboard.text_to_gamer(f'HIGHSCORE : {scoreboard.get_highscore()}', (screen_width-600, screen_height- 20 ), screen, colors.midnightblue, 30)

def  pause_events():
    global  PAUSE
    if get_key(pygame.K_ESCAPE):
        time.sleep(.1)
        PAUSE = False

def all_events(window):
    # handles all events during game
    manage_pipes(window)
    flap.show(window)
    flap.gravity()
   
    get_exit()
    get_key_press()
    get_pause()
    top_bottom_collision(flap)
    pipe_collision()



class Game:
    def __init__(self):
        self.running = True
        self.pause = PAUSE
        self.game_over = GAME_OVER
        self.START = START
        self.screen = pygame.display.set_mode((screen_width, screen_height))

    def run(self):
        global  SCORE, GAME_OVER,START, PAUSE

        while self.running == True:

            pygame.display.flip()
            pygame.display.set_caption('                                                           FLAPPY ')
            self.game_over = GAME_OVER
            self.pause = PAUSE
            self.START = START
            START = self.START
            if self.game_over == False:


                if self.pause == False:

                    self.screen.fill(colors.test_white)
                    screen = self.screen
                    # ''''''''''''''''''''''''

                    if self.START == True:


                        all_events(screen)
                        scoreboard_functions(screen)
                        # ''''''''''''''''''''''''''''##

                        pygame.display.update()
                        CLOCK.tick(40)
                    elif self.START == False:
                        Start_prompt_screen().run()
                 
                        get_start_button()


                elif self.pause ==True:

                    Pause_screen().run(SCORE)
                    pause_events()

            elif self.game_over == True:


                endgame_result =  ' N E W   H I G H S C O R E' if HIGH_SCORE  == True else  'L O S E R'

                game_over.Game_over_screen(SCORE,endgame_result).run()
                get_game_over_events()
                time.sleep(1)
                GAME_OVER = False
                print(SCORE)
if __name__ == '__main__':
    Game().run()
