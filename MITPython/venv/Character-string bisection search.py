def isIn(char,aStr):
    #Input a character, output whether or not is in string
    if len(aStr) == 0 or (len(aStr) == 1 and char != aStr):
        return False
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
    elif char > midChar:
        return isIn(char,aStr[midIndex:])
    else:
        return isIn(char,aStr[:midIndex])

print(isIn("w","abceqrstuvwx"))