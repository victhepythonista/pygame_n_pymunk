######m a  simple  road   crossing  game
###  just  dont  let the poor squirell get   crushed!!!!!!!!!!!!
# enjoy ! I guess
##############################################################
about_game = """                          Just   use [W ,S, A , D] keys cross the  road   nothing much!"""
about_dev = """                           victhepythonista@github.com      | letingvictorkipkemboi@gmail.com  |  0715893772"""

import time , sys


import pygame
try:
    import pygame._view
except:
    pass
import backend
import draw_roads
import random

from backend import text_to_gamer  , update_screen
running = True
highscore_file = 'highscore.txt'
screen_width  = 1000
screen_height  = 700
high_score_file  = 'highscore.txt'
fps  = pygame.time.Clock()
LEVEL  = 1
GAME_OVER = backend.GAME_OVER
GAME_PAUSED  = backend.GAME_PAUSED
START = False
backend.make_data_csv('highscore.txt')
HIGHSCORE = backend.get_highscore(high_score_file)
LIVES = 1


###  colors
chocolate = (210,105,30)
grey  = (119 ,136 ,153)
orangered = (205, 55,0)
forestgreen = (34,139,39)
white = (255,255,255)
skyblue  = (126, 192 ,238)
dark_olive_green  = (162, 205 ,90)
light_salmon  = (255, 160, 122)
red  =  (200,  0  ,  0)
green= (0,255,0)
blue = ( 0, 0,250)
purple = (102, 0 ,102)
black = (0,0,0)
yellow = (255,255,0)
goldenrod = (25  ,193, 37)
midnightblue = (0,0, 156)
wheat = (255 ,231 ,186)
khaki = (205 ,198 ,115)
colors_list= [chocolate , forestgreen , skyblue  , blue   , purple  , yellow , goldenrod  , midnightblue , red  , light_salmon , dark_olive_green]

##############################
## GAMEPLAY   VARIABLES  #########
################################
truck_speed  = 5
saloon_car  = 7
pickup  = 5
LEVEL_BACKGROUND  = grey
LEVEL_FACTOR = 1
SCORE  = 0
background_color_list  = [grey , wheat  , khaki ]
DYNAMIC_SPEED = LEVEL/100 *  200
####
squirrell  =  backend.Croos(screen_width/2 , screen_height-100  , 4   , 4)

number_of_lanes  = 6





def main_window():
    
    game_window = pygame.display.set_mode((screen_width  , screen_height))
    pygame.display.update()
    pygame.init()


##################### pickups  cariables
points_for_pickups  = [30  , 130  , 230  , 430  , 530  , 630  ]



pickups = {'lane1':[]  ,
           'lane2':[],
           'lane3':[],
           'lane4':[],
           'lane5':[],
           'lane6':[]}

################ LANES
                 # parameters  for  lanes ________  # pos_y  , lane_direction   , screen_width  , cars_list  , window  , interval
lane1  = backend.Lane(130 , 'left', screen_width,   pickups['lane1'] ,None , 700 )
lane2 =  backend.Lane(230 , 'right', screen_width,   pickups['lane2'] ,None , 700)
lane3  =  backend.Lane(330 , 'left', screen_width,   pickups['lane3'] ,None , 600 )
lane4  = backend.Lane(430  , 'right'  , screen_width   , pickups['lane4'] , None , 700)
lane5  =  backend.Lane(530 , 'left', screen_width,   pickups['lane5'] ,None , 700 )
#lane6  = backend.Lane(530  , 'right'  , screen_width  , pickups['lane6']  , None  , 120)


lanes_list  = [lane1 ,
               lane2,
               lane3 ,
               lane4 ,
               lane5 ]




def  get_squirell_collison(other_rect):
    ## we get  collisions  of  the  squirell
    # with  other objects
    global  running
    hitbox  = squirrell.rect


    if hitbox.colliderect(other_rect):
        ## if  there is  a collision  we  return True

        print('[  COLLISION    ]')

        return True
    else:
        return False








def get_exit():
    ## we  exit   if  the user  exists
    for ev  in pygame.event.get():
        if ev.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()


def get_startkeys(window):
    ### gets  key  presses  from start  window
    global START
    pygame.init()
    key  =  pygame.key.get_pressed()
    if key[pygame.K_s]:
        START = True
    elif key[pygame.K_q]:
        pygame.quit()
    elif key[pygame.K_a]:
        text_to_gamer(about_game , (200 , 500) , window , black , 40)
        pass
def initiate_movements():

     global GAME_PAUSED
     button  = pygame.key.get_pressed()
     if button[pygame.K_ESCAPE]:
         ## escape  to pause game
         GAME_PAUSED = True
         time.sleep(.5)




     ### get   left and  right  keys
     if button[pygame.K_d]  and ((squirrell.x+ 90) < screen_width):
         squirrell.move_right = True
     elif button[pygame.K_a]  and squirrell.x  >  0 :
         squirrell.move_left = True

 ####3  get  up  and  down  keys
     if button[  pygame.K_w]   and  squirrell.y > 0 :
        squirrell.move_up  = True
     elif button[  pygame.K_s]  and squirrell.y + squirrell.height+ 10 < screen_height :
        squirrell.move_down = True

def  get_random_color(list):
    index = random.randrange(0 , len(list) - 1)
    #print(f'GETTING  RANDOM  COLOR  FROM       {list}')
    return  colors_list[index]
    pass


def get_random_background():
    ### get  a rrandom  colour  for  the  background
    #  when  changing  levels
    background_color = [wheat  , grey  , khaki]
    index = random.randrange(0 ,len(background_color) - 1)
    return background_color[index]
    pass

def get_all_events():
    ##  getting  the  general  events  , like  quiting
    ## common in  different  screens
    
    get_exit()

def process_lanes(window):
    ##  manages   moving  of  vehicles   on the  lanes  and  handles  the  collisions
    global  SCORE
    global LIVES
    for lane in lanes_list:

        for car in lane.cars_list:


            if get_squirell_collison(car.rect)  == True:
                ##  check  for  collisions
                if car.type == 'acorn':
                    LIVES += 1
                    lane.cars_list.pop(lane.cars_list.index(car))
                elif car.type == 'pickup':
                    LIVES -= 1
                    if LIVES > 0:
                        lane.cars_list.pop(lane.cars_list.index(car))
                    else:
                        HIGHSCORE = backend.get_highscore('highscore.txt')
                        backend.check_new_highscore(LEVEL)
                        new_game(window)
                        




        lane.window = window

        lane.interval = random.randrange(150  , 300 )
        if len(lane.cars_list) == 0:

            lane.cars_list.append(backend.Vehicle(screen_width if lane.direction == 'left' else 0
                                                  , lane.pos_y,
                                                  DYNAMIC_SPEED
                                                  ,
                                                  'pickup'
                                                  , lane.direction,
                                                  get_random_color(colors_list)))
        if len(lane.cars_list) <  10:
            if random.randrange(0,15)  == 12:
                lane.cars_list.append(backend.Acorn( lane.cars_list[-1].x + lane.interval  if lane.direction == 'left'  else lane.cars_list[-1].x - lane.interval ,
                                                                                                                                lane.pos_y  ,
                                                                                                                               random.randrange(1,2)*LEVEL_FACTOR ,
                                                                                                                               'acorns/choconut.png' ,

                                                                                                                               lane.direction,
                                                                                                                            'acorn'))

            else:
                lane.cars_list.append(backend.Vehicle(  (   lane.cars_list[-1].x + lane.interval ) if lane.direction == 'left'  else (lane.cars_list[-1].x - lane.interval),
                                                   lane.pos_y,
                                                  DYNAMIC_SPEED,
                                                  'pickup'
                                                  , lane.direction ,
                                                    get_random_color(colors_list)))


        lane.manage_traffic()

    pass


def reset_game(window):
    ####  resets  the  game   ,,  [  for   game  over]
    for lane in lanes_list:
        lane.cars_list = 0

    LEVEL_FACTOR = 1

    squirrell.x = screen_width / 2
    squirrell.y = 0







def  score_manager(window):

    ## LEVEL
    text_to_gamer(f'LEVEL : {LEVEL}', (screen_width - 400, screen_height - 30),
                  window,
                  green,
                  20)
    ## SCORE
    text_to_gamer(f'HIGHSCORE : {backend.get_highscore(highscore_file)}', (screen_width-200,screen_height-30)  ,
                 window ,
                   blue ,
                  20)
    text_to_gamer(f'LIVES   : {LIVES}', (screen_width -600 , screen_height - 30),
                  window,
                  red,
                  20)
def animate_car(window):
    ###  animates   car  motion
    process_lanes(window)
    pass



def animate(window):
    ### handles  all animations
    squirrell.forage_for_nuts(window)
    animate_car(window)

    ##displlay  score
    score_manager(window)
    ###############################
    #######################
    ###################
    ####################


def  get_events_paused():

    global  GAME_PAUSED
    ##  gets  key presses  when  game  is  paused


    key   = pygame.key.get_pressed()
    if key[pygame.K_q]:
        pygame.quit()
    elif key[pygame.K_ESCAPE]:
        GAME_PAUSED = False
        print('[ RESUMING  GAME ]')
        time.sleep(.5)

def smashed_screen(window):
    global GAME_OVER
    ###  when you get  hit
    if GAME_OVER == True:
       # window  = pygame.display.set_mode((screen_width - 200 , screen_height))

        window.fill(white)
        text_to_gamer('GAME OVER', (screen_width/3, 100), window, orangered, 70)
        text_to_gamer(f'LEVEL  : {LEVEL}'  , (screen_width/3  , 200)  , window , black , 60 )
        text_to_gamer('restarting........', (screen_width/3, 400), window, yellow, 40)
        pygame.display.update()
        update_screen()
     


def paused_game_screen(window):
    pygame.init()
    info_pos_x = 100

    update_screen()
    window.fill(orangered)
    get_events_paused()
    text_to_gamer('GAME PAUSED'  , (info_pos_x  ,  30)  , window  , midnightblue  , 60)
    text_to_gamer('RESUME: press ESC' , (info_pos_x , 500) , window  , black , 30)
    text_to_gamer('EXIT : press  Q', (info_pos_x, 560), window, black, 30)

def crossed_road():
    global  LEVEL , LEVEL_BACKGROUND , colors_list
    ## checks  if  croos  crossed  the  road  and   starts  a new  level
    if squirrell.y < 100:
        print(f'[   NEW  LEVEL  STARTING.....] [  {LEVEL}]')
        LEVEL+= 1
        squirrell.y = screen_height-40
        LEVEL_BACKGROUND =get_random_background()
        for lane in lanes_list:
            lane.cars_list = [backend.Vehicle( random.randrange(200 , 700) ,
                                               lane.pos_y  ,
                                               DYNAMIC_SPEED ,
                                               'pickup'  ,
                                               lane.direction ,
                                               get_random_color(colors_list) )]
        print(f"[ STARTING  NEW  LEVEL ] \n [background color]  :  {LEVEL_BACKGROUND}")




def new_game(window):
    ### restarts  a  new  game
    global GAME_OVER  , LIVES
    GAME_OVER = True
    LIVES = 0
    #smashed_screen(game_window)
    global  LEVEL , LEVEL_BACKGROUND

    squirrell.x , squirrell.y =screen_width/2  , screen_height-40
    for lane  in lanes_list:
        lane.cars_list = []
        LEVEL  = 1
        print(background_color_list)
        LEVEL_BACKGROUND = grey
        print(f'[ backround color  new  game ::: {LEVEL_BACKGROUND }]')

    time.sleep(.1)
    pass
########################
## pause  game screen
def paused_game(window):

    paused_game_screen(window)
    get_exit()
def start_window():
    start_screen  = pygame.display.set_mode((screen_width , screen_height))
    start_screen.fill(light_salmon)
    text_to_gamer('START : press S' , (300,100) , start_screen  , black  , 40)
    text_to_gamer('EXIT : press Q', (300, 200), start_screen, red, 40)

    text_to_gamer(about_game, (0, 500), start_screen, black, 13)
    text_to_gamer(about_dev, (0, 600), start_screen, midnightblue, 12)

    update_screen()
    get_exit()
    get_startkeys(start_screen)




    pass

def game_loop():
    global game_window , GAME_OVER
    pygame.init()
    global  game_window
    while running :
        pygame.init()
        if START:
            if GAME_OVER:

                smashed_screen(game_window)

                print('[  GAME  OVER ]')
                GAME_OVER = False
            elif GAME_PAUSED == False:


                game_window  = pygame.display.set_mode((screen_width  , screen_height))
                game_window.fill(LEVEL_BACKGROUND)

                pygame.display.set_caption('CROOS ROAD')

                initiate_movements()
                # we get characters m0vements

                animate(game_window)

                get_all_events()


                fps.tick(40)
                # frames  per  second
                backend.draw_lanes(game_window)

                crossed_road()
                ###checks  if  squirell has  crossed  the  road hence
                #start  a new level

                animate(game_window)

                pygame.display.update()


                pygame.display.flip()

                backend.make_data_csv('highscore.txt')

                pass

            else:
                paused_game(game_window)

        else:
            start_window( )

if __name__ == '__main__':
    game_loop()
