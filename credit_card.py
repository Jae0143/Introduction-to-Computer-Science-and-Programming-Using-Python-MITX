
def calculate_creditcard (balance, annualInterestRate, monthlyPaymentRate):
    count = 0
    balances = balance
    monthlyInterestRate = (annualInterestRate / 12.0)
    while count < 12:
        count += 1

        minimumMonthlyPayment = balances * monthlyPaymentRate
        monthlyUnpaidbalance = (balances - minimumMonthlyPayment)
        balances = monthlyUnpaidbalance + (monthlyInterestRate * monthlyUnpaidbalance)

    return round(balances, 2)

print(calculate_creditcard(484, 0.2, 0.04))