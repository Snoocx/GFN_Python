import random

def GetInputAsInt():
    guessed = None
    try:
        guessed = int(input("Dein Rateversuch:\n"))
    except:
        GetInputAsInt()
    return guessed

def GuessingLoop():
    numberToGuess = random.randint(1,6)     # Nummer zwischen 1-6 wird generiert und in Variable gespeichert
    countGuessed = 1                        # der gezählte Wert wird auf 1 gesetzt, man startet mit dem ersten Versuch

    guessedNumber = GetInputAsInt()         # Funktionsaufruf ^ Eingabe wird auf guessedNumber gesetzt
    while guessedNumber != numberToGuess:   # Schleife wird solange wiederholen, bis man die richtige Zahl errät, ansonsten wird bei einem fehlgeschlagenen Versuch..
        countGuessed = countGuessed + 1     # ..der Counter um 1 erhöht
        guessedNumber = GetInputAsInt()     # ..und erneut nach einer Eingabe gefragt
    return countGuessed                     # Sobald die richtige Zahl eingegeben wurde, wird der Counter zurückgegeben

countGuessed = GuessingLoop()               # Startet den Ratespaß und weißt das Ergebnis vom Counter der Variable zu
print(f"Du hast beim {countGuessed}. Versuch die Zahl richtig erraten") 
