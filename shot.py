from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RAIDUS):
        super().__init__(x,y,SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity*dt