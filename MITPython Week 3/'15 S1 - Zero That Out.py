N = int(input())
#Recieve N
#For loop to receive Boss' orders
Orders = [0]
for order in range(N):
    boss = int(input())
    if boss == 0:
        Orders.pop()
    else:
        Orders.append(boss)

#List with single element = 0
#If zero, pop the last item in the list
#If not zero, append it to the list
count = 0
for element in Orders:
    count += element
print(count)

#For each item in list, add it to final count