"""
Task 2: Numpy Indexing
Verschiedene Numpy Indexing Übungen
"""

import numpy as np

def numpy_indexing_tasks():
    """Demonstriert verschiedene Numpy Indexing Operationen."""

    print("=" * 60)
    print("Task 2: Numpy Indexing")
    print("=" * 60)

    # Erstelle ein Beispiel-Array
    print("\n1. Erstelle ein 2D Array (5x5):")
    arr = np.arange(1, 26).reshape(5, 5)
    print(arr)

    # Indexing: Einzelne Elemente
    print("\n2. Zugriff auf einzelne Elemente:")
    print(f"   Element [0, 0]: {arr[0, 0]}")
    print(f"   Element [2, 3]: {arr[2, 3]}")
    print(f"   Element [-1, -1] (letztes Element): {arr[-1, -1]}")

    # Slicing: Zeilen und Spalten
    print("\n3. Slicing - Zeilen und Spalten:")
    print(f"   Erste Zeile: {arr[0, :]}")
    print(f"   Letzte Spalte:\n{arr[:, -1]}")
    print(f"   Zweite und dritte Zeile:\n{arr[1:3, :]}")

    # Slicing: Sub-Arrays
    print("\n4. Slicing - Sub-Arrays:")
    sub_array = arr[1:4, 1:4]
    print(f"   3x3 Sub-Array (Zeilen 1-3, Spalten 1-3):\n{sub_array}")

    # Boolean Indexing
    print("\n5. Boolean Indexing:")
    mask = arr > 15
    print(f"   Maske (Werte > 15):\n{mask}")
    print(f"   Gefilterte Werte: {arr[mask]}")

    # Fancy Indexing
    print("\n6. Fancy Indexing (mit Listen):")
    rows = [0, 2, 4]
    cols = [1, 3, 4]
    print(f"   Zeilen {rows}, alle Spalten:\n{arr[rows, :]}")
    print(f"   Spezifische Elemente [0,1], [2,3], [4,4]: {arr[rows, cols]}")

    # Bedingte Indexierung und Manipulation
    print("\n7. Bedingte Manipulation:")
    arr_copy = arr.copy()
    arr_copy[arr_copy % 2 == 0] = -1  # Setze alle geraden Zahlen auf -1
    print(f"   Array mit geraden Zahlen ersetzt durch -1:\n{arr_copy}")

    # 3D Array Beispiel
    print("\n8. 3D Array Indexing:")
    arr_3d = np.arange(24).reshape(2, 3, 4)
    print(f"   3D Array (2x3x4):\n{arr_3d}")
    print(f"   Erste 'Schicht': \n{arr_3d[0, :, :]}")
    print(f"   Element [1, 2, 3]: {arr_3d[1, 2, 3]}")

    # Erweiterte Operationen
    print("\n9. Erweiterte Array-Operationen:")
    arr2 = np.random.randint(1, 10, size=(4, 4))
    print(f"   Zufälliges 4x4 Array:\n{arr2}")
    print(f"   Diagonal-Elemente: {np.diag(arr2)}")
    print(f"   Transponiert:\n{arr2.T}")

    # Where-Funktion
    print("\n10. np.where() - Bedingte Auswahl:")
    result = np.where(arr > 12, arr * 2, arr)
    print(f"    Original Array:\n{arr}")
    print(f"    Werte > 12 verdoppelt, sonst unverändert:\n{result}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    numpy_indexing_tasks()

