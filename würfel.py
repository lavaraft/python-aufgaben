import random

# Punkte zählen
spieler_punkte = 0
computer_punkte = 0

print("Willkommen zum Würfelspiel!")

while True:
    input("\nDrücke Enter, um zu würfeln...")

    spieler_wurf = random.randint(1, 6) #randint zufällig eine zahl von 1- 6
    computer_wurf = random.randint(1, 6) #random zufallszahlen

    print(f"Du würfelst: {spieler_wurf}") #f" für text + variable
    print(f"Computer würfelt: {computer_wurf}")

    if spieler_wurf > computer_wurf:
        print("Du gewinnst diese Runde!")
        spieler_punkte += 1
    elif spieler_wurf < computer_wurf:
        print("Computer gewinnt diese Runde!")
        computer_punkte += 1
    else:
        print("Unentschieden!")

    print(f"Punkte: Du {spieler_punkte} - Computer {computer_punkte}")

    # Bonus: Erste 5 Siege gewinnen
    if spieler_punkte == 5:
        print("\nHerzlichen Glückwunsch! Du hast 5 Runden gewonnen und das Spiel gewonnen!")
        break
    elif computer_punkte == 5:
        print("\nComputer hat 5 Runden gewonnen. Du hast verloren!")
        break
