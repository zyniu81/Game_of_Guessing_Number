import random


def guessing_number():
    while True:
        try:
            computer_number = random.randint(1, 100)
            player_number = int(input("Guess the number between 1 and 100: "))
            if player_number < 1 or player_number > 100:
                print("Please enter a number between 1 and 100")
            elif player_number < computer_number:
                print("Too small!")
            elif player_number > computer_number:
                print("Too big!")
            elif player_number == computer_number:
                print("You win!")
                break
            else:
                print("It's not a number!")
            return guessing_number()
        except ValueError:
            print("It's not a number!")
            return guessing_number()
        except KeyboardInterrupt:
            print("Interrupted by the player")
            break


(guessing_number())
