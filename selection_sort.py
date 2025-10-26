"""
Task 3: Python Recap - Selection Sort
Implementierung von Selection Sort ohne Verwendung von Sortier-Bibliotheken.
"""

import numpy as np


def selsort(arr):
    """
    Sortiert ein Array oder eine Liste mit Selection Sort (absteigend).

    Der Algorithmus findet in jedem Schritt das Maximum und tauscht es an die
    richtige Position.

    Args:
        arr: Liste oder numpy Array zum Sortieren

    Returns:
        Sortierte Version des Arrays (absteigend)
    """
    # Konvertiere zu Liste für einheitliche Handhabung
    if isinstance(arr, np.ndarray):
        result = arr.tolist()
    else:
        result = arr.copy()

    n = len(result)

    # Äußere Schleife: Durchläuft die Positionen von oben nach unten
    for i in range(n):
        # Finde das Maximum in den verbleibenden Elementen
        max_idx = i

        # Innere Schleife: Suche das Maximum in arr[i:n]
        for j in range(i + 1, n):
            if result[j] > result[max_idx]:
                max_idx = j

        # Tausche das gefundene Maximum an Position i
        result[i], result[max_idx] = result[max_idx], result[i]

    # Wenn Input numpy array war, gebe numpy array zurück
    if isinstance(arr, np.ndarray):
        return np.array(result)

    return result


def insertion_sort(arr):
    """
    Alternative Implementierung: Insertion Sort

    Der Algorithmus baut eine sortierte Liste auf, indem jedes Element
    an der richtigen Position eingefügt wird.

    Args:
        arr: Liste oder numpy Array zum Sortieren

    Returns:
        Sortierte Version des Arrays (aufsteigend)
    """
    # Konvertiere zu Liste für einheitliche Handhabung
    if isinstance(arr, np.ndarray):
        result = arr.tolist()
    else:
        result = arr.copy()

    n = len(result)

    # Durchlaufe das Array ab dem zweiten Element
    for i in range(1, n):
        key = result[i]
        j = i - 1

        # Verschiebe Elemente größer als key eine Position nach rechts
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        # Füge key an der richtigen Position ein
        result[j + 1] = key

    # Wenn Input numpy array war, gebe numpy array zurück
    if isinstance(arr, np.ndarray):
        return np.array(result)

    return result


# Tests und Demonstrationen
if __name__ == "__main__":
    print("=" * 60)
    print("Task 3: Selection Sort und Insertion Sort")
    print("=" * 60)

    # Test 1: Liste mit ganzen Zahlen
    print("\n1. Test mit Liste von Integers:")
    test_liste = [64, 25, 12, 22, 11, 90, 88, 45, 50, 34]
    print(f"   Original: {test_liste}")
    sortiert = selsort(test_liste)
    print(f"   Selection Sort (absteigend): {sortiert}")

    # Test 2: Numpy Array
    print("\n2. Test mit Numpy Array:")
    test_array = np.array([3.14, 2.71, 1.41, 1.73, 0.58, 9.81, 6.28])
    print(f"   Original: {test_array}")
    sortiert_array = selsort(test_array)
    print(f"   Selection Sort (absteigend): {sortiert_array}")

    # Test 3: Insertion Sort
    print("\n3. Test Insertion Sort (aufsteigend):")
    test_liste2 = [64, 25, 12, 22, 11, 90, 88, 45, 50, 34]
    print(f"   Original: {test_liste2}")
    sortiert_ins = insertion_sort(test_liste2)
    print(f"   Insertion Sort (aufsteigend): {sortiert_ins}")

    # Test 4: Bereits sortierte Liste
    print("\n4. Test mit bereits sortierter Liste:")
    sortierte_liste = [1, 2, 3, 4, 5]
    print(f"   Original: {sortierte_liste}")
    print(f"   Selection Sort: {selsort(sortierte_liste)}")

    # Test 5: Liste mit einem Element
    print("\n5. Test mit einzelnem Element:")
    einzeln = [42]
    print(f"   Original: {einzeln}")
    print(f"   Selection Sort: {selsort(einzeln)}")

    # Test 6: Leere Liste
    print("\n6. Test mit leerer Liste:")
    leer = []
    print(f"   Original: {leer}")
    print(f"   Selection Sort: {selsort(leer)}")

    # Test 7: Liste mit Duplikaten
    print("\n7. Test mit Duplikaten:")
    duplikate = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"   Original: {duplikate}")
    print(f"   Selection Sort: {selsort(duplikate)}")
    print(f"   Insertion Sort: {insertion_sort(duplikate)}")

    # Performance Vergleich für größere Arrays
    print("\n8. Test mit größerem Array (100 Elemente):")
    großes_array = np.random.randint(1, 1000, 100)
    print(f"   Original (erste 10): {großes_array[:10]}")
    sortiert_groß = selsort(großes_array)
    print(f"   Sortiert (erste 10): {sortiert_groß[:10]}")
    print(f"   Sortiert (letzte 10): {sortiert_groß[-10:]}")

    print("\n" + "=" * 60)
    print("Alle Tests abgeschlossen!")
    print("=" * 60)
"""
E1.1 - Listen, for/while loops, mehrere Ausgaben
Implementiere eine Funktion, welche eine Liste mit float werten und einen Floatwert u 
als Eingaben akzeptiert, und zwei Kopien der Liste ausgibt: einmal die Listenwerte 
mit dem Wert u addiert, und einmal Listenwerte mit dem Wert u subtrahiert.
"""

def add_subtract_value(liste, u):
    """
    Addiert und subtrahiert einen Wert u von allen Elementen einer Liste.

    Args:
        liste: Liste mit float-Werten
        u: Float-Wert zum Addieren/Subtrahieren

    Returns:
        tuple: (liste_addiert, liste_subtrahiert)
    """
    liste_addiert = []
    liste_subtrahiert = []

    for wert in liste:
        liste_addiert.append(wert + u)
        liste_subtrahiert.append(wert - u)

    return liste_addiert, liste_subtrahiert


# Test der Funktion
if __name__ == "__main__":
    # Beispiel-Daten
    test_liste = [1.5, 2.0, 3.5, 4.0, 5.5]
    u_wert = 2.5

    print(f"Original Liste: {test_liste}")
    print(f"Wert u: {u_wert}")
    print()

    # Funktion aufrufen
    addiert, subtrahiert = add_subtract_value(test_liste, u_wert)

    print(f"Liste mit u addiert: {addiert}")
    print(f"Liste mit u subtrahiert: {subtrahiert}")

