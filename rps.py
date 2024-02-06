import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    """
    Selects a random choice from 'rock', 'paper', 'scissors' for the computer.
    Returns:
        str: The computer's choice.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of a round of rock, paper, scissors.
    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
    Returns:
        str: 'User wins' if the user wins, 'Computer wins' if the computer wins, 'Tie' if it's a tie.
    """
    if user_choice == computer_choice:
        return 'Tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'User wins'
    else:
        return 'Computer wins'


def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

choices = ['rock', 'paper', 'scissors']
for choice in choices:
    button = tk.Button(root, text=choice.capitalize(), command=lambda choice=choice: play_game(choice))
    button.pack(side=tk.LEFT)

root.mainloop()