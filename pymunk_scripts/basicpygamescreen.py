import pygame, sys, pymunk


SCREEN_SIZE = 600,600

class Screen:
    
    def __init__(self):
        self.name = "SCREEN"
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.screen_color = 255,255,255
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
        
        self.quit_event(ev)
    
    def run(self):
        while self.running:
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
            self.screen.fill(self.screen_color)
            
         
            pygame.display.update()    
           
  
Screen().run()