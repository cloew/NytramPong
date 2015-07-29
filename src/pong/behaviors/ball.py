from nytram.ext.box2d import Vec2
from nytram.ext.box2d.movement import InstantVelocity

class Ball:
    """ Represents a ball's behavior """
    
    def start(self):
        """ Start the body """
        direction = Vec2(0, 1)
        speed = InstantVelocity(5)
        speed.apply(self.body, direction)
        
    @property
    def body(self):
        """ Return the body the ball is connected to """
        return self.entity.body