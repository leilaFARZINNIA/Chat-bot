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


# Funktion zum Finden der Antworten für die Fragen
def antwort_finden(fragen, wissensbasis):
    antworten = []
    for frage in fragen:
        antwort = wissensbasis.get(frage.lower(), "Entschuldigung, ich kenne die Antwort auf diese Frage nicht.")
        antworten.append(antwort)
    return antworten


# Beispielhafte Wissensbasis mit Fragen und Antworten
wissensbasis = {
    "wann beginnt das semester?": "Das Semester beginnt am 1. Oktober.",
    "bis wann muss ich den semesterbeitrag bezahlen?": "Der Semesterbeitrag muss bis zum 15. September bezahlt werden.",
    "wo finde ich den vorlesungssaal?": "Den Vorlesungssaal finden Sie im Gebäude B, Raum 101.",
}


# Hauptprogramm
if __name__ == "__main__":
    print("Willkommen! Geben Sie eine zusammengesetzte Frage ein.")
    eingabe = input("Ihre Frage: ")

    # Zerlegen der Eingabe in einzelne Fragen
    fragen = frage_zerlegen(eingabe)

    if fragen:
        print("Die folgenden Fragen wurden erkannt:")
        for idx, frage in enumerate(fragen, 1):
            print(f"{idx}. {frage}")

        # Finden der Antworten für die erkannten Fragen
        antworten = antwort_finden(fragen, wissensbasis)

        print("\nDie passenden Antworten sind:")
        for idx, antwort in enumerate(antworten, 1):
            print(f"{idx}. {antwort}")
    else:
        print("Keine gültigen Fragen erkannt.")
