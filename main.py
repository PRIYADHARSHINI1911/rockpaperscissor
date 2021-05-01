import random
print("Hey there!!!Welcome to Rock Paper Scissor")
print("If you want to complete this game,enter end game")
print("Let's Start??")
uservalue=input("Enter Yes if you want to play or enter Exit if you don't want to play: ")
userpoint = 0
computerpoint = 0
if uservalue!="yes":
    print("You exited")
while(uservalue=="yes"):
     print("Be Ready")
     print("-------------------------------------------------------------------------------------------")
     rps1 = ["rock", "paper", "scissor"]
     computer = (random.choice(rps1[0:3]))
     print("Computer played and it's your turn")


     game = input("Enter 'rock' or 'paper' or 'scissor':")

     if game==computer:
         print("Tie match")
         print("-------------------------------------------------------------------------------------------")
         print("Next turn!!!")

     elif (game=="rock" and computer=="paper") or (game=="paper" and computer=="scissor") or (game=="scissor" and computer=="rock"):
         computerwon="Computer won"
         computerpoint = computerpoint + 1
         print(computerwon)
         print("Computer point:",computerpoint)
         print("-------------------------------------------------------------------------------------------")
         print("Next turn!!!")

     elif (game == "rock" and computer == "scissor") or (game == "scissor" and computer == "paper") or (
             game == "paper" and computer == "rock"):
         userwon = "You won"
         userpoint = userpoint + 1
         print(userwon)
         print("Your point:", userpoint)
         print("-------------------------------------------------------------------------------------------")
         print("Next turn!!!")

     elif (game=="end game"):
         print("You ended the game")
         print("Your points:",userpoint)
         print("Computer points:",computerpoint)
         print("--------------------------------------------------------------------------------------------")
         if userpoint>computerpoint:
             print("***************** You won *****************")
         elif(userpoint<computerpoint):
             print("***************** Computer won *****************")
         elif(userpoint==computerpoint):
             print("***************** It is a tie match *****************")
         break
     else:
         print("enter valid input")
         print("Next turn!!!")













