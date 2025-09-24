a = int(input("Geben Sie die Zahl a ein: "))
b = int(input("Geben Sie die Zahl b ein: "))

# Fehlerquellen berücksichtigen
if b == 0:
    print("Fehler: Division durch Null ist nicht erlaubt!")
elif a < 0 or b < 0:
    print("Fehler: Nur positive Zahlen sind erlaubt!")
else:
    quotient = 0
    rest = a
    
    while rest >= b:        # Solange Rest größer/gleich b
        rest -= b          # Subtrahiere b vom Rest
        quotient += 1      # Erhöhe Quotient um 1
    
    print(f"{a} / {b} = {quotient} Rest {rest}")