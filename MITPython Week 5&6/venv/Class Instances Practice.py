class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_dist_sq = (self.x - other.x)**2
        y_dist_sq = (self.y - other.y)**2
        return (x_dist_sq+y_dist_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

def userCalcDist (origin):
    print("This will calculate distance from origin to your point")
    while True:
        try:
            userInput = input("Input the coordinates of the point separated by a comma and a space!")
            pt = Coordinate(int(userInput.split(", ")[0]), int(userInput.split(", ")[1]))
            break
        except:
            print("Invalid input, try again")
    return (Coordinate.distance(pt,origin))

origin = Coordinate(0,0)
print(origin)
print(type(origin))
print(type(Coordinate))
print(isinstance(origin, Coordinate))
#print(userCalcDist(origin))


