#this finds the root of a polynomial
#In this code, we use the Newton-Rhapson to find the cube root of a number

num = float(input("Input a decimal or integer number to find the cube root of: "))
epsilon = 0.01

guess = num/2
count = 0

while abs(guess**3 - num) >= epsilon:
    #print(guess**3 - num)
    #print (3*guess)
    print(guess)
    guess = guess - ((guess**3 - num)/(3*(guess**2)))
    count += 1

print("The cube root of", num, "is " + str(guess) + "!")
print ("Number of guesses:", count)
