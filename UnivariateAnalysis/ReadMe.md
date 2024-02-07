# NORMAL DISTRIBUTION
  Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric around its mean, with the majority of the observations clustered around the mean and fewer observations in the tails. It is characterized by its bell-shaped curve.




`Code`

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset - Replace 'your_dataset.csv' with the actual file path of your dataset
# Assuming your dataset has a column named 'Temperature'
your_dataset_path = 'your_dataset.csv'
df = pd.read_csv(your_dataset_path)

# Extract the 'Temperature' column
temperature_data = df['Temperature']

# Create a histogram and fit a kernel density estimate
sns.histplot(temperature_data, kde=True, color='skyblue', stat='density')

# Set labels and title
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.title('Normal Distribution of Temperature')

# Save the plot as a high-quality image (e.g., PNG)
plt.savefig('temperature_distribution.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

 
```
`Output`





<img src="/other/images/temperature_distribution.png" width = 400>
