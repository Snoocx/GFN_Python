
#Schreiben Sie ein Programm, das den Anwender wie-
#derholt dazu auffordert, einen Wert in Inch einzugeben. Der eingegebene Wert soll in Zentimeter umgerechnet und ausgegeben wer-
#den. 
#Das Programm soll nach der Eingabe des Werts 0 beendet werden.

#Hinweis:
#Bei einer while-Schleife wird immer angegeben, gemäß welcher Bedin-
#gung wiederholt werden soll, und nicht, gemäß welcher Bedingung be-
#endet werden soll. Daher müssen Sie in diesem Programm formulieren:
#Solange die Eingabe ungleich O ist.

inches = 0.0

def GetInputInch():
   global inches
   inputInches = input("Angabe in Inch:\n") # Eingabe von Inch
   inputInches = inputInches.replace(",", ".") # , mit . ersetzen
   inches = float(inputInches) # Cast zu Float
   return inches

# Für die Übersicht teile ich die Funktion auf.. es geht auch so:
# inches = float(input("Angabe in Inch:\n").replace(",", "."))

def main():
    global inches
    while GetInputInch() != 0:
        cm = inches * 2.54
        #print("Deine Eingabe von \"" + str(inches) + "\" ergibt: " + str(cm) + "cm").... als fstring schöner:
        print(f"Deine Eingabe von \"{str(inches)}\" ergibt: {str(cm)} cm")

main()