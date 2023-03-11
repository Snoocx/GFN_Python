import random

a = random.randint(1, 10)
b = random.randint(1, 10)

c = a + b

print("Was ist das Ergebnis aus ", a ," + ", b )

zahl = int(input())

if zahl == c:
    print(zahl, "ist richtig")
else:
    print(zahl, "ist falsch")

