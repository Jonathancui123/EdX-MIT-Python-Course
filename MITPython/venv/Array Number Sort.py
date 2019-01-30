#Array = [15,5,9,11,20,1,3]
print ("We will sort your numbers for you!")
user1 = int(input("How many numbers to sort?"))

Array = []
for n in range(user1):
    new_num = float(input("What is the next number?" ))
    Array.append(new_num)

print ("Sorting!!!!")

#temp variable for sort function
temp = 0
for p in range(len(Array)-1):
    for i in range(len(Array)- (1 + p)):
        if Array[i] >= Array[(i + 1)]:
            temp = Array[i]
            Array[i] = Array[i+1]
            Array[i+1] = temp

#print (range(len(Array)))
print (Array)



