print("Bitte geben Sie Ihre Adressdaten ein:")

vorname = input("Vorname: ")
name = input("Name: ")
strasse = input("Straße: ")
hausnummer = input("Hausnummer: ")
plz = input("PLZ: ")
ort = input("Ort: ")

print("\nAdresse:")
print("========")
print(f"{vorname} {name}")
print(f"{strasse} {hausnummer}")
print(f"{plz} {ort}")
