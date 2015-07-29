from .shaders import ShaderProgram

from nytram.entity import Entity
from nytram.renderers import EntityRenderer
from nytram.ext.box2d import Body, Fixture, BodyTypes, Box

class Wall:
    """ Helper to load wall entities """
    renderer = None
    
    @classmethod
    def loadRenderer(cls):
        """ Load the renderer """
        cls.renderer = EntityRenderer(ShaderProgram, elements=[0,2,1,3,0,1], vertexData={0:[15, 1, 0, -15, -1, 0, 15, -1, 0, -15, 1, 0]})
    
    @classmethod
    def build(cls, scene, position):
        """ Build the Entity """
        entity = Entity(scene, renderer=cls.renderer)
        fixture = Fixture(Box(30, 2), density=1, restitution=0, friction=0, isSensor=False)
        entity.body = Body([fixture], bodyType=BodyTypes.Static, fixedRotation=True)
        entity.transform.position = position
        return entity
        
# Wall.loadRenderer()