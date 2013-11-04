balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0

for month in range(1, 13):
    payment = monthlyPaymentRate * balance
    total += payment
    balance = (balance - payment) * (1 + annualInterestRate / 12.0)
    print "Month:", month
    print "Minimum monthly payment:", round(payment, 2)
    print "Remaining balance:", round(balance, 2)

print "Total paid:", round(total, 2)
print "Remaining balance:", round(balance, 2)
