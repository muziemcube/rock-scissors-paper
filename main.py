import random

game_on=True

game_list=["rock", "paper", "scissors"]


while game_on:
    user_input=input('please enter any of: "rock", "paper", "scissors"').lower()
    random.shuffle(game_list)
    computer_value=game_list[0]
    #Decision

    if user_input==computer_value:
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nThe game is drawn")
    elif user_input=="rock" and computer_value=="scissors":
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nPlayer has won!")
    elif user_input=="rock" and computer_value=="paper":
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nPlayer has lost!, Computer Won! Paper covers rock")
    elif user_input=="paper" and computer_value=="rock":
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nPlayer has won!")
    elif user_input=="paper" and computer_value=="scissors":
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nPlayer has lost!, Computer Won!")
    elif user_input=="scissors" and computer_value=="paper":
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nPlayer has won!")
    elif user_input=="scissors" and computer_value=="rock":
        print(f"The user_value is : {user_input} and the computer_value is : {computer_value}")
        print("\nPlayer has lost!, Computer Won!")

    print("\nDo you want to continue the game. Type Yes if you want to continue else No")

    if user_input[0].lower()=='y':
        game_on
    else:
        if user_input[0].lower()=='n':
            game_on=False