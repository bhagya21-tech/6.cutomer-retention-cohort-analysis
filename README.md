# 📊 Customer Retention & Cohort Analysis 

Online Retail Dataset 

🔍 Project Overview 
-

This project analyzes customer purchasing behavior using cohort analysis to understand retention patterns over time.
The goal was to answer a real business question:

```python
Do customers come back after their first purchase, and howdoes retention differ across time and customer groups?

```
Using transactional retail data, i built a complete pipeline from raw data cleaning -> cohort modeling -> retention analysis
 -> business insights.

---
🗂 Datset
-


online Retail Dataset (Kaggle)
Contains real e-commerce transactions with:
* InvoiceNo 
* InvoiceDate
* CustomerID 
* Quantity
* UnitPrice
* Country

---
 ⚙ Tools & Skills Used 
 -
* Python 
* Pandas, Numpy
* Matplotlib, Seaborn 
* Data cleaning & validation
* Cohort analysis 
* Business insight generation

---
🧠 Key Concepts Implemented 
-
* Customer retention modeling 
* Cohort construction (first purchase month)
* Cohort index (month since first purchase)
* Retention matrix & heatmaps 
* Segmentation by country and customer value 

---

📈 Key Insights 
-
* Most cohorts drop to roughly 20-35% retention by the second month, showing very high early churn. 
* Retention stabilizes after 4-5 months, indicating a small loyal customer base.
* Older cohorts retain better than newer ones, suggesting a chance in customer quality or acquisition over time.
* No cohort demonstrates strong long-term retention beyond 3-4 months.
* High-value customers show better retention behavior than low-value customers.

---

💡 Business Impications 
-
* Focus retention strategies on the first 30 days (onboarding, remainders, offers).
* Investigate what changed after eary high-performing cohorts.
* Build loyalty programs for high-value customers.
* Track cohort retention monthly as a core business KPL.

---

⚠ Limitations 
-
* No marketing channel or user demographics available 
* Churn inferred from inactivity, not explicit labels
* Transactional business model only
* Historical dataset (no real-time validation)

---

```python
📁 Project Structure 

customer-retention-cohort-analysis/
|
├──data/
|  ├──online_retail.csv
|  └── cleaned_online_retail.csv
| 
├── notebooks/
|   ├── 01_data_cleaning.ipynb
|   ├── 02_cohort_analysis.ipynb
|   ├── 03_insights_visualization.ipynb
|
├── src/
|   └──cohort_utils.py
|   
├── visuals/ 
|   ├──overall_customer_retention_cohort.png
|   └──cohort_heatmap.png
|
└──README.md
```

🚀 Outcome 
-
Built a real-world customer retention analysis system that demonstrates:

* analytical thinking
* business-focused insights 
* clean data engineering
* and structured project design.
---
