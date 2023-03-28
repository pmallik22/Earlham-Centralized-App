## making the classroom as the base class?

class Classroom:
    def __init__(self, empty, roomNum):
        self.roomNum = roomNum  #example: cst_101
        self.empty = green
        self.occupied = red

    def availability(self):
        ## use an if statement using the input from the google form
        # Options on QR code page: "I am entering the room" and "I am leaving the room"
        if entering:   #entering
            return self.occupied  # return red
        else:  #leaving
            return self.empty   # return green

    def create_room(self, building, roomNum):   # building: name of list (key in dict), roomNum: building_num

# make a class called building so that making change is easier

if __name__ == "__main__": 
    buildings = {
        cst:[Classroom("101"),],
        dennis:[],
        lbc:[],
        carpenter:[],
        library:[],
        others:[],
        runyan:[],
        runyan:[],
        }
    # make a file where we store all the rooms/ buildings
    # make a function that can add/ delete rooms in that file

    # make a generalized code 

    cst = building[cst]  # calling the key cst and storing the list(value) as cst
    color = cst[0].availability()
    # in the map
    cst_101 = color  # going to color the room on the map as red or green

# make a building class with list of classroom classes
# saving the data because of power failure and loss of data, write the data to a file and read from there
# we have two parts: the display on website, data under the display