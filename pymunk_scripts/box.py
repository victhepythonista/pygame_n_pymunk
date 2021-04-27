

# a simple sxreen to contain pymunk  dynamic objects
# for use with pygame use only though as the x and y coordinates 
# arre different inpygame

import pymunk,pygame


class Ground:
    # a ground with gravity
    def __init__(self,space, x,y,w,h,d = 10):
        ground = pymunk.Segment(space.static_body, (x,y),(x + w,y),d)
        ground.elasticity = .3
        ground.friction = 3
        space.add(ground)
        
        
        
class SimpleBar:
    def __init__(self,space, x,y,w,h,d = 30):
        body = space.static_body
        body.position = x,y
        bar = pymunk.Poly.create_box(space.static_body,(w,h),d)
        bar.elasticity = .3
        bar.friction = 3
        space.add(bar)
        
            
class EnclosedBox:
    # AN ENCLOSED BOX
    def __init__(self,  space  , x,y,w,h,d =5 , elasticity = .5, friction = .1, color = pygame.Color("yellow")):
        self.x = x
        self.y = y
        self.w = w
        self.h =h
       
        self.p1 = [self.x,self.y]
        self.p2 = [self.x + self.w,self.y]
        self.p3 = [self.x + self.w , self.y + self.h]
        self.p4 = [self.x , self.y + self.h]
        self.points = [self.p1,self.p2,self.p3,self.p4]
        self.d =d
        
        for i in range(4): 
            pa = self.points[i]
            pb =  self.points[(i + 1)%4]
            print(i,pa,pb)
            seg = pymunk.Segment(space.static_body,pa,pb,d)
            seg.elasticity = elasticity
            seg.color = color
            seg.friction = friction
            space.add(seg)
            

        
        
   
        
        
        
        
    
        
    