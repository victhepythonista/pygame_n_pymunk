import pymunk, pygame



"""
A swinging pendulum based on the  PinJoint class
"""
class Pendulum:
    def __init__(self,space,joint_position,ball_position ,radius = 20, moment = 10, elasticity =1):
        b0 =space.static_body
        
        body = pymunk.Body(1, moment,pymunk.Body.DYNAMIC)
        body.position = ball_position
        pendulum = pymunk.Circle(body, radius)
        pendulum.color = pygame.Color("green")
        pendulum.elasticity = elasticity
        joint = pymunk.PinJoint(b0, body, joint_position)
        
        space.add(joint, body, pendulum)
        
        

        
        
        