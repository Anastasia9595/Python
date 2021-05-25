import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Herzlich Wilkommen zu deinem Passwortgenerator")
Anzahl_der_Buchstaben = int(input("Wie viel Buchstaben soll dein Passwort haben?"))
Anzahl_der_Symbole = int(input("Wie viele Symbole soll dein Passwort haben?"))
Anzahl_der_Zahlen = int(input("Wie viele Zahlen soll dein Passwort haben?"))

Passwort = []

for i in range(1, Anzahl_der_Buchstaben + 1):
    Passwort.append(random.choice(letters))
for i in range(1, Anzahl_der_Symbole + 1):
    Passwort += random.choice(symbols)
for i in range(1, Anzahl_der_Zahlen + 1):
    Passwort += random.choice(numbers)

random.shuffle(Passwort)


password = ""

for i in Passwort:
    password += i

print(f"Dein Passwort lauetet: {password}")




