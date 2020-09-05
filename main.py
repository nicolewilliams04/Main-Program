import turtle
import time
import os
#maybe import curses - ables to position text on screen - input by number
 
#Pre Set-Up
def rules(): #Defines function to print the rules of the game, for user to see
 print("Mū Tōrere Rules:")
 print()
 print("\u2022 The object of the game is to make it impossible for your opponent to move.")
 print()
 print("\u2022 There are 3 types of legal moves: ")
 print("   \u2022 Sideways to the next adjacent square (1-8),")
 print("   \u2022 To the “putahi”, if it is empty,")
 print("   \u2022 From the “putahi” to any unoccupied adjacent point,")
 print()
 print("\u2022 One player will be either “X” and the other “O” or one red and the other blue,")
 print("\u2022 Both players will take alternating moves until the game ends,")
 print("\u2022 The game is ended when one player is blocked in and cannot move. He loses the game and his opponent is declared the winner.")
 print()
 
#Defining function to draw game board
def drawboard():
 #Setting background size and colour
 turtle.setup(800, 600)
 wn = turtle.Screen()
 wn.bgcolor("white")
 #Sets turtle shape, colour and speed
 board = turtle.Turtle()
 board.shape("classic")
 board.color("black")
 board.speed("fastest")
 #Gets turtle ready and in position
 board.showturtle()
 board.clear
 board.penup()
 board.goto(0, 230)
 board.right(90)
 board.pendown()
 #Defining eighth funtion for turtle to draw eighth of a circle
 def eighth():
   for i in range(45):
     board.right(1)
     board.forward(0.5)
 #Drawing board
 print("Loading game board...") #To give off a loading effect whilst drawing board as it takes a couple seconds
 #Segments of the board
 board.forward(200)
 board.left(90)
 for i in range(8):
   eighth() #Uses function
   board.left(90)
   board.forward(200)
   board.backward(200)
   board.right(90)
   board.left(90)
   board.forward(200)
 #Outer-lining of board
 for i in range(8):
   board.right(90) #Setting position so turtle can draw circle from the centre instead of to the right or left
   board.circle(27)
   board.right(67.5)
   board.forward(123.5)
   board.left(90)
   board.forward(123.5)
   board.left(22.5) #Reseting position to continue loop
  board

#Defining to label board
#Labelling points of board (using point turtle)
def label():
  #Sets turtle shape, colour, style and speed
  #Setting turtle to label board positions
  point = turtle.Turtle()
  point.shape("classic")
  point.color("black")
  point.speed("fastest")
  style = ("Ariel", 10)
  #Labelling board
  point.penup()
  xy = [(-3, -6), (30, 230), (210, 155), (285, -27), (210, -207), (-35, -280), (-215, -207), (-290, -27), (-215, 155)]
  x = -1
  for i in xy:
    point.goto(i)
    x = x+1
    point.write(x, font=style)
  point.hideturtle()
  #Wraping things up
  os.system("clear")
  print("Game board completed - 100%")
  time.sleep(1)
  os.system("clear")
 
#Asking user if they'd like to play the game
play = None
while play not in ["Y", "y", "Yes", "yes", "N", "n", "No", "no"]: #Used for the else code to repeat question if not answer with the above suggested answers
 play = input("Would you like to play my program Mū Tōrere? (Y/N) ")
 if play in ["Y", "y", "Yes", "yes"]:
   os.system("clear")
   rules()
 elif play in ["N", "n", "No", "no"]:
   print("Okay, have a nice day!")
   exit() #Stops the rest of the code if the user wished to not play thus "exit"-ing the game/code
 else:
   print()
   print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ")
   print()
 
#Setting up question to ask player to continue or not
cont = None
while cont not in ["Y", "y", "Yes", "yes", "N", "n", "No", "no"]: #Used for the else code to repeat question if not answer with the above suggested answers
 cont = input("Do you wish to continue? (Y/N) ")
 if cont in ["Y", "y", "Yes", "yes"]:
   os.system("clear")
   drawboard() #Loads/draws board
   label()
 elif cont in ["N", "n", "No", "no"]:
   print("Goodbye!")
   exit() #Stops the rest of the code if the user wished to not play thus "exit"-ing the game/code
 else:
   print()
   print("Sorry, you must have inputted the wrong response. Please try again, with a more appropriate answer. ")
   print()
 
#give rules for moving and recap