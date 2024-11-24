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
    """
    Diese Funktion durchsucht die Wissensbasis nach Antworten für die gegebenen Fragen.
    """
    antworten = []
    for frage in fragen:
        antwort = wissensbasis.get(frage.lower(), "Entschuldigung, ich kenne die Antwort auf diese Frage nicht.")
        antworten.append(antwort)
    return antworten


# Funktion zum Kombinieren der Antworten
def antworten_kombinieren(antworten):
    """
    Diese Funktion kombiniert alle Antworten in eine lesbare Form.
    """
    # Variable zum Speichern der kombinierten Antworten
    kombinierte_antwort = ""
    # Iteration über die Liste der Antworten
    for idx, antwort in enumerate(antworten):
        # Nummer und Text der Antwort hinzufügen
        kombinierte_antwort += f"Antwort {idx + 1}: {antwort}\n"
    # Die kombinierten Antworten zurückgeben
    return kombinierte_antwort


# Funktion zum Erkennen von Begrüßungen und nicht-fragenden Eingaben
def erkenne_begrüßung(eingabe):
    """
    Diese Funktion erkennt Begrüßungen und reagiert entsprechend.
    """
    # Liste von Schlüsselwörtern für Begrüßungen
    begruessungs_worte = ["hallo", "guten tag", "hi", "servus", "grüß gott"]

    # Überprüfen, ob die Eingabe ein Begrüßungswort enthält
    for wort in begruessungs_worte:
        if wort in eingabe.lower():
            return "Hallo! Wie kann ich Ihnen helfen?"

    return None  # Keine Begrüßung erkannt


# Beispielhafte Wissensbasis mit Fragen und Antworten
wissensbasis = {
    "wann beginnt das semester?": "Das Semester beginnt am 1. Oktober.",
    "bis wann muss ich den semesterbeitrag bezahlen?": "Der Semesterbeitrag muss bis zum 15. September bezahlt werden.",
    "wo finde ich den vorlesungssaal?": "Den Vorlesungssaal finden Sie im Gebäude B, Raum 101.",
}


# Hauptprogramm
if __name__ == "__main__":
    print("Willkommen! Geben Sie eine zusammengesetzte Frage oder eine Nachricht ein.")
    eingabe = input("Ihre Eingabe: ")

    # Erkennung von Begrüßungen
    begruessungs_antwort = erkenne_begrüßung(eingabe)
    if begruessungs_antwort:
        print(begruessungs_antwort)
    else:
        # Zerlegen der Eingabe in einzelne Fragen
        fragen = frage_zerlegen(eingabe)

        if fragen:
            print("Die folgenden Fragen wurden erkannt:")
            for idx, frage in enumerate(fragen, 1):
                print(f"{idx}. {frage}")

            # Finden der Antworten für die erkannten Fragen
            antworten = antwort_finden(fragen, wissensbasis)

            # Kombinieren der Antworten und Ausgabe
            kombinierte_antworten = antworten_kombinieren(antworten)
            print("\nDie kombinierten Antworten sind:")
            print(kombinierte_antworten)
        else:
            print("Keine gültigen Fragen erkannt.")
