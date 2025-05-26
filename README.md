# 💳 Credit Card Users Churn Prediction

## 🧠 Project Overview

This project focuses on predicting customer churn for Thera Bank’s credit card services. Credit cards are a significant revenue stream for banks through fees such as annual charges, balance transfers, and late payments. A recent drop in credit card usage has raised concerns at Thera Bank, prompting a need to identify why customers are leaving and how to proactively retain them.

The goal of this project is to analyze historical customer data and build a predictive model that can accurately classify whether a customer is likely to churn (i.e., close their credit card account). In addition to modeling, the project aims to surface insights into key factors influencing churn behavior and offer data-driven recommendations to improve customer satisfaction and retention.

> ⚠️ **Note:** The dataset is **confidential** and cannot be shared publicly due to privacy agreements.

---

## 🎯 Project Objectives

- Identify patterns in customer behavior associated with churn  
- Build accurate classification models to predict churners  
- Understand key features influencing a customer’s decision to leave  
- Recommend data-driven strategies to reduce churn

---

## 🔧 End-to-End Workflow

As part of this comprehensive data science solution, I executed the following key steps:

- 📊 **Exploratory Data Analysis (EDA):**  
  Conducted in-depth analysis to reveal behavioral and demographic patterns associated with churn.

- 🧹 **Data Preprocessing & Feature Engineering:**  
  Cleaned, transformed, and engineered features to ensure data quality and enhance model performance.

- 🤖 **Model Implementation & Comparison:**  
  Built and evaluated multiple classification models including **Random Forest** and **XGBoost** to predict customer churn.

- 🎯 **Hyperparameter Tuning:**  
  Optimized model performance using **GridSearchCV**, ensuring robustness and generalizability.

- 📈 **Model Interpretation:**  
  Identified top churn indicators by analyzing feature importance and model outputs.

- 💡 **Business Recommendations:**  
  Provided actionable strategies to improve customer retention based on data-driven insights.

> ⚠️ **Note:** The dataset used in this project is **confidential** and cannot be shared publicly due to data protection agreements.


## 🛠️ Tools & Techniques

- **Programming:** Python  
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Plotly, Scikit-learn, XGBoost  
- **Techniques:**  
  - Data Preprocessing & Feature Engineering  
  - Exploratory Data Analysis (EDA)  
  - Model Building (Logistic Regression, Random Forest, XGBoost)  
  - Hyperparameter Tuning (GridSearchCV)  
  - Evaluation Metrics (ROC-AUC, F1-Score, Confusion Matrix)

---

## 📂 Dataset Overview

While the dataset is private, it includes anonymized features such as:

- **Customer Demographics:** Age, Gender, Education Level, Marital Status, Income  
- **Account Metrics:** Credit Limit, Card Category, Tenure  
- **Behavioral Attributes:** Transaction Amount & Count, Credit Utilization, Contact Frequency  
- **Target Variable:** `Attrition_Flag` — indicates whether a customer churned

---

## 🔍 Methodology

### 1️⃣ Data Preprocessing
- Handled missing values and outliers  
- Encoded categorical variables  
- Scaled numerical features

### 2️⃣ Exploratory Data Analysis
- Analyzed churn distribution across demographics and behaviors  
- Visualized key relationships between features and churn

### 3️⃣ Model Building & Evaluation
- Baseline: Logistic Regression  
- Advanced: Random Forest, XGBoost  
- Metrics: Accuracy, F1-Score, ROC-AUC, Confusion Matrix

### 4️⃣ Hyperparameter Tuning
- Used GridSearchCV to optimize performance of Random Forest & XGBoost

### 5️⃣ Final Model
- **XGBoost** selected for its high ROC-AUC and generalization on test data

---

## 📈 Results & Insights

- 📉 Customers with **low contact frequency** were significantly more likely to churn  
- 💳 Users with **high credit utilization** (close to maxing out their credit limit) had higher churn probability  
- ⏳ Customers with **short tenure** (newer users) had higher churn risk  
- 👥 Married and middle-aged customers had lower churn rates

---

## 📚 What I Learned

- Applied **classification modeling** to a real-world customer retention problem  
- Improved skills in **feature engineering**, particularly with financial behavioral data  
- Understood the importance of **imbalanced class handling** and using the right metrics like ROC-AUC  
- Gained practical experience in tuning models using **GridSearchCV**  
- Strengthened storytelling through **visual analysis and stakeholder-ready dashboards**

---

## 🚀 How This Project Helped Me Grow

- Reinforced the importance of **domain knowledge in financial services**  
- Gained confidence in handling **classification problems** from end to end  
- Improved my ability to convert **raw data into business impact**  
- Developed a structured approach to **model selection and evaluation**  
- Sharpened my skill in crafting **narrative insights for decision-makers**

---

## ✅ Business Value

This solution can help **Thera Bank**:

- 🔎 **Identify at-risk customers early** and target them with proactive engagement  
- 💡 Design **personalized offers and loyalty programs** for high-risk segments  
- 🧮 Use predictive analytics to **optimize marketing and support budgets**  
- 📊 Build dashboards that **visualize churn risk in real-time**  
- 🤖 Scale customer retention strategies using **AI-driven models** instead of manual judgment

---

## Acknowledgments

This project was completed as part of the Unsupervised Learning course offered by Great Learning in collaboration with The University of Texas at Austin.

I would like to sincerely thank:

- **Great Learning** for providing the course content, guidance, and mentorship.
- **The University of Texas at Austin** for designing the curriculum and making real-world datasets and case studies available.
- The instructors and mentors whose insights helped shape my understanding of unsupervised learning techniques in financial data science.

> 📌 The dataset used in this project was provided exclusively as part of the course and is not publicly available.

---

✍️ **Author:**  
**Kifayat Sayed**  
*M.Sc. AI & ML | Data Science Enthusiast*  
📧 kifayatsayed301@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/kifayat-sayed-9614a9244?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) | [Portfolio](https://yourportfolio.com)
