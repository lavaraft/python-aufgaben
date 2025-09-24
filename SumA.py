grenzwert = int(input("Geben Sie den Grenzwert g ein: "))
summe = 0
n = 0
anzahl = 0

while summe <= grenzwert:  # Kopfgesteuerte Schleife
    n += 1                # Erhöhe n um 1 (1, 2, 3, ...)
    summe += n            # Addiere n zur Summe
    anzahl += 1           # Zähle die Anzahl der Schritte

print(f"Summe: {summe}")
print(f"Anzahl der Glieder: {anzahl}")
print(f"Letzte Zahl n: {n}")