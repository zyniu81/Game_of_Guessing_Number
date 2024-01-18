import random


def guessing_number():
    """Guessing game between the computer and the player.

       The function generates a random integer between 1 and 100, and prompts the player to guess the number.
       If the player's guess is too small, the function prints "Too small!".
       If the player's guess is too big, the function prints "Too big!".
       If the player's guess is correct, the function prints "You win!" and terminates the game.
       If the player's input is not a number, the function prints "It's not a number!".
       If the player interrupts the game, the function prints "Interrupted by the player" and terminates the game.

       Args:
           None

       Returns:
           None
       """
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
