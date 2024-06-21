import matplotlib.pyplot as plt
import random

def plot_eye_test(words, num_rows, font_size=10, col_spacing=0.1, row_spacing=0.1):
    # Parameters for the visualization
    colour = "red"
    fig, ax = plt.subplots()  # This will create a figure with a size adjusted to fit the content

    # Calculate number of columns needed
    num_columns = len(words) // num_rows + (1 if len(words) % num_rows > 0 else 0)

    # Add the heading
    heading = "Circle lost"
    ax.text((num_columns - 1) * col_spacing / 2, 2.4, heading, fontsize=font_size + 10, color=colour, ha='center', va='bottom')

    # Plot each word in the grid
    for i, word in enumerate(words):
        row = i % num_rows + 2  # Adjust this value to place the grid below the heading
        col = i // num_rows
        x_position = col * col_spacing
        y_position = row * row_spacing  # Adjust to ensure words are placed below the heading
        ax.text(x_position, y_position, word, fontsize=font_size, color= colour, ha='left', va='center')

    # Set the limits and hide the axes
    ax.set_xlim(-col_spacing / 2, (num_columns - 0.5) * col_spacing)
    ax.set_ylim(0, (num_rows + 2) * row_spacing)  # Adjust to ensure heading is at the top
    ax.axis('off')  # Turn off the axes for a clean look

    # Save the plot
    plt.savefig('test_circle.png', bbox_inches='tight', format='png', dpi=300)

    # Show the plot
    plt.show()

# Manually defined list of random words with lengths between 6 and 8 characters
words = [
    "bake", "beam", "bold", "book", "busy", "cake", "calm", "bear", "jump", "ship",
    "cold", "come", "cook", "cool", "game", "deal", "deep", "dice", "dig", "dirt",
    "dope", "dust", "edge", "envy", "exit", "fade", "fair", "fake", "fall", "fame",
    "fast", "fear", "fine", "fish", "hope", "love", "luck", "note", "grow", "hand",
    "warm", "wave", "wear", "wind", "wish", "wood", "bark", "barn", "bash", "bent",
    "even", "fear", "feel", "fire", "flag", "flee", "flip", "flow", "fuel", "fuse",
    "gain", "gaze", "gear", "gift", "give", "glow", "grab", "grid", "grow", "harm",
    "hate", "have", "heal", "hear", "heat", "help", "herb", "hide", "hint", "hire"
]


# Include "blue" 20 times
words.extend(["lost"] * 10)

random.shuffle(words)

# Call the function with desired parameters
plot_eye_test(words, num_rows=10, font_size=33, col_spacing=0.2, row_spacing=0.2)

