from .collidables import Collidables
from nytram.ext.box2d import Vec2
from nytram.ext.box2d.collisions import Collision

@Collision.start(Collidables.Ball, Collidables.Goal)
def BallAndGoal(ball, goal):
    """ Handles collisions between the ball and goal """
    print("Ball is in the goal!")