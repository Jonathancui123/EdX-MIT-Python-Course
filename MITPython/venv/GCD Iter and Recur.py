"""def gcdIter(a,b):
    #Input integers a and b, output will be the greatest common denominator
    result = min(a,b)

    while result >1:
        if a%result == 0 and b%result ==0:
            break
        result -= 1

    print(result)
    return result"""

a = int(input("First number"))
b = int(input("Second number"))

def gcdRecur (a,b):
    #Input integers a and b, output will be the greatest common denominator
    if b == 0:
        return a
    if a%b == 0:
        return b
    else:
        return gcdRecur(b,a%b)

print(gcdRecur(a,b))
