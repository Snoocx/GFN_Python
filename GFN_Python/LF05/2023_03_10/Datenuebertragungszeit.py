# Eingabe
title = "Datenübertragungsrate in KBit/s\n"
datenmenge = float(input("Datenmenge in MB\n"))
uebertragungsrate = float(input(title))
# Berechnung
zeit = ((int(datenmenge)*1000) / (int(uebertragungsrate)/8))/60
# Ausgabe
print(f"Die benötigte Zeit für die Übertragung beträgt: {str(zeit)} Minuten")
