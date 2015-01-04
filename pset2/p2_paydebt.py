balance = 3329
annualInterestRate = 0.2

"""
Monthly_interest_rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly_unpaid_balance) + (Monthly_interest rate x Monthly unpaid balance)
"""

def Monthly_unpaid_balance (bal,mbal):
    return bal-mbal

def balance_each_month(mub,air):
    return round((mub + (air/12.0 * mub)),2)
                
temp = balance
minimum_monthly_payment = 10

while True:
    for m in range(1,13):
        mub = Monthly_unpaid_balance(temp,minimum_monthly_payment)
        temp = balance_each_month(mub,annualInterestRate)    
    if temp > 0:
        minimum_monthly_payment+=10
        temp = balance
    else:
        print "Lowest Payment: " + str(minimum_monthly_payment) 
        break
        
             