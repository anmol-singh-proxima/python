"""

Here is a game in which admin has selected a number and user(or player) has to guess the number by inputting it.
There are a total of 10 number of guesses fo the user
User will type a number then program will check if the number is correct or not

If number is not correct then,
1) If entered number is smaller than the selected number then print entered number is smaller
2) If entered number is greater than the selected number then print entered number is greater
It will keep on going until the Game gets Over
Game will over if user tell the correct number or he use up all his guesses

If player tells the correct number then congratulate him by printing the number of guesses he took to complete it
Or if the player crosses the limit of 10 guesses then "Game Over!" will be printed

"""


def guess_number():
    selected_number = 44  # this is the selected number, it can be any number
    num_of_guess = 0  # for keeping the count of the number of guesses
    flag = 0  # if user guess the number right then flag will become 1

    while num_of_guess < 10:
        num_of_guess += 1
        num = int(input("Guess a number from 1 to 100: "))

        if num == selected_number:
            print("Congratulations! You guessed it right.")
            print(f"The number is {num}")
            print(f"You took {num_of_guess} guesses.")
            print(f"Your score is {10 - num_of_guess + 1}.")
            flag = 1
            break
        elif num < selected_number:
            print("Guess a greater number!")
        elif num > selected_number:
            print("Guess a smaller number!")

        if abs(num - selected_number) > 30:
            print("You are very far from the right number")
        elif abs(num - selected_number) > 20:
            print("You are far from the right number.")
        elif abs(num - selected_number) > 10:
            print("You are coming closer to the right number.")
        elif abs(num - selected_number) > 5:
            print("You are very close to the right number.")
        elif abs(num - selected_number) <= 5:
            print("You are very very close to the right number. You can guess it right!")

        print(f"You have {10 - num_of_guess} guesses left.\n")

    if num_of_guess == 10 and flag == 0:
        print("Bad Luck! You did not guess right.")
        print("You have reached the limit.\nGame Over!")
        print("Better luck next time")


if __name__ == '__main__':
    guess_number()
