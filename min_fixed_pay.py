
def min_fixed(balance, annualInterestRate):
    initial_fixed_month = 10
    monthly_interest = (annualInterestRate / 12.0)


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
        if int(main(balance, initial_fixed_month, monthly_interest)) <= 0:
            return initial_fixed_month
        
        elif int(main(balance, initial_fixed_month, monthly_interest)) > 0:
            initial_fixed_month = initial_fixed_month + 10
            main(balance, initial_fixed_month, annualInterestRate)
        



print(min_fixed(3926, 0.2))
