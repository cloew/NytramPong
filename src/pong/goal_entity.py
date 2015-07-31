from .shaders import ShaderProgram
from .behaviors.goal import Goal
from .collisions import Collidables

from nytram.entity import Entity
from nytram.ext.box2d import Body, Fixture, BodyTypes, Box
from nytram.ext.box2d.collisions import Collider, CollisionRegistration

class GoalEntity:
    """ Helper to build Goal Entities """
    
    @classmethod
    def build(cls, scene, position, team):
        """ Build the Entity """
        entity = Entity(scene)
        fixture = Fixture(Box(2, 20), density=1, restitution=0, friction=0, isSensor=True)
        entity.body = Body([fixture], bodyType=BodyTypes.Static, fixedRotation=True)
        entity.transform.position = position
        entity.collider = Collider([fixture], {CollisionRegistration(Collidables.Ball, Collidables.Goal, actsAs=Collidables.Goal)})
        entity.goal = Goal(team)
        return entity