import random
def guess_the_number():
    def get_difficulty_level():
        print("Choose a difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")

        while True:
            try:
                choice = int(input("Enter the number for your chosen difficulty: "))
                if choice == 1:
                    return 1, 50
                elif choice == 2:
                    return 1, 100
                elif choice == 3:
                    return 1, 200
                else:
                    print("Invalid choice. Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_user_guess():
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a number.")

    best_score = None

    while True:
        print("Welcome to the number guessing game!")
        min_range, max_range = get_difficulty_level()
        number_to_guess = random.randint(min_range, max_range)
        attempts = 0
        guessed = False
        hints_provided = 0
        print(f"I have selected a number between {min_range} and {max_range}. Can you guess what it is:")
        
        while not guessed:
            user_guess = get_user_guess()
            attempts += 1

            if user_guess < number_to_guess:
                print("its low! Try again.")
            elif user_guess > number_to_guess:
                print("its high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print(f"New best score: {best_score} attempts!")
                else:
                    print(f"Your best score: {best_score} attempts!")

            if not guessed and attempts % 5 == 0:
                if number_to_guess % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")
                hints_provided += 1

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

guess_the_number()
  
              

