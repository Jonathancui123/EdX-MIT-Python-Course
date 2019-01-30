"""def IterativeMultiplication(a,b):
    #Input 2 integers, return a multiplied by b
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result"""

"""n = int(input("Input a number to find the factorial!"))

def Factorial(n):
    if n == 1:
        return n
    else:
        return n*Factorial(n-1)

print(Factorial(n))"""

#Finding exponents recursively
def recurPower(a,b):
    #Take in two integers, output a to bth power
    if b == 1:
        return a
    else:
        return a*(recurPower(a, b-1))

#Finding exponents iteratively
def iterPower(a,b):
    #Take in two integers, output a to the bth power
    result = 1
    while b > 0:
        result *= a
        b -= 1
    return result

print(iterPower(2,3))