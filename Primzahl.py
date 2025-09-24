zahl = int(input("Geben Sie eine Zahl ein: "))

# Sonderfälle direkt behandeln
if zahl <= 1:                           #kleiner als oder gleich groß
    print(f"{zahl} ist keine Primzahl")
elif zahl == 2:                         #gleich 
    print(f"{zahl} ist eine Primzahl")
elif zahl % 2 == 0:  # gerade Zahlen > 2 sind keine Primzahlen  # % Modulo operator -> gibt Rest einer Division zurück 
    print(f"{zahl} ist keine Primzahl")
else:
    # Optimierte Prüfung
    ist_prim = True
    teiler = 3
    
    while teiler * teiler <= zahl:  # Nur bis zur Wurzel prüfen
        if zahl % teiler == 0:      # Wenn teilbar
            ist_prim = False
            break                  # Frühzeitig abbrechen
        teiler += 2                # Nur ungerade Teiler prüfen
    
    if ist_prim:
        print(f"{zahl} ist eine Primzahl")
    else:
        print(f"{zahl} ist keine Primzahl")