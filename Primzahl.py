
def prime_checker(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:                 # 7(number) / 2(i)
            is_Prime = False                # 7(number) / 3(i)
    if is_Prime:                            # 7(number) / 4(i)
        print("Ist eine Primzahl")          # 7(number) / 5(i)
    else:                                   # 7(number) / 6(i)
        print("Keine Primzahl")             # 7(number) / 7(i)


Zahl = int(input("Gib eine Zahl ein: "))
prime_checker(Zahl)
