from random import randint

while True:
    choose = int(input("1 for head and 0 for tail: "))
    user_choice = int(input("Enter a value b/w 1-5: "))
    comp_choice = randint(1, 6)
    print(f"Comp Choice is:  {comp_choice}")
    score = comp_choice + user_choice

    if user_choice < 0 or user_choice > 5:
        print("Invalid choice. Please choose again.")
    elif score % 2 == 0 and score % 2 == choose:
        print("Its a tail. You won")
    elif score % 2 != 0 and score % 2 != choose:
        print("Its a Head. You Won")
    else:
        print("You lose.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
