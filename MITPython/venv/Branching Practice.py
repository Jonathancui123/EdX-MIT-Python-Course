print('This is the division program')
x = float(input('Give me a float for x:'))
y = float(input('Give me a float for y:'))

if x==y:
    print('they are the same number!')
    print ('x/y = ', x/y)
elif x > y:
    print ('x is greater than y')
    if y != 0:
        print ('x/y = ', x/y)
    else:
        print ('cannot divide, y is equal to zero!')
else:
    print ('y is greater than x!')
    print ('x/y = ', x/y)
