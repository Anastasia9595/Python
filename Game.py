# def my_function():
#    print("Hello")
#    print("Bye")

# my_function()

# Diese Schleife tut etwas mit jedem Item aus der Liste
# for item in list_of_item:

# Diese Schleife tut etwas mit allen Items in einer Range von x bis y
# for number in range(a,b)

# while Schleife macht etwas solnage die bedingung true ist

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

text = ['''
   ___                      ___  
 (o o)                    (o o) 
(  V  ) Du hast gewonnen (  V  )
--m-m----------------------m-m--
   ''', '''
 ()()                     ____ 
 (..)                    /|o  |
 /\/\  Du hast verloren /o|  o|
c\db/o................./o_|_o_|
                 
   ''']

WörterListe = ["Bus", "Auto", "Fahrrad"]

Wort = random.choice(WörterListe).lower()

display = []

for i in range(len(Wort)):
    display.append("_")

print(f"{' '.join(display)}")

end_of_game = False
Life = 6

while not end_of_game:

    chosen_char = input("Bitte gebe einen Buchstaben aus: ").lower()
    if not chosen_char.isalpha():
        print("Kein Gülriger Buchtabe!\n"
              "Du Verlierst ein Leben!")

    if chosen_char in display:
        print(f"Der Buchstabe {chosen_char} exisitiert bereits")

    for i in range(len(Wort)):
        letter = Wort[i]
        # print(f"Current positon {i} \n"
        #     f"Current letter: {chosen_char}")
        if letter == chosen_char:
            display[i] = letter

    if chosen_char not in Wort:
        print(f"Der Buchstabe {chosen_char} existiert nicht im gesuchten Wort.")
        Life -= 1
        print(f"Du hast nur noch {Life} versuche")
        print(stages[Life])

    if Life == 0:
        end_of_game = True
        print(text[1])

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(text[0])
