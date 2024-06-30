import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.CYAN+"Welcome to the Find the Treasure Game")
player = input(Fore.YELLOW + "Please enter your name: ")
player=player.upper()


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map=[line1,line2,line3]
print(f"{line1}\n{line2}\n{line3}")

abc=["A","B","C"]
randomletter=random.choice(abc)
randomnumber=random.randint(1,len(abc)-1)

treasure=randomletter+str(randomnumber)
letter=treasure[0]
letter_index=abc.index(letter)
number_index=int(treasure[1])-1

map[number_index][letter_index]="X"
print(Fore.CYAN + "\n-*--*--*--*--*--*--*--*--*--*-\n")

print(Fore.YELLOW + f"Lets find the treasure {player}!")
playerchoice=input(Fore.YELLOW + f"Hey {player} make a choice: (e.g., A1, C3)")
playerchoice=playerchoice.upper()
if playerchoice==randomletter+str(randomnumber):
    print(Fore.CYAN + "\n-*--*--*--*--*--*--*--*--*--*-\n")
    print(Fore.GREEN + f"YOU FIND IT! CONGRATULATIONS {player}!")
    print(f"{line1}\n{line2}\n{line3}")
    print(Fore.MAGENTA + f"Computer choice is: {randomletter + str(randomnumber)}")
else:
    print(Fore.CYAN + "\n-*--*--*--*--*--*--*--*--*--*-\n")
    print(Fore.RED + "TRY AGAIN!")
    print(Fore.YELLOW + f"Your choice is: {playerchoice}")
    print(f"{line1}\n{line2}\n{line3}")
    print(Fore.MAGENTA + f"Computer choice is: {randomletter + str(randomnumber)}")
