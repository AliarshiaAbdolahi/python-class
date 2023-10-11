import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("2048 Game")

# Define the colors for the tiles
colors = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

# Define the font for the tiles
font = ("Verdana", 40, "bold")

# Create the game grid
grid = [[0] * 4 for _ in range(4)]

# Function to add a new tile to the grid
def add_new_tile():
    # Find all empty cells
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    
    # Choose a random empty cell
    if empty_cells:
        row, col = random.choice(empty_cells)
        
        # Set the new tile value to either 2 or 4
        grid[row][col] = random.choice([2, 4])

# Function to update the game grid
def update_grid():
    for i in range(4):
        for j in range(4):
            # Get the tile value
            value = grid[i][j]
            
            # Set the tile color and text
            color = colors.get(value, "#ffffff")
            text = str(value) if value != 0 else ""
            
            # Create the tile label
            label = tk.Label(window, text=text, bg=color, fg="#000000", font=font, width=4, height=2)
            label.grid(row=i, column=j, padx=5, pady=5)

# Function to handle key presses
def key_press(event):
    # Get the key code
    key = event.keysym
    
    # Move the tiles based on the key pressed
    if key == "Up":
        move_up()
    elif key == "Down":
        move_down()
    elif key == "Left":
        move_left()
    elif key == "Right":
        move_right()
    
    # Add a new tile and update the grid
    add_new_tile()
    update_grid()

# Function to move the tiles up
def move_up():
    for j in range(4):
        for i in range(1, 4):
            # Move the tile up as far as possible
            while i > 0 and grid[i][j] != 0 and (grid[i-1][j] == 0 or grid[i-1][j] == grid[i][j]):
                if grid[i-1][j] == 0:
                    grid[i-1][j] = grid[i][j]
                    grid[i][j] = 0
                elif grid[i-1][j] == grid[i][j]:
                    grid[i-1][j] *= 2
                    grid[i][j] = 0
                i -= 1

# Function to move the tiles down
def move_down():
    for j in range(4):
        for i in range(2, -1, -1):
            # Move the tile down as far as possible
            while i < 3 and grid[i][j] != 0 and (grid[i+1][j] == 0 or grid[i+1][j] == grid[i][j]):
                if grid[i+1][j] == 0:
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 0
                elif grid[i+1][j] == grid[i][j]:
                    grid[i+1][j] *= 2
                    grid[i][j] = 0
                i += 1

# Function to move the tiles left
def move_left():
    for i in range(4):
        for j in range(1, 4):
            # Move the tile left as far as possible
            while j > 0 and grid[i][j] != 0 and (grid[i][j-1] == 0 or grid[i][j-1] == grid[i][j]):
                if grid[i][j-1] == 0:
                    grid[i][j-1] = grid[i][j]
                    grid[i][j] = 0
                elif grid[i][j-1] == grid[i][j]:
                    grid[i][j-1] *= 2
                    grid[i][j] = 0
                j -= 1

# Function to move the tiles right
def move_right():
    for i in range(4):
        for j in range(2, -1, -1):
            # Move the tile right as far as possible
            while j < 3 and grid[i][j] != 0 and (grid[i][j+1] == 0 or grid[i][j+1] == grid[i][j]):
                if grid[i][j+1] == 0:
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 0
                elif grid[i][j+1] == grid[i][j]:
                    grid[i][j+1] *= 2
                    grid[i][j] = 0
                j += 1

# Bind the key press event to the window
window.bind("<Key>", key_press)

# Add two initial tiles to the grid
add_new_tile()
add_new_tile()

# Update the grid
update_grid()

# Start the main loop
window.mainloop()