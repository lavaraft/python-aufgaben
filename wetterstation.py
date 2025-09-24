
# Schritt 1: Daten in einer Liste speichern
temperaturen = [12, 14, 9, 12, 15, 16, 15, 15, 9, 8, 13, 13, 15, 12]
tage = list(range(1, 14))  # Tage 1 bis 14

# Schritt 2: Höchste und niedrigste Temperatur finden
hoechste_temp = temperaturen[0]
niedrigste_temp = temperaturen[0]
tag_hoechste = 1
tag_niedrigste = 1

for i in range(len(temperaturen)):
    if temperaturen[i] > hoechste_temp:
        hoechste_temp = temperaturen[i]
        tag_hoechste = i + 1
    if temperaturen[i] < niedrigste_temp:
        niedrigste_temp = temperaturen[i]
        tag_niedrigste = i + 1

# Schritt 3: Größten Temperaturumschwung finden
max_umschwung = 0
tag_umschwung = 1

for i in range(len(temperaturen) - 1):
    differenz = abs(temperaturen[i] - temperaturen[i + 1])
    if differenz > max_umschwung:
        max_umschwung = differenz
        tag_umschwung = i + 1  # Tag des ersten Tages des Paares

# Schritt 4: Ergebnisse anzeigen
print("=== WETTERAUSWERTUNG ===")
print(f"Temperaturen: {temperaturen}")
print(f"Höchste Temperatur: {hoechste_temp}°C am Tag {tag_hoechste}")
print(f"Niedrigste Temperatur: {niedrigste_temp}°C am Tag {tag_niedrigste}")
print(f"Größter Temperaturumschwung: {max_umschwung}°C zwischen Tag {tag_umschwung} und Tag {tag_umschwung + 1}")