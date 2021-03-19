import pygame

class Scoreboard():


    def __init__(self):
        self.level = 0

    def text_to_gamer(self, message, position, window, color, fontsize):
        #### _this function  writes  a message to the user
        pygame.font.init()
        mess_obj = pygame.font.SysFont('chalkduster', fontsize)
        mess_render = mess_obj.render(message, 20, color)
        window.blit(mess_render, position)

    def get_highscore(self):
        try:
            with open('highscore.txt', 'r') as file:

                data = int(file.read())
                return data
        except:
            file = open('highscore.txt', 'w')
            file.write('0')
            return 0

        pass
    def check_if_highscore(self, score):

        current = self.get_highscore()

        if score  > current:
            print('[ NEEW HIGHSCORE ]')
            with open('highscore.txt', 'w') as f:
                print('[ UPDATING  HIGHSCORE]')
                f.write(str(score))
                f.close()
                return  True


        else:
            print('[ try again loser]')
            return  False



