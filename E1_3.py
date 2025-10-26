"""
E1.3 - Dictionary mit zufälligen Werten
Initialisiere ein dictionary mit Paaren, welche aus einem zufaelligen string und
zufaelligen einem Float-wert bestehen. Schreibe eine Funktion, welche ein dictionary
als Eingabe nimmt, und jeden value-wert eines key-value paares quadriert, falls dieser
Wert eine float-Zahl ist, und dann das resultierende dictionary zurueckgibt.
"""

import random
import string

def erstelle_zufaelliges_dict(anzahl=5):
    """
    Erstellt ein Dictionary mit zufälligen String-Keys und Float-Values.

    Args:
        anzahl: Anzahl der Key-Value-Paare

    Returns:
        dict: Dictionary mit zufälligen Einträgen
    """
    zufalls_dict = {}

    for i in range(anzahl):
        # Zufälliger String (3-5 Zeichen)
        laenge = random.randint(3, 5)
        key = ''.join(random.choices(string.ascii_lowercase, k=laenge))

        # Zufälliger Float-Wert zwischen 0 und 100
        value = random.uniform(0, 100)

        zufalls_dict[key] = value

    return zufalls_dict


def quadriere_float_werte(input_dict):
    """
    Quadriert alle Float-Werte in einem Dictionary.

    Args:
        input_dict: Input-Dictionary

    Returns:
        dict: Dictionary mit quadrierten Float-Werten
    """
    ergebnis_dict = {}

    for key, value in input_dict.items():
        if isinstance(value, float):
            ergebnis_dict[key] = value ** 2
        else:
            ergebnis_dict[key] = value

    return ergebnis_dict


# Test der Funktionen
if __name__ == "__main__":
    # Zufälliges Dictionary erstellen
    print("Erstelle zufälliges Dictionary...")
    test_dict = erstelle_zufaelliges_dict(6)

    print("\nOriginales Dictionary:")
    for key, value in test_dict.items():
        print(f"  '{key}': {value:.2f}")

    # Float-Werte quadrieren
    quadriert_dict = quadriere_float_werte(test_dict)

    print("\nDictionary mit quadrierten Werten:")
    for key, value in quadriert_dict.items():
        print(f"  '{key}': {value:.2f}")

    # Zusätzlicher Test mit gemischten Typen
    print("\n--- Test mit gemischten Datentypen ---")
    gemischt_dict = {
        "float1": 2.5,
        "string": "hello",
        "float2": 3.0,
        "int": 42,
        "float3": 1.5
    }

    print("\nOriginales gemischtes Dictionary:")
    print(gemischt_dict)

    quadriert_gemischt = quadriere_float_werte(gemischt_dict)

    print("\nQuadriertes gemischtes Dictionary:")
    print(quadriert_gemischt)

