import random


min_number = 1
max_number = 100
computer_list = []
user_list_min = []
user_list_max = []


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
    try:
        global computer_list
        global user_list_min
        global user_list_max
        while True:
            user_input = int(input("Guess the number between 1 and 100: "))
            computer = random.randint(min_number, max_number)
            if user_input < min_number or user_input > max_number:
                user_input = int(input("Guess the number between 1 and 100: "))
            else:
                computer_list.append(computer)
            if user_input < computer_list[0]:
                print("Too small")
                user_list_min.append(user_input)
            elif user_input > computer_list[0]:
                print("Too big")
                user_list_max.append(user_input)
            elif user_input == computer_list[0]:
                print("You win")
                break
            else:
                print("It's not a number!")
    except ValueError:
        print("It's not a number!")
        return guessing_number()
    except KeyboardInterrupt:
        print("Interrupted by the player")


(guessing_number())
