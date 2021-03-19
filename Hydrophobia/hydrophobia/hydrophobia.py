



#############################
########################################################
#_______________thIS IS A GAME DEVELOPED BY LETING vICTOR KIPKEMBOI




import pygame
from  pygame import event,quit , QUIT
import sys
import random
import time,os


def create(file):
    if os.path.isfile(file):
        pass
    else:
        with open(file , 'w') as f:f.close() 
    

#### THis  function  displays the name of the game and icon
def  set_name():
    #___this sets the name of a screen and icon title
    pygame.display.set_caption ('HYDROPHOBIA'  )
    pygame.display.set_icon(pygame.image.load  (  'hydrophobia/ball.png'  )  )

new_highscore  =False
game_paused = False
start_game  = True
def  enter_score( file , score):



    #######creates file if it doesnt exist
    write_if_not_exist(file)
   ################writes score  to file
    b = open(file, 'w')
    b.write(str(score))
    b.close()


file = 'hydrophobia/highscore.txt'
create(file)
HIGHSCORE =0






pygame.init()
game_state= True
chocolate = (210,105,30)
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
block_colors = [yellow , green  , midnightblue]
SCORE  = 0
block_list =[]


screen_width = 500
screen_height = 700
frame = pygame.time.Clock()
game_speed=  4



def  text_to_gamer(message,position,window,color,fontsize):
    #### _this function  writes  a message to the user
    pygame.font.init()
    mess_obj = pygame.font.SysFont('Consolas',fontsize)
    mess_render = mess_obj.render(message,10,color)
    window.blit(mess_render,position)
class pong_ball():

    def __init__(self , speed , pos ):
        self.speed  = speed
        self.hit  = False

        self.image   = pygame.image.load('hydrophobia/ball.png')

        self.image_rect  =  self.image.get_rect()
        self.image_rect.center= (pos)





        pass
    def move(self , window):
        window.blit(self.image  , self.image_rect)
        self.image_rect = self.image_rect.move(self.speed)



    def show(self,  window):





        window.blit(self.image,self.image_rect)


    def wall_collision(self):

        global SCORE
        #####collision with walls
        if self.image_rect.left < 0 or self.image_rect.right > screen_width:
            self.speed[0] = -self.speed[0]
        elif  self.image_rect.bottom > screen_height - 60:
            SCORE += 1
            ball_control()


            self.hit = True


        pass


speed = [7,7]

def write_if_not_exist(file):
    try:
        new = open(file, 'r')
    except:
        with open(file, 'w') as f:
            f.write('0')
            f.close()
    new = open(file, 'r')

    if new.read()=='':
        new.close()
        new_agin  = open(file, 'w')

        new_agin.write(str(0))
        new_agin.close()
    else:
        new.close()

def get_highscore():
    write_if_not_exist(file)
    o  = open(file ,'r')
    data  = o.read()
    o.close()
    print('hiiiighscore  is.........' +    data)
    return data
origin_time = time.time()



class level():


    def __init__(self):

        self.life  = 5


        self.highscore  = get_highscore()


        self.text_color  = black
        self.current_level  = 1
        self.game_speed = 3
        self.bg_color=  goldenrod
        self.original_time  = time.time()
        self.next_level  = 100
        self.color_list  = [goldenrod , green  , black  , skyblue , dark_olive_green ,light_salmon  ]
        self.color_index  = len(self.color_list)
        self.splash_image  =  pygame.image.load('hydrophobia/splash.png')
    def splash(self, window,pos):
        time.sleep(0.01)
        window.blit(self.splash_image,pos)
    def level_check(self):


        if self.life <= 0 :
            self.game_over()
        if  SCORE > self.next_level:
            self.next_level += 100
            self.current_level += 1
            color_no  = random.randrange(0,self.color_index - 1 )
            self.bg_color  = self.color_list[color_no]
    def game_resumed(self):
        global game_paused
        game_paused =  False
    def game_paused(self):
        global game_paused
        game_paused = True

        pass

    def game_over(self):


        global   gameover , new_highscore , SCORE


        the_f = get_highscore()

        if int(the_f) < SCORE :
            print('N E W    H I G H S C O R E !!!!')
            new_highscore = True

            filehigh2 = open(file ,'w')
            filehigh2.write(str(SCORE))

            enter_score(file, SCORE)
        SCORE = 0


        gameover = True
        self.current_level  = 1

        self.next_level = 100
        self.life = 3
        self.game_speed =3
        the_file = open(file, 'r')
        the_f = the_file.read()
        print(the_f)
        self.highscore = the_f
        the_file.close()



    pass
level  = level()

class  box():
    def __init__(self,x,y):
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(x,y , self.width,self.height)
        self.touched  = False

        self.color  = midnightblue

        pass


    def show_box(self, window) :
        mouse_pos=pygame.mouse.get_pos()

        if  mouse_pos[0] > self.width/2   and mouse_pos[1] > self.width/2  and mouse_pos[0] < screen_width - self.width/2  and  mouse_pos[1] < (screen_height - 60) - self.width/2 :



            self.rect.center = pygame.mouse.get_pos()
            if self.touched  == True :

                self.color = purple

                self.rect.center = pygame.mouse.get_pos()
            elif self.touched ==False:
                self.color = midnightblue


        pygame.draw.rect(window  ,self.color, self.rect , 0)
        pass
player  = box(screen_width/2 , screen_height/2 )







def player_activities(screen):
    player.show_box(screen)


def ball_activity(ball , screen):
    level.level_check()
    if ball.hit  == False:
        ball.wall_collision()
        ball.move(screen)
    if ball.hit== True:
        ball_list.pop(ball_list.index(ball))

ball_list  = []


###################################################
###########################################
################### G A M E       P A U S E D     S C  R  E  E  N  #######################
######################################
def GAME_PAUSED():
    global game_paused, screen_game_paused



    screen_game_paused= pygame.display.set_mode((screen_width,screen_height))
    set_name()
    screen_game_paused.fill(white)
    key_pressed = pygame.key.get_pressed()
    text_to_gamer('press SPACE to resume   ', (100,90),screen_game_paused,black,20)
    text_to_gamer('press Q to exit   ', (100, 150), screen_game_paused, goldenrod, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if key_pressed[pygame.K_SPACE]:
            screen_game_paused = None
            level.game_resumed()

            print('resuming')
            break
        
        if key_pressed[pygame.K_q]:
            sys.exit()

     ############################################### S T A R T   M E N U S C R E E N###########
            ###########################
            ########################################################################
 ##################################################################################################################################
show_about = False
def  START_MENU():
    global start_game

    start_menu_screen  = pygame.display.set_mode((screen_width,screen_height))
    set_name()
    start_menu_screen.fill(white)
    text_to_gamer('press SPACE  to  start', (50, 100), start_menu_screen, black, 20)
    text_to_gamer("""press  A    for  ABOUT GAME and C  to close """  ,  (0,200) , start_menu_screen , goldenrod,20)
    global show_about
    about_color  = midnightblue

    if show_about == True:
        pygame.draw.rect(start_menu_screen,midnightblue,pygame.Rect(20,220,50,50),0)
        text_to_gamer('USE THE MOUSE TO MOVE THE BLUE BOX',(10,350) , start_menu_screen,about_color,15)

        text_to_gamer('DEVELOPER.............Leting Victor Kipkemboi',(10,450) , start_menu_screen,black,15)
        text_to_gamer('EMAIL..................letingvictorkipkemboi@gmail.com',(10,470) , start_menu_screen,black,15)
        #text_to_gamer('CONTACT................0715893772', (10, 460), start_menu_screen, green, 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_pressed  = pygame.key.get_pressed()
    if key_pressed[pygame.K_SPACE]:
        start_game  = False
        start_menu_screen =None
        pass
    if key_pressed[pygame.K_a]:
        if show_about== False:
            show_about =True

    if key_pressed[pygame.K_c]:
        if show_about==True:
            show_about=False




    pygame.display.update()
####################
#########    G A M E     O V E R     S C  R E E N #############################################################################################################
#########################################
def  GAME_OVER():


    global  game_state , gameover ,screen_gameover , new_highscore,now_time,count,ball_list

    pygame.display.update()
    screen_gameover  = pygame.display.set_mode((screen_width , screen_height))
    set_name()
    screen_gameover.fill(white)
    if new_highscore  == False:

        text_to_gamer(' L O S E R !!!!!!!!', (0, screen_height / 4), screen_gameover, red, 70)
    elif new_highscore == True:
        HIGHSC  = open('highscore.txt' , 'r')
        high  = HIGHSC.read()
        HIGHSC.close()
        text_to_gamer('NEW HIGSCORE', (10, screen_height / 4), screen_gameover, midnightblue, 70)
        text_to_gamer(high,(200, screen_height / 3), screen_gameover, red, 30)




    text_to_gamer('press SPACE  to  restart' , (50 ,screen_height/2) , screen_gameover , black , 20)

    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if  key_pressed[pygame.K_SPACE]:
            print('restarting game')
            new_highscore = False
            gameover= False
            screen_gameover = None
            player.rect.x = screen_width/2
            player.rect.y = screen_height/2
            now_time = time.time()
            count = True
            ball_list = []
            break


    pass



def game_events():




    key_pressed = pygame.key.get_pressed()

    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            write_if_not_exist('highscore.txt')
            pygame.quit()
            sys.exit()




    if key_pressed[pygame.K_LCTRL]:
        global  game_paused

        level.game_paused()
        print('paused')
        pass





lives  = 3
gameover  = False
def ball_collision():
    for ball  in ball_list:
        ball.wall_collision()


def ball_control():
    if len(ball_list)<= 7:
        ball_list.append(pong_ball( [random.randrange(-3,5) , random.randrange(7,9)] , [random.randrange(70  , screen_width-20)  , -30]))


def ball_and_box_collision(screen):
    ball_collision()
    global lives , gameover


    for ball in ball_list:
        ball_control()

        ball.wall_collision()
        ball_activity(ball , screen)
        if player.rect.collidepoint(ball.image_rect.left , ball.image_rect.top):
            ball.speed = [0,0]
            level.splash(screen,ball.image_rect.center)
            level.splash(screen,player.rect.center)
            print('ball hit')
            if level.life <= 0:
                level.game_over()
            else:

                level.life  -= 1

            try:
                ball_list.pop(ball_list.index(ball))
            except:
                pass
            pygame.display.flip()



    pass

def display_level():
    pass


original_start   = True
now_time  = time.time()
count = True
def  check_time():
    global  count
    if original_start== True:

        if time.time() -now_time  >  3:
            count= False
        pass
def  loop_main():

    global  pong_screen , gameover
    while  game_state == True:
        pygame.mouse.set_visible(False)
        if start_game == False:

            if gameover == False:
                if game_paused== False:
                    check_time()

                    level.level_check()
                    game_events()
                    frame.tick(60)
                    pong_screen = pygame.display.set_mode((screen_width , screen_height),pygame.NOFRAME)
                    set_name()

                    pygame.draw.rect(pong_screen,level.bg_color , pygame.Rect(0,0 , screen_width,screen_height - 60) , 0)
                    pygame.draw.rect(pong_screen, white, pygame.Rect(0, screen_height-60, screen_width,  60), 0)
                    text_to_gamer(('SCORE: ' + str(SCORE)+'|'), (0, screen_height - 60), pong_screen,  purple, 20)
                    text_to_gamer('LCTRL to pause '+'|' , (0, screen_height - 30), pong_screen, midnightblue, 20)
                    text_to_gamer('LEVEL  : '+ str(level.current_level ) +'|' , (150 , screen_height-60  ),pong_screen , goldenrod  , 20 )
                    text_to_gamer('LIVES LEFT   :'+ str(level.life)  , (300 , screen_height-60  ) ,pong_screen , black   ,20)
                    text_to_gamer('HIGHSCORE :' + level.highscore, (300, screen_height - 30), pong_screen, black, 20)


                    if count== False:

                        ball_and_box_collision(pong_screen)


                        ball_control()
                    player_activities(pong_screen)
                if game_paused == True:
                    GAME_PAUSED()
            elif gameover == True:
                GAME_OVER()



            pygame.display.flip()



        elif start_game ==True:
            START_MENU()
    pygame.display.set_caption('HYDROPHOPIC')
    pygame.display.set_icon((pygame.image.load('ball.png')))
    pygame.display.update()


if __name__  == '__main__':
    loop_main()
    
