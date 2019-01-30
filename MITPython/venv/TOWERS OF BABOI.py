#This code will take input of 'number of rings', the starting spike (A, B or C), and the ending spike (A, B or C)
total = int(input("How many rings?"))

def PrintMove (ring, fr, to):
    print("Move ring", ring, "from spike", fr, "to spike", to)

#PrintMove(1,"A","B")
A = "A"
B = "B"
C = "C"

def Tower (total, start, goal, spare = 0):
    if total == 1:
        PrintMove(1, start, goal)
    else:
        #Move N-1 to spare
        Tower(total-1, start, spare, goal)
        #Move N to the goal
        PrintMove(total,start, goal)
        #Move N-1 to the goal
        Tower(total-1,spare, goal, start)

Tower(total,A,C,B)
