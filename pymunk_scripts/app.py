
import pygame, pymunk, sys
from pymunk import pygame_util
class App:
    
    def __init__(self, name = "App", SIZE = (500,500),gravity = (0,200), background_color = pygame.Color("grey")):
        self.name =name
        self.background_color = background_color
        self.running = True
        self.SIZE  = SIZE
        self.screen =  pygame.display.set_mode(self.SIZE)
        
        pygame.display.set_caption(self.name)
        
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.drawoptions = pygame_util.DrawOptions(self.screen)
    
        
    def quit_event(self, events ):
                # anticipate a quit event

        for ev in events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit() 
                
                
    def app_display(self):
        ev = pygame.event.get()
        self.quit_event(ev)
        
        
    def run(self):
        while self.running:
           
            self.screen =  pygame.display.set_mode(self.SIZE)
            self.screen.fill(self.background_color)
            self.space.step(0.01)
            self.drawoptions = pygame_util.DrawOptions(self.screen)
            self.space.debug_draw(self.drawoptions)
            self.app_display()
            
            pygame.display.update()
