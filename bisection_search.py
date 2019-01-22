balance = 320000
anualInterestRate = 0.2

balances = balance

month_interest = anualInterestRate / 12.0
lower_bound = (balances / 12.0)
upper_bound = (balances * (1 + month_interest) ** 12) / 12.0
precision = 0.1

remainder = balance

while (remainder > precision):
    result = (lower_bound + upper_bound) / 2

    for month in range(1, 13):
        new_balance = remainder - result
        month_interest_dol = month_interest * new_balance
        remainder = new_balance + month_interest_dol
    
    if (remainder <  0): # the prediction is too high because, the person has to pay more than what he ows
        upper_bound = result
        remainder = balance
    elif (remainder > precision): # The prediction is too low because the remainder couldn't fulful the accuracy I want.
        lower_bound = result
        remainder = balance
print(round ( result, 2))