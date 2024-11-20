def frage_zerlegen(eingabe):
    # Überprüfen, ob die Eingabe gültig ist (nicht None und nicht leer)
    if not isinstance(eingabe, str) or not eingabe.strip():
        print("Ungültige Eingabe! Bitte geben Sie eine gültige Frage ein.")
        return []  # Leere Liste zurückgeben, wenn die Eingabe ungültig ist

    # Zerlegen der Eingabe in einzelne Fragen basierend auf '?'
    fragen_liste = eingabe.split("?")
    
    # Entfernen von Leerzeichen und Hinzufügen des '?' für jede Frage
    fragen_liste = [frage.strip() + "?" for frage in fragen_liste if frage.strip()]
    
    return fragen_liste


# Hauptprogramm
if __name__ == "__main__":
    eingabe = input("Bitte geben Sie eine oder mehrere Fragen ein: ")
    fragen = frage_zerlegen(eingabe)
    if fragen:
        print("Zerlegte Fragen:")
        for frage in fragen:
            print("-", frage)
    else:
        print("Keine gültigen Fragen gefunden.")
