alphabet = "abcdefghijklmnopqrstuvwxyz"

print ('Welcome to the letter finder!')
print ('Choose a string of letters to receive from the alphabet')
print ('Start at a higher letter value to recieve a reverse order string!')

input1 = int(input('Start at letter number: '))
input2 = int(input('End at letter number: '))

if input1>input2:
    if (input2-2)== -1:
        snip = alphabet[input1 - 1::-1]
    else:
        snip = alphabet[input1-1:input2-2:-1]
else:
    snip = alphabet[input1-1:input2]

print ("Your string is: " + snip)