x = input('Give me a binary number!!')
y = x[::-1]
result = 0
digit = 0

for char in y:
    result += int(char)*(2**digit)
    digit += 1
print(result)
