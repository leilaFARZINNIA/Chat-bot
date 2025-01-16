import random
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
def antwort_finden(fragen, dics):

    antworten = []
    for frage in fragen:
        case_insensitive_dics = {key.lower(): value for key, value in dics.items()}
        antwort = case_insensitive_dics.get(frage.lower(), "Keine Antwrot gefundden")
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

        kombinierte_antwort += f"\n{random.choice(antwort)}"
    # Die kombinierten Antworten zurückgeben
    return kombinierte_antwort


# Funktion zum Erkennen von Begrüßungen und nicht-fragenden Eingaben
def erkenne_begrüßung(eingabe):
    # Liste von Schlüsselwörtern für Begrüßungen
    begruessungs_worte = ["hallo", "guten tag", "hi", "servus", "grüß gott"]

    # Überprüfen, ob die Eingabe ein Begrüßungswort enthält
    for wort in begruessungs_worte:
        if wort in eingabe.lower():
            return "Hallo! Wie kann ich Ihnen helfen?"

    return None  # Keine Begrüßung erkannt


import re

# Define a list of known locations
KNOWN_LOCATIONS = [
    "Berlin", "Munich", "Hamburg", "Cologne", "Frankfurt", 
    "Stuttgart", "Düsseldorf", "Leipzig", "Dortmund", "Essen",
    "Hanover", "Braunschweig", "Wolfenbüttel",  "Goslar", "Clausthal"
]

def search_location_from_text(text, locations=KNOWN_LOCATIONS):
    matches = []
    for location in locations:
        if re.search(rf"\b{re.escape(location)}\b", text, re.IGNORECASE):
            matches.append(location)
    return matches

def compuond_question(eingabe, fragen_liste):

    # Erkennung von Begrüßungen
    begruessungs_antwort = erkenne_begrüßung(eingabe)
    if begruessungs_antwort:
        return begruessungs_antwort
    else:
        # Zerlegen der Eingabe in einzelne Fragen
        fragen = frage_zerlegen(eingabe)

        if fragen:
            # Finden der Antworten für die erkannten Fragen
            antworten = antwort_finden(fragen, fragen_liste)
            if(antworten[0] == "Keine Antwrot gefundden"):
                return "Entschuldigung, zurzeit haben wir keine Antwort für diese Frage."
            # Kombinieren der Antworten und Ausgabe
            kombinierte_antworten = antworten_kombinieren(antworten)

            found_locations = search_location_from_text(kombinierte_antworten)
            if(isinstance(found_locations, list) and len(found_locations) > 0):
                return [kombinierte_antworten, found_locations]
            
            return kombinierte_antworten
        
        else:
            return "Keine gültigen Fragen erkannt."
