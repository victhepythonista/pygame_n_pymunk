

############  this  module  is responsible  for  drawing   vaarious  vehicles
import  pygame

from pygame import Rect


class  Line():
    def __init__(self  , x,y,w , h):
        self.x  = x
        self.y = y
        self.width  =  w
        self.height  = h

    def   draw_line(self    , window  ,color):
        pygame.draw.rect(window  , color  , Rect(self.x  , self.y   , self.width  , self.height))







