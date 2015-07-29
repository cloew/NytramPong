from nytram import Application, Window
from nytram.entity.camera import Camera, OrthoProjection

import sys

def main(args):
    """ Run the main file """
    window = Window(width=400, height=400, title="Pong")
    app = Application(window=window)
    
    projection = OrthoProjection(width=20, height=20)
    camera = Camera(eye=[0.0, 10.0, 10.0], projection=projection)
    
    app.run()

if __name__ == "__main__":
    main(sys.argv[1:])