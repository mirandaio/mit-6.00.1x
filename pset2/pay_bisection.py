balance = 999999
annualInterestRate = 0.18

low = balance / 12.0
high = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0

payment = (high + low) / 2.0
b = balance
for month in range(1, 13):
    b = (b - payment) * (1 + annualInterestRate / 12.0)

while abs(b) > 0.01:
    if b < 0:
        high = payment
    else:
        low = payment
        
    payment = (high + low) / 2.0
    b = balance
    for month in range(1, 13):
        b = (b - payment) * (1 + annualInterestRate / 12.0)

print "Lowest Payment:", round(payment, 2)
