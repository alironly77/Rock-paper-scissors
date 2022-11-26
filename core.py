import random


print("Welcome To Rock Paper Scissors Game 😀 ")
UserPoint = 0
ComputerPoint = 0
PossibleActions = ["Rock", "Paper","Scissors"]

while UserPoint < 3 and ComputerPoint < 3 :

    UserActions = input("Enter To Choice(Rock, Paper, Scissors): ")
    ComputerActions = random.choice(PossibleActions)
    if UserActions == ComputerActions:
        print(f"Both players selected {UserActions}. It's a tie!")
    elif UserActions == "Rock" and ComputerActions == "Scissors":
        UserPoint += 1
        print("Rock smashes scissors! You win!")
    elif UserActions == "Rock" and ComputerActions == "Paper":
        ComputerPoint += 1
        print("Paper covers rock! You lose.")
    elif UserActions == "Paper" and UserActions == "Rock":
        UserPoint += 1
        print("Paper covers rock! You win!")
    elif UserActions == "Paper" and ComputerActions == "Scissors":
        ComputerPoint += 1
        print("Scissors cuts paper! You lose.")
    elif UserActions == "Scissors" and ComputerActions == "Rock":
        ComputerPoint += 1
        print("Rock smashes scissors! You lose.")
    elif UserActions == "Scissors" and ComputerActions == "Paper":
        UserPoint += 1
        print("Scissors cuts paper! You win!")
    if UserPoint >= 3 :
        print("You Win 🥳")
    elif ComputerPoint >= 3 :
        print ("You lose 😕")

