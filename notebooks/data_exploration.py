import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.2)

# Load the dataset
df = pd.read_csv('D:\EHPON\sales_data.csv')

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check dataset information
print("\nDataset Information:")
df.info()

# Check basic statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())



# Convert Month to datetime for time series analysis
df['Month'] = pd.to_datetime(df['Month'])
df['Month_Num'] = df['Month'].dt.month
df['Year'] = df['Month'].dt.year

# Display updated dataframe
print("\nUpdated DataFrame with datetime features:")
print(df.head())

# Create a copy of the dataframe for analysis
df_analysis = df.copy()

# Check correlation between numerical variables
correlation_matrix = df_analysis[['Sales_Amount', 'Marketing_Spend', 'Temperature', 'Promotion', 'Month_Num']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Visualize correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Numerical Variables')
plt.savefig(r'D:\EHPON\correlation_matrix.png')

plt.close()

