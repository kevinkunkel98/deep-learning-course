"""
E1.2 - Listen, for/while loops
Implementiere eine Funktion, welche zwei Listen mit strings als Eingaben akzeptiert
und eine Liste ausgibt, welche alle Kombinationen von Verkettungen von strings
in der Form f(l0, l1) = {u + v, u ∈ l0, v ∈ l1} enthaelt.
"""

def string_kombinationen(l0, l1):
    """
    Erstellt alle Kombinationen von String-Verkettungen aus zwei Listen.

    Args:
        l0: Erste Liste mit Strings
        l1: Zweite Liste mit Strings

    Returns:
        list: Liste mit allen Kombinationen u + v, wobei u aus l0 und v aus l1
    """
    kombinationen = []

    for u in l0:
        for v in l1:
            kombinationen.append(u + v)

    return kombinationen


# Test der Funktion
if __name__ == "__main__":
    # Beispiel-Daten
    liste1 = ["Hallo", "Guten", "Schönen"]
    liste2 = ["Welt", "Tag", "Morgen"]

    print(f"Liste 1: {liste1}")
    print(f"Liste 2: {liste2}")
    print()

    # Funktion aufrufen
    ergebnis = string_kombinationen(liste1, liste2)

    print("Alle String-Kombinationen:")
    print(ergebnis)
    print()
    print(f"Anzahl der Kombinationen: {len(ergebnis)}")

