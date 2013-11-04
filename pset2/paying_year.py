balance = 3926
annualInterestRate = 0.2
payment = 0
b = 1

while b > 0:
    payment += 10
    b = balance

    for month in range(1, 13):
        b = (b - payment) * (1 + annualInterestRate / 12.0)
        
print "Lowest Payment:", payment
