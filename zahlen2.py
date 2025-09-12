import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Zahlenratenspiel")
print(f"Wähle eine Zahl zwischen {lowest_num} und {highest_num}") #f" macht das lowest_num und highest_num als zahlen auftretten und nicht als wort

while is_running: 

    guess = input("Tippe deine Schätzung ein: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess < lowest_num or guess > highest_num:
            print("Zahl zu hoch")
            print(f"Bitte wähle eine Zahl zwischen {lowest_num} und {highest_num}") 
        elif guess < answer:
            print("Zu niedrig")
        elif guess > answer:
            print("Zu hoch")
        else:
            print(f"Richtig! Antwort lautet{answer}")
            print(f"Anzahl deiner Schätzungen: {guesses}")  
            is_running = False #boolean loop escape 
    else:
        print("Falsch")
        print(f"Bitte wähle eine Zahl zwischen {lowest_num} und {highest_num}") 
