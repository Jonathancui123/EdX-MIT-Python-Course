#guess and check to find the cube root of an integer

num = int(input("Enter a number: "))
ans_int = 0
guess_iter3 = 0.01
guess_iter2 = 0.1
guess_iter1 = 0.0001
ans_value = 0
dev = 0

while ans_int**3 < num:
    ans_int += 1
if ans_int**3 == num:
    print ('yay')
    print ("The cube root of", num, "is " + str(ans_int) + "!")
else:
    ans_value = ans_int - 1
    while ans_value**3 < num:
        ans_value +=  guess_iter2
    ans_value -= guess_iter2
    while ans_value**3 < num:
        ans_value += guess_iter3
    ans_value -= guess_iter3
#deviation calculation for final value
    dev = abs(num - ans_value**3)
    ans_value += guess_iter1
    new_dev = abs(num - ans_value**3)
    while new_dev < dev:
        dev = new_dev
        ans_value += guess_iter1
        new_dev = abs(num - ans_value**3)
    ans_value -= guess_iter1
    #print (round(ans_value, 2))
    print("The cube root of", num, "is " + str(round(ans_value, 4)) + "!")

