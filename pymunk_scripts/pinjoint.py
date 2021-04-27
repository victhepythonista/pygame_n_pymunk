import pymunk



class BasicPinJoint:
    def __init__(self,space,x,y,w,h, ropelength = 200):
        b0 = space.static_body
        
        body = pymunk.Body(30,10,pymunk.Body.DYNAMIC)
        body.position = 200,300
        ball = pymunk.Circle(body,20)
        joint = pymunk.PinJoint(b0, body, (200,200))
        
        space.add(body,joint,ball)
        