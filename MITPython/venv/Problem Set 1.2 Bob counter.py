s = input("Give a string: ")

#for loop to move through the string
#slice 3 character string
#check if "BOB" or not

index = 0
count = 0

for char in range(len(s)-2):
    chunk = s[index:(index+3)]
    print(chunk)
    if chunk == 'bob':
        count += 1
        print(count)
    index += 1

print("Number of times bob occurs is:", count)