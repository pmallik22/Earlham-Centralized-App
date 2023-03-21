## making the classroom as the base class?

class Classroom:
    def __init__(self, empty, roomNum):
        self.roomNum = roomNum
        self.empty = empty

    def availability(self):
        ## use an if statement using the input from the google form
        if yes:   ## assuming the question in the google form was "Are you using the room now?" with yes or no options
            return self.occupied
        else:
            return self.empty

Buildings = [CST, LBC]
CST = [100, 101, ...]
100 = Classroom()


buildings = [
    [Classroom("101"), Classroom()],
    []
]