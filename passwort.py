password = input("Gib dein Passwort ein: ")

ist_lang_genug = len(password) >= 8
hat_min_zahl = any(char.isdigit() for char in password)
hat_min_sonderzeichen =  "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
hat_min_sonderzeichen = any(char in hat_min_sonderzeichen for char in password)


if ist_lang_genug and hat_min_zahl and hat_min_sonderzeichen: 
    print("Passwort ist stark")
else: 
    print("Passwort ist zu schwach")

