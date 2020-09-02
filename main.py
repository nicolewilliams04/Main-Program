import os

#Pre Set-Up
def rules(): #defines function to print the rules of the game, for user to see
  print("The rules for the game Mū Tōrere are:")
  print()
  print("\u2022 One player will be either “X” and the other “O” or one red and the other blue,")
  print("\u2022 The object of the game is to make it impossible for your opponent to move,")
  print("\u2022 There are only 3 types of legal moves: ")
  print("   \u2022 Sideways to the next adjacent square (1-8),")
  print("   \u2022 To the “putahi”, if it is empty,")
  print("   \u2022 From the “putahi” to any unoccupied adjacent point,")
  print("\u2022 No jumping,")
  print("\u2022 Both players will take alternating moves until the game ends,")
  print("\u2022 The game is ended when one player is blocked in and cannot move. He loses the game and his opponent is declared the winner.")
  print()

play = None 
while play not in ["Y", "y", "Yes", "yes", "N", "n", "No", "no"]: #used for the else code to repeat question if not answer with the above suggested answers
  play = input("Would you like to play my program Mū Tōrere? (Y/N) ")
  if play in ["Y", "y", "Yes", "yes"]:
    os.system("clear")
    rules()
  elif play in ["N", "n", "No", "no"]:
    print("Okay, have a nice day!")
    exit() #stops the rest of the code if the user wished to not play thus "exit"-ing the game/code
  else: 
    print()
    print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ") 
    print()

    cont = None 
while cont not in ["Y", "y", "Yes", "yes", "N", "n", "No", "no"]: #used for the else code to repeat question if not answer with the above suggested answers
  cont = input("Do you wish to continue? (Y/N) ")
  if cont in ["Y", "y", "Yes", "yes"]:
    print("insert game")
  elif cont in ["N", "n", "No", "no"]:
    print("Goodbye!")
    exit() #stops the rest of the code if the user wished to not play thus "exit"-ing the game/code
  else: 
    print()
    print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ") 
    print()