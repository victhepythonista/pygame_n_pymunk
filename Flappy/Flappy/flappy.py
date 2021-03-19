import pygame

import  colors


class Flappy ( ):

    def __init__(self , x, y):
        self.x = x
        self.y = y
        self.going_up = False
        self.drop_distance = 4
        self.up_distance = 8
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        self.wing_width = 20
        self.wing_length = 20
        self.up = True
        self.down = False
        self.body = None

    def show(self, window):
        ## displaying  on screeen

        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(window, (20,1,100), self.rect)

        pygame.draw.line(window, colors.white, self.rect.center, self.rect.midright)
        beak = pygame.draw.polygon(window, colors.red,
                                   [
                                       [self.rect.topright[0], self.rect.midright[1] - 10],
                                       [self.rect.topright[0] + 10, self.rect.midright[1] + 10],
                                       [self.rect.bottomright[0], self.rect.bottomright[1]],
                                       [self.rect.topright[0], self.rect.midright[1]-10]
                                   ])


        self.body = pygame.draw.circle(window, colors.yellow, (self.rect.center), self.rect.width/2+ 4)
        tail = pygame.draw.polygon(window, colors.yellow,([
            [self.rect.midleft[0],self.rect.midleft[1]],
            [self.rect.midleft[0] - 20,self.rect.midleft[1]+ 5],
            [self.rect.midleft[0] - 20, self.rect.midleft[1]-5]
        ]))
        if self.up ==  True:

            pygame.draw.polygon(window, colors.light_salmon, [
            [self.rect.centerx + 10,self.rect.centery],
            [self.rect.centerx-10, self.rect.centery],
            [self.rect.centerx, self.rect.topleft[1]- 10]
        ] )
        else :

            pygame.draw.polygon(window, colors.light_salmon, [
                [self.rect.centerx + 10, self.rect.centery],
                [self.rect.centerx - 10, self.rect.centery],
                [self.rect.centerx, self.rect.bottomleft[1] + 12]
            ])
        eye = pygame.draw.circle(window, colors.black, (self.rect.x + 20, self.rect.topright[1] + 3), 2)


    def gravity(self):
        if self.going_up:
            self.up = True

            self.going_up = False


            pass
        else:
            self.y += self.drop_distance

            self.up = False


    def go_up(self):

        self.going_up = True
        self.y -= self.up_distance
