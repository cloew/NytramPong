from .shaders import ShaderProgram
from .collisions import Collidables

from nytram.entity import Entity
from nytram.renderers import EntityRenderer
from nytram.ext.box2d import Body, Fixture, BodyTypes, Box
from nytram.ext.box2d.collisions import Collider, CollisionRegistration

class Paddle:
    """ Helper to build Paddle Entities """
    renderer = None
    
    @classmethod
    def loadRenderer(cls):
        """ Load the renderer """
        cls.renderer = EntityRenderer(ShaderProgram, elements=[0,2,1,3,0,1], vertexData={0:[.5, 2.5, 0, -.5, -2.5, 0, .5, -2.5, 0, -.5, 2.5, 0]})
    
    @classmethod
    def build(cls, scene, position):
        """ Build the Entity """
        entity = Entity(scene, renderer=cls.renderer)
        fixture = Fixture(Box(1, 5), density=1, restitution=0, friction=0, isSensor=False)
        entity.body = Body([fixture], bodyType=BodyTypes.Dynamic, fixedRotation=True)
        entity.transform.position = position
        entity.collider = Collider([fixture], {CollisionRegistration(Collidables.Ball, Collidables.Wall, actsAs=Collidables.Wall)})
        return entity