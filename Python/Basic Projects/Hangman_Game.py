print(f"\nWelcome to hangman game!!!!")
#guess word
import string
import random
length_actual_word = random.randrange(4, 5)
string1 = string.ascii_lowercase
actual_word = "".join(random.choice(string1) for items in range(length_actual_word))
print(actual_word)
#generate blanks
sample = []
for word in actual_word:
    sample += "_"
print(sample)
#Guessing and loops
life = (len(actual_word) + 1)
game_over = False
while not game_over:
    guessed_word = input("Enter a letter: ").lower()
    for i in range(len(actual_word)): #0,1,2,3....
        if actual_word[i] == guessed_word: 
            sample[i] = guessed_word
    print(sample)
    if guessed_word not in actual_word:
        life -= 1
        print(f"Wrong guess. You are left with {life} lives")
        if life == 0:
            game_over = True
            print("You loose")
    if '_' not in sample:
        game_over = True
        print("You guessed right. You won")