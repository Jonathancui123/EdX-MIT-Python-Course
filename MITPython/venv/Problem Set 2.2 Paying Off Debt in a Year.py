#Trial and error to find the minimum needed
balance = 999999
annualInterestRate = 0.18

minPay = 0
monthlyInterestRate = annualInterestRate/12

def check (balance,monthlyInterestRate,minPay):
    remainingBalance = balance
    for month in range(12):
        remainingBalance -= minPay
        remainingBalance *= (1 + monthlyInterestRate)
    return remainingBalance

while check(balance,monthlyInterestRate,minPay) > 0:
    minPay += 10

print("The minimum payment is: $" + str(minPay))