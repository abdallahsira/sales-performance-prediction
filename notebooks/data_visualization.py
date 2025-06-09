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

# Convert Month to datetime for time series analysis
df['Month'] = pd.to_datetime(df['Month'])
df['Month_Num'] = df['Month'].dt.month
df['Year'] = df['Month'].dt.year

print("Generating visualizations...")

# 1. Time Series Analysis of Sales Trends
plt.figure(figsize=(14, 7))
plt.plot(df['Month'], df['Sales_Amount'], marker='o', linestyle='-', linewidth=2, markersize=8)
plt.title('Monthly Sales Trend (2023)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r'D:\EHPON\sales_trend.png')
plt.close()
print("1. Sales trend visualization created")

# 2. Seasonal Analysis
plt.figure(figsize=(12, 6))
sns.boxplot(x='Season', y='Sales_Amount', data=df)
plt.title('Sales Distribution by Season', fontsize=16)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig(r'D:\EHPON\sales_by_season.png')

plt.close()
print("2. Seasonal analysis visualization created")

# 3. Impact of Promotions on Sales
plt.figure(figsize=(10, 6))
sns.boxplot(x='Promotion', y='Sales_Amount', data=df)
plt.title('Impact of Promotions on Sales', fontsize=16)
plt.xlabel('Promotion (0 = No, 1 = Yes)', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig(r'D:\EHPON\sales_by_promotion.png')

plt.close()
print("3. Promotion impact visualization created")

# 4. Regional Sales Comparison
plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Sales_Amount', data=df)
plt.title('Sales Comparison by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig(r'D:\EHPON\sales_by_region.png')

plt.close()
print("4. Regional comparison visualization created")

# 5. Relationship Between Marketing Spend and Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales_Amount', hue='Season', size='Promotion', 
                sizes=(100, 200), data=df)
plt.title('Relationship Between Marketing Spend and Sales', fontsize=16)
plt.xlabel('Marketing Spend ($)', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig(r'D:\EHPON\marketing_vs_sales.png')
plt.close()
print("5. Marketing vs sales visualization created")

# 6. Temperature Impact on Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Sales_Amount', hue='Season', size='Promotion', 
                sizes=(100, 200), data=df)
plt.title('Impact of Temperature on Sales', fontsize=16)
plt.xlabel('Temperature (°F)', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig(r'D:\EHPON\temperature_vs_sales.png')
plt.close()
print("6. Temperature impact visualization created")

print("All visualizations have been generated successfully!")

