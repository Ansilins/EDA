import matplotlib.pyplot as plt
import numpy as np

# Define a more complex maze data with start (S) and end (E) points
complex_maze_data = [
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W S     W    W     W             W W",
    "WWWWWWW W WWWWW WWWWW W WWWWWW WWW W",
    "W     W W       W     W     W   W  W",
    "W WWW W W WWWWWWW WWWWWWWWW WWW WWWW",
    "W   W W W     W           W   W    W",
    "WW WW W WWWWWWWWWWWWWWW W WWWWWWWWWW",
    "W   W   W       W       W       W  W",
    "W W WWWWW W WWWWW WWWWWWWWWWWWW W WW",
    "W W     W W     W       W     W W  W",
    "W WWWWWWW WWW W WWWWWW WWWWW W W WWW",
    "W       W   W W     W     W  W W   W",
    "WWWWW WW W W W WWWWW WWWWWWWWWWWWW W",
    "W         W W       W         W    W",
    "W WWWWWWWWWW WWWWWWWWWWWWWWW WWWWWW ",
    "W W       W       W         W      W",
    "W W WWWWWWWWWWWWWW WWWWWWWW W WWWWWW",
    "W W   W             W       W      W",
    "W WWW W W W W WWWWWWWWWWWWW WWWWWW W",
    "W     W W W       W     W       W  W",
    "W WWW W WWWWWWW W WW WW W WWWWW WWWW",
    "W W W W     W   W     W           W ",
    "W W W W WWWWWWWWWWWWWWWWWWW W WWWWWW",
    "W W   W W       W         W W W    W",
    "W WWWWW W WWWWWWWWWWWWWWWWW  W WWW W",
    "W       W         W     W          W",
    "W WWW WWWWWWWWWWW WWW WWW WW WWWWWWW",
    "W   W       W     W W W         W  W",
    "WWW WWW WWWWW WWWWW W W WWWWWWW W WW",
    "W     W     W       W   W          W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWE W",
]

# Ensure all rows have the same length by padding with spaces if necessary
max_length = max(len(row) for row in complex_maze_data)
complex_maze_data = [row.ljust(max_length) for row in complex_maze_data]

# Create a 2D list from the complex maze data
complex_maze_list = []
for row in complex_maze_data:
    row_list = []
    for char in row:
        if (char == 'W'):
            row_list.append(1)  # Wall
        elif (char == ' '):
            row_list.append(0)  # Path
        elif (char == 'S'):
            row_list.append(2)  # Start
        elif (char == 'E'):
            row_list.append(3)  # End
    complex_maze_list.append(row_list)

# Convert the 2D list to a numpy array
complex_maze_array = np.array(complex_maze_list)

# Create a plot
fig, ax = plt.subplots()

# Draw the maze
wall_thickness = 1  # Thickness of the walls

for i in range(complex_maze_array.shape[0]):
    for j in range(complex_maze_array.shape[1]):
        if (complex_maze_array[i, j] == 1):
            color = 'GREEN'
            # Draw thin green walls as rectangles with larger length and smaller width
            ax.add_patch(plt.Rectangle((j, i + (1 - wall_thickness) / 2), 1, wall_thickness, edgecolor=color, facecolor=color))  # Horizontal walls
            ax.add_patch(plt.Rectangle((j + (1 - wall_thickness) / 2, i), wall_thickness, 1, edgecolor=color, facecolor=color))  # Vertical walls

# Adjust the position of START and END labels further outside of the maze
start_pos = np.where(complex_maze_array == 2)
end_pos = np.where(complex_maze_array == 3)

if (start_pos[0].size > 0 and start_pos[1].size > 0):
    ax.text(start_pos[1][0] - 2, start_pos[0][0] - 2, 'START', ha='center', va='center', fontsize=12, fontweight='bold', color='black')

if (end_pos[0].size > 0 and end_pos[1].size > 0):
    ax.text(end_pos[1][0] + 2, end_pos[0][0] + 2, 'END', ha='center', va='center', fontsize=12, fontweight='bold', color='black')

# Set plot limits
ax.set_xlim(-1, complex_maze_array.shape[1] + 1)
ax.set_ylim(-1, complex_maze_array.shape[0] + 1)

# Turn off the axes
ax.set_xticks([])
ax.set_yticks([])

# Remove the plot outline (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Save the plot as an image file
plt.savefig("maze4_green.png", dpi=300, bbox_inches='tight')
plt.show()

