
import pymunk, pygame



class RotatingRect:
    def __init__(self,space,x,y,w,h,force,position):
        body = pymunk.Body(199,10,pymunk.Body.DYNAMIC)
        body.position = x,y
        
        body.apply_force_at_local_point(force,position)
        
        rect = pymunk.Poly.create_box(body, (w,h))
        
        space.add(body, rect)
        