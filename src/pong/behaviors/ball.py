from nytram.ext.box2d import Vec2
from nytram.ext.box2d.movement import InstantVelocity

import random

class Ball:
    """ Represents a ball's behavior """
    
    def start(self):
        """ Start the body """
        self.reset()
        
    def reset(self):
        """ Reset the ball to its proper game starting position """
        self.needsToMove = True
        self.movement.direction = self.getInitialDirection()
        
    def getInitialDirection(self):
        """ Return the initial direction for the Ball """
        directions = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
        posOrNeg = [-1, 1]
        
        x = random.choice(directions)*random.choice(posOrNeg)
        y = random.choice(directions)*random.choice(posOrNeg)
        return Vec2(x, y).unitVector
        
    def update(self):
        """ Update the ball """
        if self.needsToMove:
            self.position.assign(x=0, y=0)
            self.needsToMove = False
    
    @property
    def position(self):
        """ Return the position for the ball """
        return self.entity.transform.position
        
    @property
    def movement(self):
        """ Return the movement for the ball """
        return self.entity.movement