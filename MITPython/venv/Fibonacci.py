def fib(x):
    #Input integer number, output xth fibonacci number
    if x == 1 or x == 0:
        return 1
    else:
        return fib(x-1) + fib(x-2)
x = int(input("x"))
print(fib(x))