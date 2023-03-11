#alternative Lösung ohne globale Variable, jedoch mit 2 Funktionsaufrufen..

def GetInputAsInch():
   inputInches = input("Angabe in Inch:\n") # Eingabe von Inch
   inputInches = inputInches.replace(",", ".") # , mit . ersetzen
   return float(inputInches) # Cast zu Float

def main():
    inches = GetInputAsInch()
    while inches != 0:
        cm = inches * 2.54 #die Berechnung könnte auch ausgelagert werden in eine eigene Funktion... aber für eine Zeile macht es keinen Sinn 3 Zeilen zu schreiben... Faulheit und so..
        print(f"Deine Eingabe von \"{str(inches)}\" ergibt: {str(cm)} cm")
        inches = GetInputAsInch()

main()