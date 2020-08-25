"""

**** Snake-Water-Gun Game ****

Rules of Game:
* This game is played between two players
* Each player has to select any one of the three things i.e. Snake, Water, Gun
* There are some fundamental:
  * Snake drinks Water
  * Water drowns Gun
  * Gun kills Snake
* So, when 1st player selects Snake and 2nd player selects Water then 1st player wins
* Similarly, when 1st player selects Water and 2nd player selects Gun then 1st player wins
* Again, when 1st player selects Gun and 2nd player selects Snake then 1st player wins

* So, in this program, user has to put number of turns(chances) he wants to play this game
* Then program will randomly select any of the three things
* And it will ask the user to enter his choice
* Then, it will check who won, and based on that it will create a score board
* At last, after the game is over, it will display who won the game

"""

import random

game_list = ['S', 'W', 'G']
game_list_full = ['Snake', 'Water', 'Gun']
user_score = 0
computer_score = 0
user_choices = []
computer_choices = []
total_turns = 0


def score_board():
    """This function displays the score board after the game is over"""
    global user_score, computer_score, computer_choices, user_choices, total_turns
    print("\n***************** SCORE BOARD *****************")
    print("{:11s}Computer's Choices  VS  Your Choices".format(" "))
    for i in range(total_turns):
        print("Turn {:2d} => {:^18s}{:6s}{:^12s}".format(i + 1, computer_choices[i], " ", user_choices[i]))
    print("\n***********************************************\n")
    print(f"Your score: {user_score}\nComputer's Score: {computer_score}")
    print("\n***********************************************\n")
    if user_score > computer_score:
        print("CONGRATULATIONS! You won the Game. PLAY AGAIN!")
    elif user_score < computer_score:
        print("SORRY! You lose the game. TRY AGAIN!")
    else:
        print("OFFOOO! Game is tie. PLAY AGAIN!")
    print("\n***********************************************")


def check_who_won(user_choice):
    """This function checks who won the current turn based on the inputs from the user"""
    global user_score, computer_score, computer_choices, user_choices
    computer_choice = random.choice(game_list)
    flag = ""
    remark = ""

    for i in range(3):
        if computer_choice == game_list[i]:
            computer_choices.append(game_list_full[i])
        if user_choice == game_list[i]:
            user_choices.append(game_list_full[i])

    if computer_choice == 'S':
        if user_choice == 'W':
            computer_score += 1
            flag = "c"
            remark = "Computer's Snake drank Your Water"
        elif user_choice == 'G':
            user_score += 1
            flag = "u"
            remark = "Your Gun killed Computer's Snake"
    elif computer_choice == 'W':
        if user_choice == 'G':
            computer_score += 1
            flag = "c"
            remark = "Computer's Water drowned Your Gun"
        elif user_choice == 'S':
            user_score += 1
            flag = "u"
            remark = "Your Snake drank Computer's Water"
    elif computer_choice == 'G':
        if user_choice == 'S':
            computer_score += 1
            flag = "c"
            remark = "Computer's Gun killed Your Snake"
        elif user_choice == 'W':
            user_score += 1
            flag = "u"
            remark = "Your Water drowned Computer's Gun"

    print(f"Computer Selected: {computer_choice}")
    if flag == "u":
        print("YOU WON!", end=" ")
    elif flag == "c":
        print("YOU LOSE!", end=" ")
    else:
        print("GAME TIE!", end=" ")

    if remark != "":
        print(remark)


def snake_water_gun_game():
    """This function starts the Snake-Water-Gun game"""
    global total_turns

    print("\n===============================================")
    print("======********* SNAKE WATER GUN *********======")
    print("===============================================")
    print("Game Rules:")
    print("In Snake VS Water: Snake Wins")
    print("In Water VS Gun  : Water Wins")
    print("In Snake VS Gun  : Gun Wins")
    print("\nComputer will select any one of the three and You too have to select one")
    print("Then, Computer will tell who won \"You or Computer\"")
    print("Are you excited for the game? LETS PLAY!")

    while True:
        print("\nHow many turns you want to play?")
        number = input("Select from 1 to 20: ")
        if number.isnumeric():
            number = int(number)
            if number <= 0 or number > 20:
                print("Enter correct input. Try Again!")
                continue
            else:
                print(f"\nYou have total of {number} turns to play.")
                break
        else:
            print("Enter correct input. Try Again!")

    total_turns = number
    turns = 0
    while turns < total_turns:
        print("\n===============================================")
        print("Select any one by typing")
        print("S for Snake\nW for Water\nG for Gun")
        choice = input("Enter your choice: ")
        choice = choice.upper()
        if choice not in game_list:
            print("Wrong Input. Try Again!")
            continue
        turns += 1
        check_who_won(choice)
        if turns < total_turns:
            print(f"{total_turns - turns} turns left")

    if turns == total_turns:
        print("\nGAME OVER!")
        score_board()


if __name__ == "__main__":
    snake_water_gun_game()
