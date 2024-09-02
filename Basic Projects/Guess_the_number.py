import random

print('''
 
    _     _  _  _   __   _              _  _  _
   / `/ //_`/_`/_`  //_//_`  /|// //|,//_)/_`/_/
  /_;/_//_,._/._/  // //_,  / |/_//  //_)/_,/ \_


Let me think of a number between 1 - 50.
''')
guess1 = random.randint(1, 50)

level = input("Choose your difficulty level (Hard or Easy): ").lower()

def guess():
    attempts = 5 if level == "hard" else 10
    print(f"You have only {attempts} attempts to guess.")
    
    for i in range(1, attempts + 1):
        while True:
            guess = input("Make a guess: ")
            if guess.isdigit():
                guess = int(guess)
                if 1 <= guess <= 50:
                    break
                else:
                    print("Guess out of range. Please enter a number between 1 and 50.")
            else:
                print("Invalid input. Please enter a number.")
        
        diff = guess - guess1
        
        if guess == guess1:
            print("Correct. You won")
            break
        elif diff > 15:
            print("Too far")
        elif diff > 10:
            print("Far")
        elif diff > 5:
            print("Somewhat Near.")
        elif diff > 0:
            print("Almost there.")
        
        print(f"You are left with {attempts - i} guesses.")
    else:
        print("You are out of guesses. The correct number was:", guess1)

guess()
