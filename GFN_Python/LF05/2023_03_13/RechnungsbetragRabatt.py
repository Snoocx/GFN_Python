def GetInputAsRevenue():
   revenueString = input("Wie hoch war der Umsatz?\n")
   revenueString = revenueString.replace(",", ".") 
   return  float(revenueString) 

def CalculateBillingAmountFromRevenue(revenue):
    if revenue >= 500:
        discount = 10
    elif revenue >= 100:
        discount = 5
    else:
        discount = 0
    return revenue * ( 1 - discount / 100 )

def main():
    revenue = GetInputAsRevenue()
    billingAmount = CalculateBillingAmountFromRevenue(revenue)
    print(f"Bei einem Umsatz von \"{str(revenue)} €\", ist der Rechnungsbetrag abzüglich des Rabattes: {str(billingAmount)} €")

main()