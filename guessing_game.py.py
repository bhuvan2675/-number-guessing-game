import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_score = 100

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                
                score = max(max_score - (attempts - 1) * 10, 0)
                print(f"Correct! You guessed it in {attempts} attempts.")
                print(f" Your score: {score}/100")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


number_guessing_game()
