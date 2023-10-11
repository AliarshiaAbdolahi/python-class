import random
from tkinter import *
from tkinter import messagebox

# List of colors
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']

def start_game():
    global score, time_left, current_color

    # Reset score and time left
    score = 0
    time_left = 30

    # Update score and time labels
    score_label.config(text="Score: " + str(score))
    time_label.config(text="Time left: " + str(time_left) + "s")

    # Start the countdown timer
    countdown()

    # Pick a random color from the list
    current_color = random.choice(colors)

    # Update the color label with the chosen color
    color_label.config(text=current_color, fg=current_color)

def check_guess(guess):
    global score, time_left, current_color

    # Check if the guessed color matches the current color
    if guess == current_color:
        score += 1
        score_label.config(text="Score: " + str(score))

    # Pick a new random color
    current_color = random.choice(colors)

    # Update the color label with the new color
    color_label.config(text=current_color, fg=current_color)

def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        time_label.config(text="Time left: " + str(time_left) + "s")
        root.after(1000, countdown)
    else:
        # Game over
        messagebox.showinfo("Game Over", "Time's up! Final score: " + str(score))

# Create the main window
root = Tk()
root.title("Color Guessing Game")

# Create the color label
color_label = Label(root, font=("Helvetica", 72))
color_label.pack(pady=20)

# Create the guess buttons
guess_frame = Frame(root)
guess_frame.pack(pady=10)

for color in colors:
    button = Button(guess_frame, text=color, padx=10, pady=5, command=lambda c=color: check_guess(c))
    button.pack(side=LEFT)

# Create the score and time labels
score_label = Label(root, text="Score: 0")
score_label.pack(pady=10)

time_label = Label(root, text="Time left: 30s")
time_label.pack(pady=10)

# Create the start button
start_button = Button(root, text="Start Game", command=start_game)
start_button.pack(pady=20)

# Run the main loop
root.mainloop()
