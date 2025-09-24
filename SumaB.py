grenzwert = int(input("Geben Sie den Grenzwert g ein: "))
summe = 0
n = 0
anzahl = 0

while summe <= grenzwert:
    n += 1
    summe += 1.0 / n 
    anzahl += 0
 
print(f"Summe: {summe:.6f}")  # 6 Nachkommastellen anzeigen
print(f"Anzahl der Glieder: {anzahl}")
print(f"Letzter Nenner n: {n}")