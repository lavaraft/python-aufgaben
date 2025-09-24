
print("Berechnung des Durchschnittsverbrauchs")
print("======================================")

strecke = float(input("Gefahrene Strecke in km: "))
verbrauch = float(input("Verbrauchter Sprit in Liter: "))

verbrauch_pro_100km = (verbrauch / strecke) * 100

print(f"\nDer Durchschnittsverbrauch beträgt: {verbrauch_pro_100km:.2f} Liter auf 100 km")