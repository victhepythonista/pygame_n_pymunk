
import pymunk
class Square:
    def __init__(self,space, x,y,w,h):
        body = pymunk.Body(20,120,body_type=pymunk.Body.DYNAMIC)
        shape = pymunk.Poly.create_box(body, (w,h))
        
        space.add(body,shape)
        
    def shape(self, listt):
        listt.append(self.shape)
        
    