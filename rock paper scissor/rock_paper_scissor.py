import random

game = ["Rock", "Paper", "Scissors"]
computer = game[random.randint(0, 2)]

player = True
while player == True:
    player = input("Rock Paper or Scissor? ('I quit' to leave the game) ")
    if player == 'I quit':
        print("Thank you for playing")
        break
    elif player.lower() == computer.lower():
        print (f"the computer choice was: {computer.title()}")
        print("Game Tied")
    elif player.lower() == "rock" :
        print (f"the computer choice was: {computer.title()}")
        if computer.lower() == "paper":
            print("You lose")
        else:
            print("You win")
    elif player.lower() == "scissor" :
        print (f"the computer choice was: {computer.title()}")
        if computer.lower() == "rock":
            print("You lose")
        else:
            print("You win")
    elif player.lower() == "paper" :
        print (f"the computer choice was: {computer.title()}")
        if computer.lower() == "scissor":
            print("You lose")
        else:
            print("You win")
    else:
        print("Please insert a valid play")
    player = True
    computer = game[random.randint(0, 2)].lower()
    
