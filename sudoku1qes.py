import matplotlib.pyplot as plt
import numpy as np

# Sample Sudoku puzzle from the provided PDF for Sudoku 1
sudoku_puzzle = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0],
]



fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)

color = 'red'

# Draw grid lines
for i in range(10):
    lw = 2 if i % 3 == 0 else 1
    ax.axhline(i, color=color, lw=lw)
    ax.axvline(i, color=color, lw=lw)

# Fill in the Sudoku numbers
for row in range(9):
    for col in range(9):
        num = sudoku_puzzle[row][col]
        if num != 0:
            ax.text(col + 0.5, 8.5 - row, str(num), ha='center', va='center', fontsize=16, color=color)

# Add title
plt.text(4.5, 10, 'Sudoku puzzle', ha='center', va='center', fontsize=18, color=color, weight='bold')

# Hide axis
ax.axis('off')
plt.subplots_adjust(top=0.85)
plt.savefig("sudoku_red_question.png", dpi=300, bbox_inches='tight')
# Adjust the subplot to prevent the title from overlapping
plt.show()
