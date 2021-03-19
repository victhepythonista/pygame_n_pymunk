##  backend  functions   and  classes
import pygame
import os
import draw_roads

from pygame import Rect

chocolate = (210,105,30)
forestgreen = (34,139,39)
red= (255,0,0)
green= (0,255,0)
blue = ( 0, 0,250)
purple = (102, 0 ,102)
black = (0,0,0)
yellow = (255,255,0)
goldenrod = (25  ,193, 37)
midnightblue = (0,0, 156)
white = (255,255,255)
grey  = (119 ,136 ,153)

GAME_OVER = False
GAME_PAUSED  = False
highscore_file = 'highscore.txt'

home_dir  = os.path.dirname(os.path.abspath(__file__))


class Acorn:
    ## the  acorn  class
    ##  givess  you one  extra life
    
    def __init__(self  , x  , y   ,speed  ,  image , direction , type):
        self.type = type
        self.x  = x
        self.speed  = speed
        self.y  =  y
        self.direction  = direction
        self.image  =pygame.image.load(image)
        #self.image_size  = Image.open(image).size
        self.rect   = Rect(self.x  , self.y    ,30 , 30 )
    def show(self  , window):
        ##  show the acorn on the screen
        window.blit(self.image  , (self.x,self.y))
        self.rect = Rect(self.x, self.y, 30, 30)

    def  move(self):
        ##  initiates  and  directs  movements
        if self.direction == 'left':

            self.x -= self.speed
        elif self.direction   == 'right':
            self.x  += self.speed





    pass

class Lane():
    def __init__(self , pos_y  , lane_direction   , screen_width  , cars_list  , window  , interval  ):
        self.pos_y  = pos_y
        self.direction  = lane_direction
        self.cars_list = cars_list
        self.window  = window
        self.screen_width  = screen_width
        self.interval = interval
    def manage_traffic(self):
        for car in self.cars_list:

            if self.direction == 'left':
                car.move()
                car.show(self.window)
                if car.x  < -100:
                    self.cars_list.pop(self.cars_list.index(car))




                pass
            elif self.direction =='right':

                car.move()
                car.show(self.window)
                if car.x > self.screen_width:
                    self.cars_list.pop(self.cars_list.index(car))
                pass


class Croos():
    #  CHARACTER CLASS

    def __init__(self, x, y, vel  , up_vel):
        self.nutken_list = [pygame.image.load(  'characters/squirell_facing_right.png'),
                            pygame.image.load('characters/squirell_facing_left.png')]
        self.vel = vel
        self.allow_to_move = True
        self.x = x
        self.y = y
        self.up_vel  = up_vel
        self.movement_images = []
        self.width = 20
        self.height = 60
        self.squirrel_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.move_right = False
        self.move_left = False
        self.move_up  = False
        self.move_down = False
        self.forage_count = 0
        self.pos = (self.x - 25, self.y - 20)
        self.image  = self.nutken_list[self.forage_count]
        self.image_rect = Rect(self.image.get_rect())
        self.rect  = Rect(self.x  , self.y  , self.image_rect.width  , self.image_rect.height)
    def forage_for_nuts(self, window):

        self.rect = Rect(self.x, self.y, self.image_rect.width, self.image_rect.height)

        #window.blit(self.nutken_list[self.forage_count], self.rect)
        window.blit(self.nutken_list[self.forage_count] , (self.x , self.y))



###  moving left and right
        if self.move_left == True:
            self.move_right = False
            self.x -= self.vel
            self.move_left = False
            self.forage_count = 1
            self.pos = (self.x - 25, self.y - 20)
        elif self.move_right == True:

            self.move_left = False
            self.move_right = False
            self.x += self.vel

            self.pos = (self.x - 39, self.y - 20)
            self.forage_count = 0



######   moving  up  and down
        if self.move_down== True:
            self.move_up = False
            self.y += self.vel
            self.move_down = False

        elif self.move_up== True:

            self.move_down = False
            self.move_up = False
            self.y-= self.vel




    def get_current_hitbox(self):
        return self.nutken_list[self.forage_count].get_rect()



class Vehicle():
    def __init__(self  , x ,y , speed  , type  , direction , color):

        self.x = x
        self.y  = y
        self.speed = speed

        self.type  = type
        self.direction  = direction
        self.color = color
        self.width  = 70
        self.height  = 40
        self.rect = pygame.Rect(self.x  , self.y  , self.width  , self.height)


    def show(self  , window  ):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.type  == 'pickup':
            rect_car  = pygame.Rect(self.x  , self.y , self.width  , self.height)

            #      DRAWING  TIRES
            pygame.draw.circle(window  ,
                               black,

                               (rect_car.topleft[0]+10,rect_car.topright[1]),
                               5,
                               0)
            pygame.draw.circle(window  , black,
                               (rect_car.topright[0]-12 , rect_car.topright[1]),
                              5,
                               0)
            pygame.draw.circle(window, black,
                               (rect_car.topleft[0] + 10, rect_car.bottomleft[1]),
                               5,
                               0)
            pygame.draw.circle(window, black,
                               (rect_car.topright[0] -12, rect_car.bottomright[1]),
                               5,
                               0)

            # CAR BODY


            pygame.draw.rect(window , self.color ,rect_car)

            # WINDOWS  AND  EXHAUST

            #windscrreen
            #dpygame.draw.polygon(window  , black  , [] , 0)

    def  move(self):
        if self.direction == 'left':

            self.x -= self.speed
        elif self.direction   == 'right':
            self.x  += self.speed
    pass




##############################################
################################################
########                ###########################
######## L E V E L  S  ########
########                ######
#########################
########################
def create_file(name):
    ### ___creates file if it doesnt exist

    try:

        file = open(name, 'r')
        print('file  exists......')
        file.close()
        return True

    except:
        file = open(name, 'w')
        file.close()
        return False

## default  values of scores and levels
data  = """
data,value
highscore,0
paused,0
running,1
"""
dir = os.getcwd()
filepath = os.path.join(os.getcwd(), 'highscore.txt')
def make_data_csv(filepath):

    




    if os.path.isdir(dir):
        if os.path.isfile(filepath):
            pass
        else:

            create_file(filepath )
            with open(filepath , 'w')  as data_file:
                data_file.write('0')
    else:

        os.makedirs(dir)





def get_highscore(file_name):
    with open(file_name  , 'r') as  highscore_file:
        return(int(highscore_file.read()) )
    pass
def draw_dotted_line(points , length):
    length_of_dots  = 5
    number_of_dots  = length ,length_of_dots
    for point  in points:
        pass

def  check_new_highscore(score ):
    high = get_highscore(highscore_file)
    make_data_csv('highscore.txt')
    print(f'[    your  score : {score}  ]')
    print(f'[  HIGHSCORE   {high}]')
    if  score > high:
        print(['\nNEW    HIGHSORE \n '])
        with open(highscore_file  , 'w')  as data_file:
                data_file.write(str(score))
    else:
        print('[  sorry NOT  A NEW  HIGHSCORE  ]')
                
                
                
def  get_points_to_draw_lines(length  , points):
    points_list = []

    interval   =  length/points
    p  = 0
    for  point  in  range(points ):
        points_list.append(p)
        p  += interval
    #points_list.append(p+ interval+interval)
    return points_list


    pass

def draw_lanes(window):
    ##  this  function  draws  the  lanes   on   the  screeen
    lanes  = 7
    width  = 1000
    height  = 700

    interval  =  height/lanes



    points = get_points_to_draw_lines(height , lanes)
    for line  in points:
        ## drawing  lane  line
        if points.index(line)  == -1:
            continue
        draw_roads.Line(0  , line , width  , 2).draw_line(window , black)




def update_screen():
    ###  basic  screen  refresh
    pygame.display.update()

    pygame.display.flip()

def  text_to_gamer(message,position,window,color,fontsize):
    ###   displays   text  on the  screen
    pygame.font.init()
    mess_obj = pygame.font.SysFont('Consolas',fontsize)
    mess_render = mess_obj.render(message,10,color)
    window.blit(mess_render,position)



###########################################################################################################
###############################################################################################
##############                   OTHER  SCREENS                               #######################
######################################################################





