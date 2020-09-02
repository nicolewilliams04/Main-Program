#Pre Set-Up
play = None 
while play not in ["Y", "y", "Yes", "yes", "N", "n", "No", "no"]:  
  play = input("Would you like to play my program Mū Tōrere? (Y/N) ")
  if play in ["Y", "y", "Yes", "yes"]:
    print("rules")
  elif play in ["N", "n", "No", "no"]:
    print("Okay, have a nice day!")
    exit() 
  else: 
    print()
    print("Sorry, you must have inputted the wrong response. Please try again, with either Y or N. ") 
    print()