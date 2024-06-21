import matplotlib.pyplot as plt

# New Sudoku puzzle solution
new_sudoku_solution = [
    [4, 8, 3, 9, 2, 1, 6, 5, 7],
    [9, 6, 7, 3, 4, 5, 8, 2, 1],
    [2, 5, 1, 8, 7, 6, 4, 9, 3],
    [5, 4, 8, 1, 3, 2, 9, 7, 6],
    [7, 2, 9, 5, 6, 4, 1, 3, 8],
    [1, 3, 6, 7, 9, 8, 2, 4, 5],
    [3, 7, 2, 6, 8, 9, 5, 1, 4],
    [8, 1, 4, 2, 5, 3, 7, 6, 9],
    [6, 9, 5, 4, 1, 7, 3, 8, 2],
]

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)

color = 'green'

# Draw grid lines
for i in range(10):
    lw = 2 if i % 3 == 0 else 1
    ax.axhline(i, color=color, lw=lw)
    ax.axvline(i, color=color, lw=lw)

# Fill in the Sudoku numbers
for row in range(9):
    for col in range(9):
        num = new_sudoku_solution[row][col]
        if num != 0:
            ax.text(col + 0.5, 8.5 - row, str(num), ha='center', va='center', fontsize=33, color=color)

# Add title
plt.text(4.5, 10, 'Sudoku Solution', ha='center', va='center', fontsize=18, color=color, weight='bold')

# Hide axis
ax.axis('off')
plt.subplots_adjust(top=0.85)
plt.savefig("new_sudoku_solution.png", dpi=300, bbox_inches='tight')
# Adjust the subplot to prevent the title from overlapping
plt.show()
