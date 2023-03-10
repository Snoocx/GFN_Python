def status_anzeigen (anzahl_parkplaetze_belegt, eingang_frei, ausgang_frei, vermietet):
    
    # Ausgangswerte
    parkplaetze_gesamt = 500
    auslastung = parkplaetze_gesamt * 0.95

    # Aktionen als Bool festlegen
    parkhaus_gesperrt = False
    parkhaus_belegt = False
    parkhaus_frei = False

    # Priorität mit If,Elif,Else von oben nach unten..
    # Parkhaus gesperrt.. 
    if eingang_frei == False or ausgang_frei == False or vermietet == True:
        parkhaus_gesperrt = True
    # Parkhaus belegt
    elif auslastung < anzahl_parkplaetze_belegt:
        parkhaus_belegt = True
    # Parkhaus frei
    else:
        parkhaus_frei = True

    # Einfache Abfrage und Ausgabe für den aktuellen Status
    if parkhaus_frei == True:
        print("Parkhaus frei")
    elif parkhaus_belegt == True:
        print("Parkhaus belegt")
    elif parkhaus_gesperrt == True:
        print("Parkhaus gesperrt")
        


def main ():
    status_anzeigen(330, True, True, False)     #Beispiel aus Aufgabe

    status_anzeigen(200, False, True, False)    #Einfahrt blockiert
    status_anzeigen(200, True, False, False)    #Ausfahrt blockiert
    status_anzeigen(200, False, False, True)    #für Veranstaltung angemietet

    status_anzeigen(200, True, True, False)     #frei

    status_anzeigen(475, True, True, False)     #Auslastung genau 95%.. 
    status_anzeigen(476, True, True, False)     #Auslastung über 95%.. 
    status_anzeigen(476, False, True, False)    #Auslastung über 95% und Einfahrt blockiert
    status_anzeigen(476, True, False, False)    #Auslastung über 95% und Ausfahrt blockiert
    status_anzeigen(476, True, True, True)      #Auslastung über 95% und für Veranstaltung angemietet
    status_anzeigen(476, False, False, True)    #Auslastung über 95%, Ein und Ausfahrt blockiert und für Veranstaltung angemietet


main()


