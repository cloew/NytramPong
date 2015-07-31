
class Player:
    """ Behavior to have a paddle controlled by the player """
    
    def __init__(self, upKey, downKey):
        """ Initialize the Player """
        self.upKey = upKey
        self.downKey = downKey
        
    def start(self):
        """ Connect the player input """
        self.inputHandler.register(self.upKey, self.movement["Up"].startOrStop(startWhen=lambda event: event.pressed))
        self.inputHandler.register(self.downKey, self.movement["Down"].startOrStop(startWhen=lambda event: event.pressed))
        
    @property
    def inputHandler(self):
        """ Return the input handler """
        return self.entity.scene.app.inputHandler
        
    @property
    def movement(self):
        """ Return the connected movement """
        return self.entity.movement