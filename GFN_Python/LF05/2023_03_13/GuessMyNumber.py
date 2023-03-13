# Aufgabenstellung:
# Es soll eine Zahl von 1-6 generiert werden. Diese Zahl soll erraten werden. Die gebrauchten Versuche sollen am Ende ausgegeben werden.

import random

def GetInputAsInt():
    guessed = None
    try:
        guessed = int(input("Dein Rateversuch:\n"))
        if guessed > 6 or guessed < 1:      # Wenn die Zahl gr��er oder kleiner als der generierte Bereich ist
            raise Exception                 # soll die Eingabe wiederholt werden..
    except:
        GetInputAsInt()
    return guessed

def GuessingLoop():
    numberToGuess = random.randint(1,6)     # Nummer zwischen 1-6 wird generiert und in Variable gespeichert
    countGuessed = 1                        # der gez�hlte Wert wird auf 1 gesetzt, man startet mit dem ersten Versuch

    guessedNumber = GetInputAsInt()         # Funktionsaufruf ^ Eingabe wird auf guessedNumber gesetzt
    while guessedNumber != numberToGuess:   # Schleife wird solange wiederholen, bis man die richtige Zahl err�t, ansonsten wird bei einem fehlgeschlagenen Versuch..
        countGuessed = countGuessed + 1     # ..der Counter um 1 erh�ht
        guessedNumber = GetInputAsInt()     # ..und erneut nach einer Eingabe gefragt
    return countGuessed                     # Sobald die richtige Zahl eingegeben wurde, wird der Counter zur�ckgegeben


print("Errate eine Zahl zwischen 1-6...")
countGuessed = GuessingLoop()               # Startet den Ratespa� und wei�t das Ergebnis vom Counter der Variable zu
print(f"Du hast beim {countGuessed}. Versuch die Zahl richtig erraten") 
