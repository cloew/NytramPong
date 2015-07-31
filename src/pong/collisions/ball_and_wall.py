from .collidables import Collidables
from nytram.ext.box2d import Vec2
from nytram.ext.box2d.collisions import Collision

@Collision.start(Collidables.Ball, Collidables.Wall)
def BallAndWall(ball, wall):
    """ Handles collisions between the ball and wall """
    ball.movement.speed += 1