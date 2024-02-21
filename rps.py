import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
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
    user_choice_label.config(text=f"User chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

choices = ['rock', 'paper', 'scissors']
for i, choice in enumerate(choices):
    button = tk.Button(root, text=choice.capitalize(), command=lambda choice=choice: play_game(choice))
    button.grid(row=0, column=i, padx=10, pady=10)

user_choice_label = tk.Label(root, text="User chose: ")
user_choice_label.grid(row=1, column=0, columnspan=3)

computer_choice_label = tk.Label(root, text="Computer chose: ")
computer_choice_label.grid(row=2, column=0, columnspan=3)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()