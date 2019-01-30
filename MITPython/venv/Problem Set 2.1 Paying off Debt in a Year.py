balance = 484
monthlyPaymentRate = 0.04
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12

remainingBalance = balance
for month in range (12):
    minMonthPayment = monthlyPaymentRate * remainingBalance
    remainingBalance -= minMonthPayment
    remainingBalance *= (monthlyInterestRate + 1)
    print ("Month " + str(month + 1) + " remaining balance: $", round(remainingBalance,2))