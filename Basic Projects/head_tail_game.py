"""
A simple head-tail game where the user guesses whether the sum of a random number
and their choice will be even or odd. The user wins if their guess matches the result.
"""

from random import randint

def main():
    while True:
        try:
            choose = int(input("Enter 1 for head and 0 for tail: "))
            user_choice = int(input("Enter a value between 1-5: "))
            
            if choose not in [0, 1]:
                print("Invalid choice. Please enter 0 for tail or 1 for head.")
                continue
            if user_choice < 1 or user_choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

            comp_choice = randint(1, 6)
            print(f"Computer choice is: {comp_choice}")
            score = comp_choice + user_choice
            result = "tail" if score % 2 == 0 else "head"

            if (choose == 1 and result == "head") or (choose == 0 and result == "tail"):
                print(f"It's a {result}. You won!")
            else:
                print(f"It's a {result}. You lose.")

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

