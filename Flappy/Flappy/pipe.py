import  pygame
import colors

class Pipe():
    def __init__(self, x, y, width, height, color, position):
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.color = colors.black
        self.position = position
        self.rect =  pygame.Rect(self.x, self.y,self.width, self.height)



    def draw_pipe(self, window):
        self.rect = pygame.Rect(self.x, self.y,self.width, self.height)
        main_pipe = pygame.draw.rect(window, self.color,self.rect )

        pass

    def move(self, speed):
        self.x -= speed

