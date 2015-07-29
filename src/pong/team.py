
class Team:
    """ Represents a team """
    
    def __init__(self, name, ap):
        """ Initialize the team """
        self.name = name
        self.score = 0
        self.app
        
    def score(self):
        """ Score a goal for this team """
        self.score += 1
        if self.score >= 10:
            self.app.stop()