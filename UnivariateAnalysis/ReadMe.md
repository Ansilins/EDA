# UNIVARIATE ANALYSIS
Univariate analysis involves examining one variable at a time to understand its characteristics and behavior. Here are some common types of analysis that can be performed using univariate analysis,

1.Descriptive Statistics.
2.Sum
3.Measures of Central Tendency
4.Measure of Dispersion.
5.Quantiles and Percentiles.
6.Probability Distribution.
7.Skewness and Kurtosis.
8.Outlier Detection.
9.Missing Values Analysis.
10.Data Transformation.
11.Frequency Distribution.




# Normal Distribution
  Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric around its mean, with the majority of the observations clustered around the mean and fewer observations in the tails. It is characterized by its bell-shaped curve.




`Code`

```python
# Load your dataset - Replace 'your_dataset.csv' with the actual file path of your dataset
# Assuming your dataset has a column named 'Temperature'
your_dataset_path <- 'your_dataset.csv'
df <- read.csv(your_dataset_path)

# Extract the 'Temperature' column
temperature_data <- df$Temperature

# Create a histogram with kernel density estimate using ggplot2
library(ggplot2)
ggplot(data = df, aes(x = temperature_data)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = 'skyblue', color = 'black') +
  geom_density(alpha = 0.5, fill = 'orange') +
  labs(title = 'Normal Distribution of Temperature', x = 'Temperature', y = 'Density') +
  theme_minimal()

# Save the plot as a high-quality image (e.g., PNG)
ggsave('temperature_distribution.png', dpi = 300, width = 6, height = 4, units = 'in')

# Show the plot


 
```
`Output`





<img src="/other/images/temperature_distribution.png" width = 400>



# SUM IN EDA
In Exploratory Data Analysis (EDA), the "sum" function is often used to calculate the total of a numerical variable across a dataset. This can be useful for understanding the overall magnitude or distribution of a variable, identifying potential outliers, or simply obtaining summary statistics.
Understanding Total Magnitude
Detecting Outliers
Comparing Groups or Categories

`sample code`
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
`Output`

<<img src="/other/images/sum.png" width = 400>


# MEASURE OF CENTRAL TENDENCY

Measures of central tendency are statistical measures used to summarize or describe the central or typical value of a dataset. They provide insight into the center or midpoint of a distribution of values. The three most common measures of central tendency are the mean, median, and mode:

Mean: Also known as the average, the mean is calculated by summing up all the values in a dataset and dividing by the total number of values. It represents the arithmetic average of the dataset and is sensitive to outliers.

Median: The median is the middle value of a dataset when it is sorted in ascending order. If the dataset has an odd number of values, the median is the middle value. If the dataset has an even number of values, the median is the average of the two middle values. The median is robust to outliers and extreme values.

Mode: The mode is the value that appears most frequently in a dataset. A dataset can have one mode (unimodal), two modes (bimodal), or more than two modes (multimodal). Unlike the mean and median, the mode can be applied to both numerical and categorical data.

# Measures of Dispersion

In statistics, measures of dispersion are used to quantify the spread or variability of a dataset. Here are some common measures of dispersion:

1. **Range**: The range is the simplest measure of dispersion and is calculated as the difference between the largest and smallest values in the dataset. It gives an idea of how spread out the data is.

import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Range
range_val = np.max(data) - np.min(data)

# Visualize Range
plt.figure()
plt.boxplot(data)
plt.title('Range: {}'.format(range_val))
plt.show()


2. **Variance**: The variance measures the average squared deviation of each data point from the mean of the dataset. It provides a measure of the dispersion of the data around the mean.

import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)



# Variance
variance_val = np.var(data)

# Visualize Variance
plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.title('Variance: {}'.format(variance_val))
plt.show()


3. **Standard Deviation**: The standard deviation is the square root of the variance and is perhaps the most widely used measure of dispersion. It indicates the average deviation of data points from the mean.

import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Standard Deviation
std_dev_val = np.std(data)

# Visualize Standard Deviation
plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.title('Standard Deviation: {}'.format(std_dev_val))
plt.show()


4. **Mean Absolute Deviation (MAD)**: MAD measures the average absolute difference between each data point and the mean of the dataset. Unlike the variance, it is not influenced by extreme values.
`Code`
```python
import numpy as np
import matplotlib.pyplot as plt

```
# Generate sample dataset
`Code`

np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Mean Absolute Deviation (MAD)
`Code`

mad_val = np.mean(np.abs(data - np.mean(data)))

# Visualize MAD
`Code`

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.title('Mean Absolute Deviation (MAD): {}'.format(mad_val))
plt.show()


5. **Percentiles and Quartiles**: Percentiles divide a dataset into hundredths, while quartiles divide it into quarters. They give insight into the distribution of the data and can help identify outliers.
`Code`

import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
`Code`

np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Percentiles and Quartiles
`Code`

percentiles = np.percentile(data, [25, 50, 75])
q1, median, q3 = percentiles

# Visualize Percentiles and Quartiles
`Code`

plt.figure()
plt.boxplot(data)
plt.title('Quartiles: Q1={}, Median={}, Q3={}'.format(q1, median, q3))
plt.show()


6. **Interquartile Range (IQR)**: IQR is the range between the first and third quartiles of the dataset. It is robust to outliers and gives a measure of the spread of the central 50% of the data.
`Code`

import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
`Code`

np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Interquartile Range (IQR)
`Code`

percentiles = np.percentile(data, [25, 75])
iqr_val = percentiles[1] - percentiles[0]

# Visualize IQR
`Code`

plt.figure()
plt.boxplot(data)
plt.title('Interquartile Range (IQR): {}'.format(iqr_val))
plt.show()


7. **Coefficient of Variation (CV)**: CV is the ratio of the standard deviation to the mean, expressed as a percentage. It is useful for comparing the variability of datasets with different means.

Each measure has its own strengths and weaknesses, and the choice of which one to use depends on the specific characteristics of the data and the objectives of the analysis.
`Code`

import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
`Code`

np.random.seed(0)  # for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Coefficient of Variation (CV)
`Code`

cv_val = np.std(data) / np.mean(data) * 100
`output`
Coefficient of Variation: 47.140452079103174


# Visualize CV
`Code`

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.title('Coefficient of Variation (CV): {:.2f}%'.format(cv_val))
plt.show()
