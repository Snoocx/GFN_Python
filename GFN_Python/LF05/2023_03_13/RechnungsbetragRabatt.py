def GetInputAsRevenue():
   revenueString = input("Wie hoch war der Umsatz?\n")
   revenueString = revenueString.replace(",", ".") 
   return  float(revenueString) 

def CalculateBillingAmountFromRevenue(revenue):
    if revenue >= 500:
        revenue = revenue * 0.9
    elif revenue >= 100:
        revenue = revenue * 0.95
    return revenue

def main():
    revenue = GetInputAsRevenue()
    billingAmount = CalculateBillingAmountFromRevenue(revenue)
    print(f"Bei einem Umsatz von \"{str(revenue)} €\", ist der Rechnungsbetrag abzüglich des Rabattes: {str(billingAmount)} €")

main()