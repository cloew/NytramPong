from pong import BallEntity, Wall

from nytram import Application, Window
from nytram.entity import Scene
from nytram.entity.camera import Camera, OrthoProjection
from nytram.ext.box2d import World, Vec2

import sys

def main(args):
    """ Run the main file """
    window = Window(width=400, height=400, title="Pong")
    app = Application(window=window)
    
    scene = Scene(app)
    scene.world = World(gravity=Vec2(0, 0))
    
    bottomWall = Wall.build(scene, [0, -10])
    topWall = Wall.build(scene, [0, 10])
    ball = BallEntity.build(scene, [0, 0])
    
    projection = OrthoProjection(width=20, height=20)
    camera = Camera(eye=[0.0, 0.0, 10.0], projection=projection)
    
    app.run()

if __name__ == "__main__":
    main(sys.argv[1:])