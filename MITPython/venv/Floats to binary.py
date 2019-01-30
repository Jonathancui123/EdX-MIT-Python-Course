x = float(input("Give me a decimal between 0 and 1"))
p = 0


while x*(2**p) %1 !=0:
    p += 1
    #print(x*(2**p))
    #what to do to break infinite loop?

y = int(x*(2**p))
dec = ''

while y > 0:
    dec = dec + str(y%2)
    y = y//2
result = int(dec)/(10**p)


print(result)

