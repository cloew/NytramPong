from .behaviors.player import Player
from .shaders import ShaderProgram
from .collisions import Collidables, CollidableCategories

from nytram.entity import Entity
from nytram.renderers import EntityRenderer
from nytram.ext.box2d import PlayerBody, Fixture, BodyTypes, Box, Filter
from nytram.ext.box2d.collisions import Collider, CollisionRegistration
from nytram.ext.box2d.movement import Axis, Movement, InstantVelocity

class Paddle:
    """ Helper to build Paddle Entities """
    renderer = None
    
    @classmethod
    def loadRenderer(cls):
        """ Load the renderer """
        cls.renderer = EntityRenderer(ShaderProgram, elements=[0,2,1,3,0,1], vertexData={0:[.5, 2.5, 0, -.5, -2.5, 0, .5, -2.5, 0, -.5, 2.5, 0]})
    
    @classmethod
    def build(cls, scene, position, upKey, downKey):
        """ Build the Entity """
        entity = Entity(scene, renderer=cls.renderer)
        dynamicFixture = Fixture(Box(1, 5), density=1, restitution=0, friction=0, isSensor=False, filter=Filter(categoryBits=CollidableCategories.DynamicPaddle, maskBits=~CollidableCategories.Ball))
        kinematicFixture = Fixture(Box(1, 5), density=1, restitution=0, friction=0, isSensor=False, filter=Filter(categoryBits=CollidableCategories.KinematicPaddle, maskBits=CollidableCategories.Ball))
        entity.body = PlayerBody([dynamicFixture], [kinematicFixture], fixedRotation=True)
        entity.transform.position = position
        entity.collider = Collider([kinematicFixture], {CollisionRegistration(Collidables.Ball, Collidables.Wall, actsAs=Collidables.Wall)})
        entity.movement = Movement({"Up":[0,1], "Down":[0,-1]}, InstantVelocity(5, axis=Axis.Vertical))
        entity.player = Player(upKey, downKey)
        return entity