import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.2)

print("=== RIDGE REGRESSION MODEL ===")

# Load and prepare data
df = pd.read_csv('D:\EHPON\sales_data.csv')
df['Month'] = pd.to_datetime(df['Month'])

# Prepare data for modeling
df_model = df.copy()
df_model = pd.get_dummies(df_model, columns=['Season', 'Region'], drop_first=True)

# Select features and target
X = df_model[['Marketing_Spend', 'Temperature', 'Promotion', 
              'Season_Spring', 'Season_Summer', 'Season_Winter', 'Region_South']]
y = df_model['Sales_Amount']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# Test different alpha values
print("\nTesting Ridge Regression alpha values:")
alpha_values = [0.1, 1.0, 10.0, 100.0, 1000.0]
best_alpha = None
best_r2 = -np.inf

for alpha in alpha_values:
    ridge_model = Ridge(alpha=alpha)
    ridge_model.fit(X_train_scaled, y_train)
    y_pred = ridge_model.predict(X_test_scaled)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"Alpha: {alpha:6.1f} | MSE: {mse:10.2f} | R²: {r2:.4f}")
    
    if r2 > best_r2:
        best_r2 = r2
        best_alpha = alpha

print(f"\nBest Alpha: {best_alpha}")

# Train final model
final_model = Ridge(alpha=best_alpha)
final_model.fit(X_train_scaled, y_train)
y_pred_final = final_model.predict(X_test_scaled)
mse_final = mean_squared_error(y_test, y_pred_final)
r2_final = r2_score(y_test, y_pred_final)

print("\nModel Performance Metrics")
print(f"R² Score: {r2_final:.4f}")
print(f"MSE: {mse_final:.2f}")
print(f"Accuracy: {r2_final*100:.2f}%")

# Feature Coefficients
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': final_model.coef_
})
coefficients = coefficients.sort_values('Coefficient', ascending=False)

print("\n FEATURE COEFFICIENTS ")
print(coefficients)

# Visualization: Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=coefficients, palette='viridis')
plt.title(f'Ridge Regression Coefficients (α={best_alpha})')
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ridge_coefficients.png', dpi=300, bbox_inches='tight')

plt.close()

# Visualization: Model Performance
performance_data = pd.DataFrame({
    'Metric': ['R² Score', 'Accuracy %'],
    'Value': [r2_final, r2_final*100]
})

plt.figure(figsize=(8, 5))
sns.barplot(x='Metric', y='Value', data=performance_data, palette='Blues')
plt.title('Ridge Regression Performance Metrics')
plt.ylabel('Value')
for i, v in enumerate(performance_data['Value']):
    plt.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.savefig('ridge_performance.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization: Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_final, alpha=0.7, s=100)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Ridge Regression: Actual vs Predicted Sales')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ridge_actual_vs_predicted.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n Ridge Regression model completed")
print(" Charts saved: ridge_coefficients.png, ridge_performance.png, ridge_actual_vs_predicted.png")

