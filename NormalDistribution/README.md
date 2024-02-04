# NORMAL DISTRIBUTION
  This folder contains normal distribution on different dataset and features in the datasets. 


`Code`

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset - Replace 'your_dataset.csv' with the actual file path of your dataset
# Assuming your dataset has a column named 'Rainfall'
your_dataset_path = 'your dataset path'
df = pd.read_csv(your_dataset_path)

# Extract the 'Rainfall' column
rainfall_data = df['Rainfall']

# Create a histogram and fit a kernel density estimate
sns.histplot(rainfall_data, kde=True, color='skyblue', stat='density')

# Set labels and title
plt.xlabel('Rainfall')
plt.ylabel('Density')
plt.title('Normal Distribution of Rainfall')

# Save the plot as a high-quality image (e.g., PNG) with higher DPI
plt.savefig('rainfall_distribution_high_quality.png', dpi=2000, bbox_inches='tight')

# Show the plot
plt.show()
 
```
`Output`
