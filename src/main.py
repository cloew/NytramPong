from pong import BallEntity, GoalEntity, Team, Wall
from pong.collisions import BallAndGoal, BallAndWall

from nytram import Application, Window
from nytram.entity import Scene
from nytram.entity.camera import Camera, OrthoProjection
from nytram.ext.box2d import World, Vec2
from nytram.ext.box2d.collisions import CollisionManager

import sys

def main(args):
    """ Run the main file """
    window = Window(width=600, height=400, title="Pong")
    app = Application(window=window)
    
    scene = Scene(app)
    scene.world = World(gravity=Vec2(0, 0))
    scene.collisionManager = CollisionManager([BallAndGoal, BallAndWall])
    
    Wall.loadRenderer()
    BallEntity.loadRenderer()
    
    leftTeam = Team("Left", app)
    rightTeam = Team("Right", app)
    
    bottomWall = Wall.build(scene, [0, -10])
    topWall = Wall.build(scene, [0, 10])
    ball = BallEntity.build(scene, [0, 0])
    leftGoal = GoalEntity.build(scene, [-13.5, 0], rightTeam)
    rightGoal = GoalEntity.build(scene, [13.5, 0], leftTeam)
    
    projection = OrthoProjection(width=30, height=20)
    camera = Camera(eye=[0.0, 0.0, 10.0], projection=projection)
    
    app.run()
    
    print("Left Team:", leftTeam.points)
    print("Right Team:", rightTeam.points)

if __name__ == "__main__":
    main(sys.argv[1:])