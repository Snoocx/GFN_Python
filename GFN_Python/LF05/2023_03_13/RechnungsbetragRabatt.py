def GetInputAsRevenue():
   revenue = input("Wie hoch war der Umsatz?\n")  # Eingabe von Umsatz
   revenue = revenue.replace(",", ".")            # , mit . ersetzen

   try:                                             # Überprüfe mit Try ob der eingegebene Wert in Float umgewandelt werden kann:
      revenue = float(revenue)                      # Umwandlung von String zu Float
   except ValueError:
       print("Bitte nur Zahlen eingeben!")          # Ausgabe falls keine Zahl eingegeben wurde
       exit()                                       # Beenden des Programms
   else:
       return revenue                               # Zurückgeben von der Eingabe als Float
       

def CalculateBillingAmountFromRevenue(revenue):
    if revenue >= 500:                                  # Ab einem Umsatz von 500 wird..
        discount = 10                                   # der Discount auf 10 gesetzt
    elif revenue >= 100:                                # Wenn der Umsatz kleiner als 500 aber größer als 100 ist wird..
        discount = 5                                    # der Discount auf 5 gesetzt
    else:                                               # Wenn der Umsatz kleiner als 500 und kleiner als 100 ist wird..
        discount = 0                                    # der Discount auf 0 gesetzt
    return revenue * ( 1 - discount / 100 )             # Berechnung und Rückgabe des Rechnungsbetrages

def main():
    revenue = GetInputAsRevenue()                               # Funktionsaufruf ^ hier wird der Umsatz geholt und zugewiesen
    billingAmount = CalculateBillingAmountFromRevenue(revenue)  # Funktionsaufruf, Umsatz wird mit übergeben ^ hier wird der Rechnungsbetrag ausgerechnet und zugewiesen
    print(f"Bei einem Umsatz von \"{str(revenue)} €\", ist der Rechnungsbetrag abzüglich des Rabattes: {str(billingAmount)} €") # Ausgabe

main()