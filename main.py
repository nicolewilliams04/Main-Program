import turtle # Draws the board using a "turtle"
import time # Used for turtle or functions to wait a couple seconds before doing
import os # Used to clear outputs

# Defining functions
def rules(): # Defines function to print the rules of the game, for player to see
 print("Mū Tōrere Rules:")
 print()
 print("\u2022 The object of the game is to make it impossible for your opponent to move.")
 print()
 print("\u2022 There are 3 types of legal moves: ")
 print("   \u2022 Sideways to the next adjacent arm end (1-8),")
 print("   \u2022 To the “putahi”, if it is empty,")
 print("   \u2022 From the “putahi” to any unoccupied adjacent arm,")
 print()
 print("\u2022 One player will be red and the other blue,")
 print("\u2022 Both players will take alternating moves until the game ends,")
 print("\u2022 The game is ended when one player is blocked in and cannot move. They lose the game and their opponent is declared the winner.")
 print()

def drawboard(): # Defining function to draw game board
 #Setting background size and colour
 turtle.setup(800, 600)
 wn = turtle.Screen()
 wn.bgcolor("white")
 # Sets turtle shape, colour and speed
 board = turtle.Turtle()
 board.shape("classic")
 board.color("black")
 board.speed("fastest")
 # Gets turtle ready and in position
 board.showturtle()
 board.clear
 board.penup()
 board.goto(0, 230)
 board.right(90)
 board.pendown()

 def eighth(): # Defining eighth funtion for turtle to draw eighth of a circle
   for _ in range(45): # Repeats code below 45 times to draw 1/8 of a circle
     board.right(1)
     board.forward(0.5)

 # Drawing the board
 os.system("clear")
 print("Loading game board...") # To give off a loading effect whilst drawing board as it takes a couple seconds
 # Segments of the board
 board.forward(200)
 board.left(90)
 for _ in range(8): # Repeats 8 times to draw the line segments of the star shape centre
   eighth() # Uses function
   board.left(90)
   board.forward(200)
   board.backward(200)
   board.right(90)
 board.left(90)
 board.forward(200)
 # Outer-lining of board
 for _ in range(8): # Repeats 8 times to outline the board star shape, connecting the dots and drawing the circle positions
   board.right(90) # Setting position so turtle can draw circle from the centre instead of to the right or left
   board.circle(27)
   board.right(67.5)
   board.forward(123.5)
   board.left(90)
   board.forward(123.5)
   board.left(22.5) # Reseting position to continue loop
 board.hideturtle()

def label(): # Labelling points of board (using point turtle)
  # Sets turtle shape, colour, style and speed
  point = turtle.Turtle()
  point.shape("classic")
  point.color("black")
  point.speed("fastest")
  style = ("Ariel", 10) # Sets font style
  # Labelling board
  point.penup()
  new_position_xy = [(-3, -6), (30, 230), (210, 155), (285, -27), (210, -207), (-35, -280), (-215, -207), (-290, -27), (-215, 155)] # Making a list of coordinates to label poitns
  x = -1 
  for i in new_position_xy: # Goes from one coordinate to the next and prints off number which +1 as it moves on
    point.goto(i)
    x = x+1
    point.write(x, font=style) 
  point.hideturtle()
  # Wraping things up
  os.system("clear") # Clears the ouput on text screen
  print("Game board completed - 100%")
  time.sleep(1) # Waits to clear output system so user can read above statement
  os.system("clear")

# Setting up dict for coverting word to numbers
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}

# Start-up
# Asking user if they'd like to play the game
play = None
while play not in ["y", "yes", "n", "no"]: # Used for the else code to repeat question if not answer with the above suggested answers
 play = input("Would you like to play my program Mū Tōrere? (Y/N) ")
 # play = "y"
 play = play.lower() # Converts the input to all lowercase so it's not case sensitive
 if play in ["y", "yes"]:
   os.system("clear")
   rules() # Uses previosuly defines rules function
 elif play in ["n", "no"]:
   print("Okay, have a nice day!")
   exit() # Stops the rest of the code if the user wished to not play thus "exit"-ing the game/code
 else:
   print()
   print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ")
   print()

# Setting up question to ask player to continue or not
cont = None
while cont not in ["y", "yes", "n", "no"]: # Used for the else code to repeat question if not answer with the above suggested answers
 cont = input("Do you wish to continue? (Y/N) ")
 # cont = "y"
 cont = cont.lower() # Converts the input to all lowercase so it's not case sensitive
 if cont in ["y", "yes"]:
   os.system("clear")
   drawboard() # Loads/draws board using previously defined function
   label() # Labels board using previously defined function
 elif cont in ["n", "no"]:
   print("Goodbye!")
   exit() # Stops the rest of the code if the user wished to not play thus "exit"-ing the game/code
 else:
   print()
   print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ")
   print()

# Setting positions of game pieces on board to specific coordinates
pos_0 = (0, 1)
pos_1 = (0, 257)
pos_2 = (180, 181.5)
pos_3 = (254.5, 1.5)
pos_4 = (180, -179)
pos_5 = (0, -253.5)
pos_6 = (-180, -179)
pos_7 = (-254.5, 1.5)
pos_8 = (-180, 181.5)

# Creating game pieces
# Player tahi
tahi = {}
for turtleName in ["a", "b", "c", "d"]: # For each for the letters in list, creates a turtle alocated to each letter and hides etc - listed below)
  tahi[turtleName] = turtle.Turtle()
  tahi[turtleName].hideturtle()
  tahi[turtleName].penup()
  tahi[turtleName].shape("circle")
  tahi[turtleName].color("red")
  tahi[turtleName].speed("fastest")
  tahi[turtleName].shapesize(2.25)

# Player rua
rua = {}
for turtleName in ["a", "b", "c", "d"]:  # For each for the letters in list, creates a turtle alocated to each letter and hides etc - listed below)
  rua[turtleName] = turtle.Turtle()
  rua[turtleName].hideturtle()
  rua[turtleName].penup()
  rua[turtleName].shape("circle")
  rua[turtleName].color("blue")
  rua[turtleName].speed("fastest")
  rua[turtleName].shapesize(2.25)

# Allocating game pieces to their starting positions
# Player tahi
tahi["a"].goto(pos_1)
tahi["b"].goto(pos_2)
tahi["c"].goto(pos_3)
tahi["d"].goto(pos_4)

# Player rua
rua["a"].goto(pos_5)
rua["b"].goto(pos_6)
rua["c"].goto(pos_7)
rua["d"].goto(pos_8)

# Showing all eight "tahi" and "rua" turtles after they've moved to their allocated positions
for turtleName in ["a", "b", "c", "d"]:
  tahi[turtleName].showturtle()
  rua[turtleName].showturtle()

# Creating a dictionary of variables for each position for later use - allocating turtles to positons for user
pos = {}
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
  pos[n] = "empty" # Setting the position to empty

# Setting a position to occupied by turtle
# Player tahi
for turtleName in ["a", "b", "c", "d"]:
  if tahi[turtleName].distance(pos_0) == 0:
    pos[0] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_1) == 0:
    pos[1] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_2) == 0:
    pos[2] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_3) == 0:
    pos[3] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_4) == 0:
    pos[4] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_5) == 0:
    pos[5] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_6) == 0:
    pos[6] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_7) == 0:
    pos[7] = tahi[turtleName]
  elif tahi[turtleName].distance(pos_8) == 0:
    pos[8] = tahi[turtleName]

# Player rua
for turtleName in ["a", "b", "c", "d"]:
  if rua[turtleName].distance(pos_0) == 0:
    pos[0] = rua[turtleName]
  elif rua[turtleName].distance(pos_1) == 0:
    pos[1] = rua[turtleName]
  elif rua[turtleName].distance(pos_2) == 0:
    pos[2] = rua[turtleName]
  elif rua[turtleName].distance(pos_3) == 0:
    pos[3] = rua[turtleName]
  elif rua[turtleName].distance(pos_4) == 0:
    pos[4] = rua[turtleName]
  elif rua[turtleName].distance(pos_5) == 0:
    pos[5] = rua[turtleName]
  elif rua[turtleName].distance(pos_6) == 0:
    pos[6] = rua[turtleName]
  elif rua[turtleName].distance(pos_7) == 0:
    pos[7] = rua[turtleName]
  elif rua[turtleName].distance(pos_8) == 0:
    pos[8] = rua[turtleName]

def ask_user_position(question,):
  while True: # Infinite loop
    user_position_response = input(question).lower()
    if user_position_response in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]:
      position = ''.join(help_dict[i] for i in user_position_response.split())
      position = int(position)
      return position # Break out of function and by extension the infinite loop
    elif user_position_response in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
      position = int(user_position_response)
      return position # Break out of function and by extension the infinite loop
    else:
      print()
      print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ")
      print()

turn = "Rua"
change_player = True
game_end = False
while game_end == False: # Infinite loop, break with "break" command
  if change_player: # Same as if change_player == True:
    turn = "Tahi" if turn != "Tahi" else "Rua" # Flip the user playing, this syntax is called a "Ternary operator"
    if turn == "Tahi":
      color = "red"
    else:
      color = "blue"
    change_player = False
    os.system("clear")
    print(f"It's {turn}'s turn! Your counters are " + color + ".") # This is an f-string and is a function in python 3. It allows variables inside a string.
    print()
  else:
    print(f"There was an issue with this move, please try again {turn}.")
    print()
  old_position = ask_user_position("What position is the counter you want to move at? ")
  new_position = [i for i, j in pos.items() if j == "empty"][0] # Find new_position (the empty space) using board state (pos) and python's list comprehention

  # In other programming languages they have a function called "switch", python doesn't implement this which is why this is required.
  if new_position == 0:
    new_position_xy = pos_0
  elif new_position == 1:
    new_position_xy = pos_1
  elif new_position == 2:
    new_position_xy = pos_2
  elif new_position == 3:
    new_position_xy = pos_3
  elif new_position == 4:
    new_position_xy = pos_4
  elif new_position == 5:
    new_position_xy = pos_5
  elif new_position == 6:
    new_position_xy = pos_6
  elif new_position == 7:
    new_position_xy = pos_7
  elif new_position == 8:
    new_position_xy = pos_8

  # Move player logic
  current_player = tahi if turn == "Tahi" else rua # Ternary operator
  for turtleName in ["a", "b", "c", "d"]:
    if pos[old_position] == current_player[turtleName]:
      if pos[old_position].distance(new_position_xy) <= 256.0: # If the space between the turtle space and the new space is less than 256
        empty_position_xy = pos[old_position]._position # Stare the empty position
        pos[old_position].goto(new_position_xy) # Move turtle to new position
        pos[new_position] = current_player[turtleName] # Update board state
        pos[old_position] = "empty" # Update empty space in board state
        change_player = True # It's the other person's turn now
        break # Stop for loop continuing

  # Check to see if winning conditions have been met
  if change_player:
    opponent = rua if turn == "Tahi" else tahi # Ternary operator
    # Check if next player can move at least one turtle to the empty spot
    can_move = False
    for turtleName in ["a", "b", "c", "d"]:
      distance_from_empty = opponent[turtleName].distance(empty_position_xy)
      if distance_from_empty <= 256.0:
        can_move = True # Can the oponent move to the empty space
        break
    if not can_move:
      print()
      print(f"Player {turn} wins!")
      game_end = True # While loop will break when this is set to true

print("Thanks for playing.")