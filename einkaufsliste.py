foods = []
prices = []
total = []

while True:
    food = input("Eingabe um Lebensmittel zu kaufen (q um nicht): ")
    if food.lower == "q":
        break
    else:
        price = float(input(f"Eingabe preis von {food}: €"))
        foods.append(food)
        prices.append(price)

print("---- DEIN EINKAUFSWAGEN ----")

for food in foods: 
    print(food, end=" ") 


for price in prices:
    total += price

print()
print(f"Deine Gesamtsumme ist: €{total}") 