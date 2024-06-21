import matplotlib.pyplot as plt
import numpy as np

# Define a more complex maze data with start (S) and end (E) points
complex_maze_data = [
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W S       W             W             W",
    "W WWWWW W W WWWWW WWWWW W WWWWW WWWWW W",
    "W     W W W W   W     W W W   W W     W",
    "WWWWW W WWW W WWWWWWW W WWW W W W WWWWW",
    "W     W     W       W W     W W W     W",
    "W WWWWWWWWWWW WWWWW W WWWWWWWWWWW WWWWW",
    "W W       W       W W             W   W",
    "W W WWWWW W WWWWWWWWWWWWWWWWWWWWW W W W",
    "W W     W   W                   W W W W",
    "W WWWWWWW W W WWWWWWWWWWWWWWWWW W W W W",
    "W W       W W                 W W W W W",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWW W W W W W",
    "W W W                         W W W W W",
    "W W WWWWWWWWWWWWWWWWWWWWWWWWWWW W W W W",
    "W W                           W W W W W",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W W",
    "W                             W W W W W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W W",
    "W                               W W W W",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",
    "W                               W W W W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",
    "W                                 W W W",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W",
    "W                                 W W W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWW W W",
    "W                                   W W",
    "W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W",
    "W                                     W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
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
            # Draw thin green walls as rectangles with larger length and smaller width
            ax.add_patch(plt.Rectangle((j, i + (1 - wall_thickness) / 2), 1, wall_thickness, edgecolor='green', facecolor='green'))  # Horizontal walls
            ax.add_patch(plt.Rectangle((j + (1 - wall_thickness) / 2, i), wall_thickness, 1, edgecolor='green', facecolor='green'))  # Vertical walls

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
plt.savefig("maze2_green.png", dpi=300, bbox_inches='tight')
plt.show()
