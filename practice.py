import random
game = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
player_point = 0

print("Snake, Water & Gun Game: \n")
print("S for Snake\nw for Water\ng for Gun\n")

while no_of_chance<chance:
    _input = input("Snake,Water,Gun : ")
    _random = random.choice(game)

    if _input==_random:
        print("Game Tie \n")

    elif _input=="s" and _random=="g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif _input=="s" and _random=="w":
        player_point = player_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("player wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif _input=="w" and _random=="s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif _input=="w" and _random=="g":
        player_point = player_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("player wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif _input=="g" and _random=="s":
        player_point = player_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("player wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif _input=="g" and _random=="w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    else:
        print("Invalid Input ")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game Over")

if computer_point>player_point:
    print("Computer Wins & You Loose")

if player_point>computer_point:
    print("You Win & Computer Loose")

elif computer_point==player_point:
    print("Game Tie")

print(f"your point is {player_point} and computer point is {computer_point}")



