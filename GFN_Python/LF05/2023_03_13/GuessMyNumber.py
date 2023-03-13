import random

def GetInputAsInt():
    guessed = None
    try:
        guessed = int(input("Dein Rateversuch:\n"))
    except:
        GetInputAsInt()
    return guessed

def GuessingLoop():
    numberToGuess = random.randint(1,6)
    countGuessed = 1

    guessedNumber = GetInputAsInt()
    while guessedNumber != numberToGuess:
        countGuessed = countGuessed + 1
        guessedNumber = GetInputAsInt()
    return countGuessed

countGuessed = GuessingLoop()
print(f"Du hast beim {countGuessed}. Versuch die Zahl richtig erraten")
