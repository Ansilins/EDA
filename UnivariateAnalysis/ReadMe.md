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



# SUM IN EDA
In Exploratory Data Analysis (EDA), the "sum" function is often used to calculate the total of a numerical variable across a dataset. This can be useful for understanding the overall magnitude or distribution of a variable, identifying potential outliers, or simply obtaining summary statistics.
Understanding Total Magnitude
Detecting Outliers
Comparing Groups or Categories

'sample code'
```python
import pandas as pd

# Load the Excel file into a pandas DataFrame
excel_file_path = 'your_excel_file.xlsx'  # Replace 'your_excel_file.xlsx' with the path to your Excel file
df = pd.read_excel(excel_file_path)

# Assuming 'column_name' is the name of the column you want to calculate the sum for
column_name = 'your_column_name'  # Replace 'your_column_name' with the actual name of the column

# Calculate the sum of the column
column_sum = df[column_name].sum()

print("Sum of '{}' column: {}".format(column_name, column_sum))

```
