import random
import tkinter as tk
from tkinter import messagebox

def play_round(user_choice):
    """
    Play a single round of the game.

    Args:
        user_choice (str): The user's choice (Rock, Paper, Scissors).
    """
    global num_rounds, user_score, computer_score

    game_emojis = ["👊", "✌️", "✋"]
    choices = {"Rock": 0, "Scissors": 1, "Paper": 2}
    user_choice_index = choices[user_choice]
    computer_choice_index = random.randrange(0, 3)

    # Check the winner
    if user_choice_index == computer_choice_index:
        result = "It's a tie"
    elif (user_choice_index == 0 and computer_choice_index == 1) or \
         (user_choice_index == 1 and computer_choice_index == 2) or \
         (user_choice_index == 2 and computer_choice_index == 0):
        result = "You won."
        user_score += 1
    else:
        result = "You lost"
        computer_score += 1

    # Update labels with choices and result
    user_label.config(text=f"Your choice: {game_emojis[user_choice_index]}")
    computer_label.config(text=f"Computer's choice: {game_emojis[computer_choice_index]}")
    result_label.config(text=result)

    # Update scores
    num_rounds += 1
    player_score_label.config(text=f"Player Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    # Ask if the user wants to play another round
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        pass
    else:
        end_game()

def end_game():
    """
    End the game and display the final scores.
    """
    messagebox.showinfo("Game Over", f"Game Over!\n\nPlayer Score: {user_score}\nComputer Score: {computer_score}")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Initialize variables
num_rounds = 0
user_score = 0
computer_score = 0

# Buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_round("Rock"))
rock_button.grid(row=0, column=0, padx=(0, 10))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_round("Scissors"))
scissors_button.grid(row=0, column=2, padx=(10, 0))
paper_button = tk.Button(root, text="Paper", command=lambda: play_round("Paper"))
paper_button.grid(row=0, column=1)

# Labels to display choices and result
user_label = tk.Label(root, text="")
user_label.grid(row=1, column=0, columnspan=3)
computer_label = tk.Label(root, text="")
computer_label.grid(row=2, column=0, columnspan=3)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3)

# Labels to display scores
player_score_label = tk.Label(root, text=f"Player Score: {user_score}")
player_score_label.grid(row=4, column=0, columnspan=3)
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}")
computer_score_label.grid(row=5, column=0, columnspan=3)

# Run the application
root.mainloop()
