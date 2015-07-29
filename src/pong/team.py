
class Team:
    """ Represents a team """
    
    def __init__(self, name, app):
        """ Initialize the team """
        self.name = name
        self.points = 0
        self.app = app
        
    def score(self):
        """ Score a goal for this team """
        self.points += 1
        if self.points >= 10:
            self.app.stop()