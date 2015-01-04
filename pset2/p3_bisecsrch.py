balance = 999999
annualInterestRate = 0.18

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
"""

def m_upperb(annualInterestRate,balance):
    return ((balance*((1+annualInterestRate/12.0)**12))/12.0)
    
def m_lowerb(balance):
    return (balance/12)
    
def Monthly_unpaid_balance (bal,mbal):
    return (bal-mbal)

def balance_each_month(mub,air):
    return ((mub + (air/12.0 * mub)))    

temp = balance
high=0.0 
low=0.0   
minimum_monthly_payment=0.0
low= m_lowerb(temp)   
high= m_upperb(annualInterestRate,temp)

while (high-low)>0.01:
    mid = ((high+low)/2.0)
            
    for m in range(1,13):
            mub = Monthly_unpaid_balance(temp,mid)
            temp = balance_each_month(mub,annualInterestRate)         
    
    minimum_monthly_payment = mid   
    if temp<0:
            high = mid
            temp = balance 
    else:
            low = mid+0.01
            temp = balance
      
    
print "Lowest Payment: " + str(round(minimum_monthly_payment,2))
     

     
     
     