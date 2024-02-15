# UNIVARIATE ANALYSIS
Univariate analysis involves examining one variable at a time to understand its characteristics and behavior. Here are some common types of analysis that can be performed using univariate analysis,

1.Descriptive Statistics.
2.Frequency Distribution.
3.Measures of Central Tendency.
4.Measure of Dispersion.
5.Quantiles and Percentiles.
6.Probability Distribution.
7.Skewness and Kurtosis.
8.Outlier Detection.
9.Missing Values Analysis.
10.Data Transformation.

































## Normal Distribution
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



#SUM 
sum is used to add the total numbers and provide as the details of total value
