# Paste your code into this box

initial_fixed_month = 10
annualInterestRates = 0.04
monthly_interest = (annualInterestRates / 12.0)
balances = 4596


def main(balance, monthly_pay, month_interest_rate):
    balances = balance
    count = 0
    while count < 12:
        count += 1
        unpaid_month = balances - monthly_pay
        update_balance = unpaid_month + (month_interest_rate * unpaid_month)
        balances = update_balance - month_interest_rate
    return balances 
            

while True:
    if main(balances, initial_fixed_month, monthly_interest) <= 0:
        print(initial_fixed_month)
        break
        
    else:
        initial_fixed_month = initial_fixed_month + 10
        main(balances, initial_fixed_month, annualInterestRates)
        