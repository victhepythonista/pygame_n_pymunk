

import  pipe, pygame, random, colors

class Pipe_manager():
    def __init__(self, speed, flappy):

        self.pipes_passed = 0
        self.speed= speed
        self.flappy = flappy
        self.pipes_list = []
        self.game_state = True
        self.position = 'top'
        self.pipe_proximity = 120,150

        self.color = colors.chocolate
    def clear_cache(self):
        self.pipes_list = []
        self.pipes_passed = 0
    def add_pipe(self):

        display = pygame.display.get_window_size()
        width = display[0]
        height = display[1]
        height_for_the_pipes = height - 30

        def return_random_height():
            return  random.randint(height_for_the_pipes-260, height_for_the_pipes - 100)
        def get_x():
            x = width+ 20  if  self.pipes_list == []  else  self.pipes_list[-1].x +250

            return x
        x = get_x()


        top = self.pipes_list.append(pipe.Pipe(x, 0, 40, return_random_height(), self.color , 'top'))

        y_bottom_pipe = self.pipes_list[-1].rect.bottomleft[1] + 100
        if self.pipes_list[-1].position == 'top':

            if self.pipes_list[-1].rect.bottomleft[1] > height-130:

                pass
            else:
                self.pipes_list.append(pipe.Pipe(x, y_bottom_pipe , 40, height_for_the_pipes - y_bottom_pipe, self.color, 'bottom'))


    def move_pipes(self, window):

        if len(self.pipes_list) < 7:
            self.add_pipe()

        for pipe in self.pipes_list:
            if pipe.x + pipe.width < 0:
                self.pipes_list.pop(self.pipes_list.index(pipe))
                self.add_pipe()
                self.pipes_passed += 1


            else:
                pipe.move(self.speed)
                pipe.draw_pipe(window)

    def get_collision(self):
        for pipe in self.pipes_list:
            if pipe.rect.colliderect(self.flappy):
                return True
            else: return False
        pass
