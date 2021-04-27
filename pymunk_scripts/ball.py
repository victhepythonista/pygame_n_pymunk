
import pygame,pymunk

"""

a simple ball object that adds itself to a pymunnk space

"""
class Ball:
    def __init__(self,space, x,y,r,color = pygame.Color("green"), mass= 20, moment = 10,elasticity = 0):
        body = pymunk.Body(mass,moment, pymunk.Body.DYNAMIC)
        body.position = x,y
        circle  = pymunk.Circle(body,r)
        circle.elasticity = elasticity
        space.add(body,circle)
        
    
class RigidBall:
     def __init__(self,space, x,y,r,color = pygame.Color("green")):
        body = space.static_body
        body.position = x,y
        circle  = pymunk.Circle(body,r)
      
        space.add(body,circle)
        