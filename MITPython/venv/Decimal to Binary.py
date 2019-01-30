x = int(input("Give me a decimal-representation integer!"))
result = ''

if x < 0:
    is_negative = True
    x = abs(x)
else:
    is_negative = False

while x > 0:
    digit = x%2
    result = str(digit) + result
    x = x//2
if is_negative:
    result = '-' + result

print (result)