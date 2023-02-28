## making the classroom as the base class?

class Classroom:
    def __init__(self, empty, occupied):
        self.empty = empty
        self.occupied = occupied

    def availability(self):
        ## use an if statement using the input from the google form
        if yes:   ## assuming the question in the google form was "Are you using the room now?" with yes or no options
            return self.occupied
        else:
            return self.empty
