adressbuch = []
while True:
    print("\n--- Mini-Adressbuch ---") #\n -> Zeilenumbruch
    print("1. Kontakt hinzufügen")
    print("2. Kontakte anzeigen")
    print("3. Nach Name suchen")
    print("3. Kontakte löschen")
    print("5. Beenden")

    wahl = input("Wähle eine Option (1-5): ")

    if wahl == "1":
        name = input("Name: ")
        telefon = input("telefon: ")
        email = input("E-Mail: ")
        kontakt = {"Name": name, "Telefon": telefon, "E-Mail": email}
        adressbuch.append(kontakt)
        print(f"{name} wurde hinzugefügt.")
    elif wahl == "2":
        print("\nAlle Kontakte:")
        for kontakt in adressbuch:
            print(f"{kontakt['Name']} - {kontakt['Telefon']} - {kontakt['E-Mail']}")
    elif wahl == "3":
        suche = input("Nach welchem Namen suchen? ")
        gefunden = False
        for kontakt in adressbuch:
            if kontakt["Name"].lower() == suche.lower():
                print(f"Gefunden: {kontakt['Name']} - {kontakt['Telefon']} - {kontakt['E-Mail']}")
                gefunden = True
        if not gefunden:
            print("Kein Kontakt gefunden.")
    elif wahl == "4":
        loesche = input("Welchen Kontakt löschen? ")
        gefunden = False
        for kontakt in adressbuch:
            if kontakt["Name"].lower() == loesche.lower():
                adressbuch.remove(kontakt)
                print(f"{kontakt['Name']} wurde gelöscht.")
                gefunden = True
                break
        if not gefunden:
            print("Kontakt nicht gefunden.")
    elif wahl == "5":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Option. Bitte 1-5 wählen.")