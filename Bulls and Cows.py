"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - BULLs and COWs
author: Václav Kryštof
email: v.krystof@seznam.cz
discord: Vašek K.#0340
"""

import random

print("""
Hi there!
-------------------------------------------------------------
I've generated a random 4 digit number for you.
Guess a secret 4-digit number (except "0") with unique values
Let's play a bulls and cows game.
-------------------------------------------------------------""")

def nahodne_cislo(cisla: list):
    """
    Creates a unique 4-digit number from list of numbers
    """
    return random.sample(cisla, k=4)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_num = nahodne_cislo(a)
pocet_kol = 0

while True:
    akce = input("Zadej 4-místné číslo od 1-9, čísla se nesmí opakovat:")  # creates string
            
    if akce[0] == "0" or len(set(akce)) != 4 or not akce.isdigit():
        print(f"Zadáno: {akce}")
        print("Musí obsahovat jen čísla, nesmí obsahovat 0, nesmí být kratší/delší než 4 znaky")
        continue

    list_akce = [int(i) for i in akce]
            
    if list_akce == random_num:
        pocet_kol += 1
        print(f"Correct, you've guessed the right number: {akce}")
        print(f"Guessed in {pocet_kol} guesses!")
        print("-------------------------------------------------------------")
        break

    else:
        bull = []
        cow = []
        for x in range(0,4):
            if list_akce[x] == random_num[x]:
                bull.append((list_akce[x]))
            elif list_akce[x] not in bull and list_akce[x] in random_num:
                cow.append((list_akce[x]))
        pocet_kol += 1
                
    if len(bull) == 0 and len(cow) == 0:
        print("Bulls:", len(bull) , "Cows:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) == 0 and len(cow) == 1:
        print("Bulls:", len(bull), "Cow:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) == 0 and len(cow) > 1:
        print("Bulls:", len(bull), "Cows:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) == 1 and len(cow) == 1:
        print("Bull:", len(bull), "Cow:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) == 1 and len(cow) == 0:
        print("Bull:", len(bull), "Cows:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) == 1 and len(cow) > 1:
        print("Bull:", len(bull), "Cows:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) > 1 and len(cow) == 0:
        print("Bulls:", len(bull), "Cows:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) > 1 and len(cow) == 1:
        print("Bulls:", len(bull), "Cow:", len(cow))
        print("-------------------------------------------------------------")
    elif len(bull) > 1 and len(cow) > 1:
        print("Bulls:", len(bull), "Cows:", len(cow))
        print("-------------------------------------------------------------")
    bull.clear()
    cow.clear()
