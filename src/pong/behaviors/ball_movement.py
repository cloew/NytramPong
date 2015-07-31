
class BallMovement:
    """ Represents movement for the Ball """
    
    def __init__(self, speed):
        """ Initialize with the speed """
        self.speed = speed
        self.initialSpeed = speed
        
    def reset(self):
        """ Reset the ball movement to the initial speed """
        self.speed = self.initialSpeed
        
    def update(self):
        """ Update the ball """
        velocity = self.body.velocity
        desiredVelocity = velocity.unitVector*self.speed
        impulse = (desiredVelocity - velocity)*self.body.mass
        
        self.body.applyImpulse(impulse)
        
    @property
    def body(self):
        """ Return the body for the ball """
        return self.entity.body