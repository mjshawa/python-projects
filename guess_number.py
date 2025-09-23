import random

def guess_the_number():
    """
    A simple guess-the-number game.
    """
    # 1. Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    
    # Initialize the guess and the attempt counter
    guess = 0
    attempts = 0

    print("Welcome to the Guess-the-Number game!")
    print("I've picked a number between 1 and 50. Can you guess it?")

    # 2. Use a while loop to allow the user to guess
    while guess != secret_number:
        try:
            # Get user input for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # 3. Provide hints: "Too high" or "Too low"
            if guess < secret_number:
                print("Too low! Try again. 👎")
            elif guess > secret_number:
                print("Too high! Try again. 👎")
            else:
                # The user guessed correctly
                print(f"Congratulations! You guessed the number {secret_number} correctly! 🎉")
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

    # 4. Print the total number of attempts when guessed correctly
    print(f"It took you {attempts} attempts to guess the number. 🥳")
if __name__ == "__main__":
    guess_the_number()
