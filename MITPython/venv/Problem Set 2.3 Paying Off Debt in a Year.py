balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12

monthlyLower = balance/12
monthlyUpper = (balance* (1 + monthlyInterestRate)**12 / 12)
minPay = (monthlyLower + monthlyUpper)/2


def check (balance,monthlyInterestRate,minPay):
    remainingBalance = balance
    for month in range(12):
        remainingBalance -= minPay
        remainingBalance *= (1 + monthlyInterestRate)
    return remainingBalance

result = check(balance, monthlyInterestRate, minPay)

while abs(result) > 0.05:
    if result > 0:
        monthlyLower = minPay
        minPay = (monthlyLower + monthlyUpper) / 2
    else:
        monthlyUpper = minPay
        minPay = (monthlyLower + monthlyUpper) / 2
    result = check(balance, monthlyInterestRate, minPay)
    print(round(minPay,2))


print("The minimum payment is: $" + str(round(minPay,2)))