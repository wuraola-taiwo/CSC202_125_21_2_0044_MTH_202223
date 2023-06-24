# Number Guessing Game
import random
def game():
    print("Welcome to my number guessing game: ")
    print("Im thinking of a number between 1 and 100")

    # Pick a random number
    number = random.randint(1, 100)
    print(number)

    # Difficulty
    def difficulty():
        guesses = 0

        difficulty = input("Choose a Difficulty, 'easy' or 'hard': ").lower()
    
    
        if difficulty == 'easy':
            guesses = 10
            print(f"You have {guesses} attempts to guess the number")
            return guesses
            
        elif difficulty == 'hard':
            guesses = 5
            print(f"You have {guesses} attempts to guess the number")
            return guesses
            
        else:
                print("Enter a valid choice")
    guesses = difficulty()


    playing = True
    
    while playing:

        # guessing
        choice = int(input("Guess a number: "))

        
        if choice == number:
            print("You Guessed The Correct Number🎉🎉")
            playing = False

        # Accuracy
        elif choice > number:
            print("Too high")
            guesses -= 1
            print(f"you have {guesses} guesses left")
        
        elif choice < number:
            print("Too low")
            guesses -= 1
            print(f"you have {guesses} guesses left")

        if guesses == 0:
            print("You lose")
            playing = False

game()