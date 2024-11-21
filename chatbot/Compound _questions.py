# Funktion zum Zerlegen und Erkennen von zusammengesetzten Fragen
def frage_zerlegen(eingabe):
  
    if not eingabe:
        return []  

    # Zerlegen der Eingabe anhand von Trennzeichen (wie '?', 'und', 'oder')
    trennzeichen = ['?', ' und ', ' oder ']
    fragen_liste = [eingabe]

    # Wiederholtes Zerlegen anhand der definierten Trennzeichen
    for trenn in trennzeichen:
        neue_fragen_liste = []
        for frage in fragen_liste:
            neue_fragen_liste.extend(frage.split(trenn))
        fragen_liste = neue_fragen_liste

    # Entfernen von Leerzeichen und leeren Einträgen
    fragen_liste = [frage.strip() + '?' for frage in fragen_liste if frage.strip()]
    return fragen_liste


# Beispielhafte Verwendung der Funktion
if __name__ == "__main__":
    print("Willkommen! Geben Sie eine zusammengesetzte Frage ein.")
    eingabe = input("Ihre Frage: ")
    fragen = frage_zerlegen(eingabe)

    if fragen:
        print("Die folgenden Fragen wurden erkannt:")
        for idx, frage in enumerate(fragen, 1):
            print(f"{idx}. {frage}")
    else:
        print("Keine gültigen Fragen erkannt.")
