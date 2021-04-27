
import pymunk, math



class Slope:
    
    def __init__(self,space, x,y,endx,endy, d = 10, elasticity = 0, friction = 0):
        
        pa = x,y
        pb = endx,endy

        seg = pymunk.Segment(space.static_body, pa, pb, d)
        seg.elasticity = elasticity
        seg.friction = friction
        space.add(seg)