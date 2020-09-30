import turtle #Draws the board usinga "turtle"
import time #Used for turtle or functions to wait a couple seconds before doing
import os #Used to clear outputs 
#maybe import curses - ables to position text on screen - input by number
 
#Pre Set-Up
def rules(): #Defines function to print the rules of the game, for player to see
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
   for i in range(45): #Repeats code below 45 times to draw 1/8 of a circle
     board.right(1)
     board.forward(0.5)
 #Drawing board
 print("Loading game board...") #To give off a loading effect whilst drawing board as it takes a couple seconds
 #Segments of the board
 board.forward(200)
 board.left(90)
 for i in range(8): #Repeats 8 times to draw the line segments of the star shape centre
   eighth() #Uses function
   board.left(90)
   board.forward(200)
   board.backward(200)
   board.right(90)
 board.left(90)
 board.forward(200)
 #Outer-lining of board
 for i in range(8): #Repeats 8 times to outline the board star shape, connecting the dots and drawing the circle positions
   board.right(90) #Setting position so turtle can draw circle from the centre instead of to the right or left
   board.circle(27)
   board.right(67.5)
   board.forward(123.5)
   board.left(90)
   board.forward(123.5)
   board.left(22.5) #Reseting position to continue loop
 board.hideturtle()

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
  xy = [(-3, -6), (30, 230), (210, 155), (285, -27), (210, -207), (-35, -280), (-215, -207), (-290, -27), (-215, 155)] #Making a list of coordinates
  x = -1
  for i in xy: #Goes from one coordinate to the next and prints off number which +1 as it moves on
    point.goto(i)
    x = x+1
    point.write(x, font=style)
  point.hideturtle()
  #Wraping things up
  os.system("clear") #Clears the ouput on text screen
  print("Game board completed - 100%")
  time.sleep(1)
  os.system("clear")
 
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

#Setting positions of game pieces on board
pos_0 = (0, 1)
pos_1 = (0, 257)
pos_2 = (180, 181.5)
pos_3 = (254.5, 1.5)
pos_4 = (180, -179)
pos_5 = (0, -253.5)
pos_6 = (-180, -179)
pos_7 = (-254.5, 1.5)
pos_8 = (-180, 181.5)

#Creating game pieces
#Player tahi
#Creating four turtle game pieces for player one (tahi) using list
tahi = {}
for turtleName in ["a", "b", "c", "d"]:
  tahi[turtleName] = turtle.Turtle()
  tahi[turtleName].penup()
  tahi[turtleName].shape("circle")
  tahi[turtleName].color("red")
  tahi[turtleName].speed("fastest")
  tahi[turtleName].shapesize(2.25)
#Player rua
#Creating four turtle game pieces for player two (rua) using list
rua = {}
for turtleName in ["a", "b", "c", "d"]:
  rua[turtleName] = turtle.Turtle()
  rua[turtleName].penup()
  rua[turtleName].shape("circle")
  rua[turtleName].color("blue")
  rua[turtleName].speed("fastest")
  rua[turtleName].shapesize(2.25)
#Allocating game pieces to their starting positions
#Player tahi
tahi["a"].goto(pos_1)
tahi["b"].goto(pos_2)
tahi["c"].goto(pos_3)
tahi["d"].goto(pos_4)
#Player rua
rua["a"].goto(pos_5)
rua["b"].goto(pos_6)
rua["c"].goto(pos_7)
rua["d"].goto(pos_8)
 
