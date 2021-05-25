import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



Spiel=[rock,paper,scissors]

durchgang = 1

while durchgang < 11:


      print("Wilkommen zu einem Spiel\n"
            "Stein:0\n"
            "Papie:1\n"
            "Schere:2")
      user_choice=int(input("Bitte tätige hier deine Eingabe: "))
      if user_choice < 0 or user_choice >= 3:
            print("Bitte eine Gültige Zahl eingeben\n")
      else:
            print(f"Deine Auswahl: \n"
                  f"{Spiel[user_choice]}")



      computer_choice = random.randint(0,2)
      print(f"Der Pc Wählte: \n"
            f"{Spiel[computer_choice]}")

      if user_choice == 0 and computer_choice == 2:
            print("Du hast gewonnen\n")
      elif computer_choice == 0 and user_choice == 2:
            print("Du hast verloren\n")
      elif computer_choice > user_choice:
            print("Du hast verloren\n")
      elif computer_choice==user_choice:
            print("Gleichstand\n")
      elif user_choice == 1 and computer_choice == 0:
            print("Du hast gewonnen\n")
      elif user_choice == 2 and computer_choice == 1:
            print("Du hast gewonnen\n")

      durchgang += 1









