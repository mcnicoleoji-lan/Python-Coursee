import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    # Update labels
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Run app
root.mainloop()