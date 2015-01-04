pay = 0.0
interest = 0.0
totalpay = 0.0
"""
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal
"""
def monthlypay(mRate,bal):
    return round(mRate*bal,2)

def inter(aRate,bal):
     return round(aRate/12 * bal,2)       

for m in range(1,13):
    print m
    pay = monthlypay(monthlyPaymentRate,balance)
    print "Minimum monthly payment: "+str(pay)
    balance-=pay
    interest = inter(annualInterestRate,balance)
    balance+=interest
    print "Remaining balance:" + str(balance)
    totalpay+=pay 
print "Total paid: " +str(totalpay)
print "Remaining balance: " +str(balance)     