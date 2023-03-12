def GetInputAsInch():
   inputInches = input("Angabe in Inch:\n") # Eingabe von Inch
   inputInches = inputInches.replace(",", ".") # , mit . ersetzen
   return float(inputInches) # Cast zu Float

def main():

    while True:                     # die While-Schleife wird immer wiederholt, weil die Bedinung "immer" True ist
        inches = GetInputAsInch()   # der Input wird über die Methode GetInputAsInch() geholt und in die Variable inches gespeichert
        if inches == 0:             # Überprüft ob die Eingegebene Zahl 0 ist
            break                   # mit break verlässt man die "aktuelle" Schleife
        cm = inches * 2.54          #die Berechnung könnte auch ausgelagert werden in eine eigene Funktion... aber für eine Zeile macht es keinen Sinn 3 Zeilen zu schreiben... Faulheit und so..
        print(f"Deine Eingabe von \"{str(inches)}\" ergibt: {str(cm)} cm")

main()