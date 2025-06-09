# 📈 Sales Performance Prediction & Analysis

This project analyzes 24 months of sales data to uncover business insights and build predictive models. The Ridge Regression model achieved **95.97% accuracy** and identified **temperature, marketing spend**, and **seasonality** as key drivers of sales performance.

---

## 🔍 Project Goals

- Explore and visualize trends in sales data
- Build predictive models to forecast sales
- Interpret results and deliver actionable business insights

---

## 🧠 Techniques Used

- Data Cleaning & Feature Engineering
- Correlation Analysis & EDA
- Time-Series & Seasonal Analysis
- Ridge Regression with hyperparameter tuning
- Model evaluation (R², MSE, coefficient analysis)
- Matplotlib & Seaborn for visualizations

---

## 🗂️ Project Structure

```
├── data/                   # Dataset (CSV)
├── notebooks/              # Python scripts for analysis & modeling
├── outputs/                # Charts & graphs
├── final_report.md         # Full project report and insights
```

---

## 📊 Key Insights

- **Temperature**: ~$4,367 sales increase per °F
- **Marketing Spend**: ~$0.67 ROI per dollar
- **Summer Peak**: $31,000 median sales
- **South Region**: ~$1,363 underperformance
- **Best Model**: Ridge Regression (α = 0.1)

---


## 📷 Sample Visuals

![correlation_matrix](https://github.com/user-attachments/assets/38bd2f66-a89a-428b-9501-ff92c3fcdf66)
![sales_by_season](https://github.com/user-attachments/assets/260a628b-6101-47d9-9946-42c77c1400b1)
![marketing_vs_sales](https://github.com/user-attachments/assets/a709158a-e866-4d6c-b113-e2c7cfc9820a)
![ridge_coefficients](https://github.com/user-attachments/assets/bff534e9-89c6-4509-838e-3e4c6684dff3)


---

## ✅ Results Summary

| Model            | R² Score | MSE       | Rank |
|------------------|----------|-----------|------|
| Ridge Regression | **0.9597** | 1,175,106 | 1st  |
| Linear Regression| 0.9531   | 1,365,175 | 2nd  |
| Random Forest    | 0.9374   | 1,823,033 | 3rd  |

---

## 🙋‍♂️ Author

**Abdalla Sera**  
[LinkedIn](https://www.linkedin.com/in/yourprofile)  
📧 abdallahsira47@gmail.com  

---

## 🧾 License

This project is licensed under the MIT License.
