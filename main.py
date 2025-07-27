import ascii_art as art

import random

all_symbols = [art.rock, art.paper, art.scissor, art.lizard, art.spock]

comp_choice = random.randint(1,5)

# rock(1) > scissor and lizard
# paper(2) > spock and rock
# scissor(3) > lizard and paper
# lizard(4) > paper and spock
# spock(5) > rock and scissor

rock = 1
paper = 2
scissor = 3
lizard = 4
spock = 5
while True:
      player_choice = int(input("choose your symbol: \n"
                                "1. rock \n"
                                "2. paper \n"
                                "3. scissor \n"
                                "4. lizard \n"
                                "5. spock \n"
                                "0. to exit \n"
                                ))
      if player_choice == 0:
          break
      if player_choice  <= len(all_symbols) and player_choice > 0:      # checking if player has choose valid number
          if player_choice == comp_choice:
            print(f"Your choice is: \n {all_symbols[player_choice -1]}" )
            print(f"Computer choice is: \n {all_symbols[comp_choice -1]}" )
            print("DRAW!!!")
          # player win conditions
          elif player_choice == rock and (comp_choice == scissor or comp_choice == lizard ):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You WIN!!!")
          elif player_choice == paper and (comp_choice == spock or comp_choice == rock ):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You WIN!!!")
          elif player_choice == scissor and (comp_choice == lizard or comp_choice == paper):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You WIN!!!")
          elif player_choice == lizard and (comp_choice == paper or comp_choice == spock):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You WIN!!!")
          elif player_choice == spock and (comp_choice == rock or comp_choice == scissor):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You WIN!!!")
          # comp win conditions
          elif comp_choice == rock and (player_choice == scissor or player_choice == lizard) :
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You Lose.")
          elif comp_choice == paper and (player_choice == spock or player_choice == rock) :
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You Lose.")
          elif comp_choice == scissor and (player_choice == lizard or player_choice == paper):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You Lose.")
          elif comp_choice == lizard and (player_choice == paper or player_choice == spock):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You Lose.")
          elif comp_choice == spock and (player_choice == rock or player_choice == scissor):
            print(f"Your choice is: \n {all_symbols[player_choice - 1]}")
            print(f"Computer choice is: \n {all_symbols[comp_choice - 1]}")
            print("You Lose.")
      else:
            print("enter a valid choice \n")

