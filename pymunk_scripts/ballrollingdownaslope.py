import pygame, sys, pymunk, time,random


from slope import Slope

SCREEN_SIZE = 600,600

ball_spawn_point = 400,-10

class Screen:
    
    def __init__(self):
        self.name = "SCREEN"
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.screen_color = 255,255,255
        self.balls_list = []
        self.space = pymunk.Space()
        self.space.gravity = 0,100
        pygame.display.set_caption(self.name)
        
    def quit_event(self, events ):
            # anticipate a quit event

        for ev in events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit() 
                

    def display(self):
        ev = pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            b = self.create_ball(self.space)
            self.balls_list.append(b)
            time.sleep(.2)
            
        self.quit_event(ev)
        
    def create_ball(self,space):
            
        cherry_atom = pymunk.Body(50, 10, pymunk.Body.DYNAMIC)
        
        cherry_atom.position = 300,0
        
        shape = pymunk.Circle(body = cherry_atom, radius=20)
        shape.elasticity = .2
        
        # add the shape to the space
        
        space.add(cherry_atom,shape)
        return shape
       
    def draw_balls(self):
        for b in self.balls_list:
            pygame.draw.circle(self.screen, (10,200,200), b.body.position, 20)
            
            
        
       
       
    print('new cherrie !')
    
    def draw_lines(self):
        line1 = [[300, 90],[750,-60]]
        line2 = [[-300,100],[420,200]]
        line3 = [[100,400],[2050,300]]
        
        
        lines = [line1, line2, line3]
        for line in lines:
            pygame.draw.lines(self.screen, (0,0,0), True,line, 10)
            

    def run(self):
        
        space = self.space
        space.gravity = 0,100
        ball = self.create_ball(space)
        self.balls_list.append(ball)
        
        # lets addd the slopes
        Slope(space,300,100,750,-50)
        Slope(space, -300,100,420,200)
        Slope(space, 100,400,2050,300)
        Slope(space,600,0,590,600)
        Slope(space,0,0,0,600)
        Slope(space,0,600,600,600)
        while self.running:
            self.display()
            self.screen = pygame.display.set_mode((600,600))
            self.screen.fill(self.screen_color)
            space.step(.01)
           
           
            self.draw_lines()
            self.draw_balls()
            pygame.display.update()    
           
if __name__ == '__main__':
    Screen().run()