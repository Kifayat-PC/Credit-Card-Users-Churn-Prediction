# -*- coding: utf-8 -*-
"""GL project K4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15JRT1w8GcqUuwI13JlZPcAcdjrrD28bw

# Credit Card Users Churn Prediction - Problem Statement

## Context

Thera Bank has recently observed a sharp decline in the number of credit card users. Credit cards are a significant source of revenue for the bank through various fees, such as annual charges, transaction fees, late payment penalties, and foreign exchange fees. The loss of customers using credit card services directly impacts the bank’s profitability. To mitigate this issue, Thera Bank seeks to understand the reasons behind customer attrition and identify patterns in customer behavior that lead to churn.

### Problem Statement
The objective of this analysis is to develop a classification model that can predict which customers are likely to discontinue their credit card services. By exploring customer data, identifying key influencing factors, and building predictive models, the bank can take proactive measures to retain customers. Additionally, actionable insights and recommendations will help improve customer satisfaction, optimize service offerings, and reduce churn, ultimately enhancing the bank’s overall financial performance.

### Data Dictionary

- CLIENTNUM: Client number. Unique identifier for the customer holding the account
- Attrition_Flag: Internal event (customer activity) variable - if the account is closed then "Attrited Customer" else "Existing Customer"
- Customer_Age: Age in Years
- Gender: The gender of the account holder
- Dependent_count: Number of dependents
- Education_Level: Educational Qualification of the account holder - Graduate, High School, Unknown, Uneducated, College(refers to a college student), Post-
Graduate, Doctorate.
- Marital_Status: Marital Status of the account holder
- Income_Category: Annual Income Category of the account holder
- Card_Category: Type of Card
- Months_on_book: Period of relationship with the bank
- Total_Relationship_Count: Total no. of products held by the customer
- Months_lnactive_12_mon: No. of months inactive in the last 12 months
- Contacts_Count_12_mon: No. of Contacts between the customer and bank in the last 12 months
- Credit_Limit: Credit Limit on the Credit Card
- Total_Revolving_Bal: The balance that carries over from one month to the next is the revolving balance
- Avg_Open_To_Buy: Open to Buy refers to the amount left on the credit card to use (Average of last 12 months)
- Total-Trans-Amt: Total Transaction Amount (Last 12 months)
- Total_Trans_Ct: Total Transaction Count (Last 12 months)
- Total-Ct-Chng-Q4_01: Ratio of the total transaction count in 4th quarter and the total transaction count in the 1st quarter
- Total_Amt_Chng_Q4_Q1: Ratio of the total transaction amount in 4th quarter and the total transaction amount in the 1st quarter
- Avg_Utilization_Ratio: Represents how much of the available credit the customer spent

##Objective
The primary objective of this analysis is to develop a machine learning-based classification model to predict customer churn in Thera Bank’s credit card services. By leveraging customer data, the goal is to identify key factors influencing attrition and uncover actionable insights that can help the bank retain customers. The model should effectively differentiate between customers who are likely to stay and those who may leave, enabling the bank to implement targeted retention strategies. Additionally, recommendations will be provided to enhance customer engagement, optimize service offerings, and improve overall customer satisfaction, ultimately reducing churn and safeguarding the bank’s revenue.

### Let us start by importing the required libraries
"""

# code to import necessary libraries for the project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For modeling and evaluation
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

# For preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# For oversampling and undersampling
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Suppress warnings and set plot style
import warnings
warnings.filterwarnings('ignore')
sns.set(style="whitegrid")

"""### Understanding the structure of the data"""

# from google.colab import drive
# drive.mount('/content/drive')
from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/BankChurners.csv'
df = pd.read_csv(file_path)

"""#Data Overview :
- to understand the dataset

### Displaying the first few rows of the dataset
"""

df.head()

"""### Checking the shape of the dataset"""

df.shape

"""### Checking the data types of the columns for the dataset"""

print(df.info())

"""### Statistical summary of the dataset"""

df.describe()

"""# Check for missing values and basic statistics:"""

# Check missing values count
missing_values = df.isnull().sum()
missing_values[missing_values > 0]

"""Therefore there are missing values
- 1,519 missing values in Education_Level

- 749 missing values in Marital_Status

## Fixing missing values

Since these are categorical variables, we will fill missing values with the most frequent category (mode). ​
"""

# Fill missing values with mode
df["Education_Level"].fillna(df["Education_Level"].mode()[0], inplace=True)
df["Marital_Status"].fillna(df["Marital_Status"].mode()[0], inplace=True)

# Verify missing values are handled
df.isnull().sum()

"""## Univariate and Bivariate analysis"""

# Set style
sns.set_style("whitegrid")

# Separate numerical and categorical columns
numerical_features = ['Customer_Age', 'Dependent_count', 'Months_on_book', 'Months_Inactive_12_mon',
                      'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Open_To_Buy',
                      'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Total_Amt_Chng_Q4_Q1',
                      'Avg_Utilization_Ratio']

categorical_features = ['Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category']

# Plot Univariate Analysis for numerical variables
plt.figure(figsize=(15, 15))
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(4, 4, i)
    sns.histplot(df[feature], kde=True, bins=20, color="blue")
    plt.title(f'Distribution of {feature}')
plt.tight_layout()
plt.show()

# Plot Univariate Analysis for categorical variables
plt.figure(figsize=(15, 10))
for i, feature in enumerate(categorical_features, 1):
    plt.subplot(2, 3, i)
    sns.countplot(x=df[feature], palette='coolwarm')
    plt.title(f'Count of {feature}')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""## Observations from Univariate Analysis:


- Customer_Age: The distribution shows that most customers are between the ages of 30 and 60, with a few outliers on both extremes.

- Dependent_count: This feature has most values between 0 and 5 dependents, with a few customers having larger numbers.

- Months_on_book: Customers are mostly long-term clients, with the majority of the values ranging from 20 to 60 months, though there are some short-term customers.

- Months_Inactive_12_mon: This variable shows a wide range of activity, from inactive customers (0 months) to those who have been inactive for several months.

- Contacts_Count_12_mon: Most customers seem to contact the bank between 0 and 5 times in the last year.

- Credit_Limit: The distribution of credit limits is skewed, with many customers having limits between $1,000 and $25,000.

- Total_Revolving_Bal: This feature has a skewed distribution with many customers having a balance close to zero, but a few customers carry higher revolving balances.

- Avg_Open_To_Buy: This variable shows a right-skewed distribution, with many customers using most of their available credit.

- Total_Trans_Amt: The total transaction amount shows a wide range, with the majority of customers having a relatively low transaction amount in the last 12 months.

- Total_Trans_Ct: Most customers have a smaller number of transactions (less than 100).

- Total_Ct_Chng_Q4_Q1: This feature has a varied distribution indicating fluctuating transaction activity across quarters.

- Avg_Utilization_Ratio: Most customers have a low utilization ratio, showing they don’t use the majority of their available credit.
"""

plt.figure(figsize=(12, 8))
corr_matrix = df[numerical_features].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# Bivariate Analysis: Numerical features vs. Attrition_Flag
plt.figure(figsize=(15, 15))
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(4, 4, i)
    sns.boxplot(x='Attrition_Flag', y=feature, data=df, palette='Set2')
    plt.title(f'{feature} vs Attrition_Flag')
plt.tight_layout()
plt.show()

# Bivariate Analysis: Categorical features vs. Attrition_Flag
plt.figure(figsize=(15, 10))
for i, feature in enumerate(categorical_features, 1):
    plt.subplot(2, 3, i)
    sns.countplot(x=feature, hue='Attrition_Flag', data=df, palette='coolwarm')
    plt.title(f'{feature} vs Attrition_Flag')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""##Bivariate Analysis: Correlation Insights
1. Gender vs Attrition Flag -

- The number of existing male and female customers is almost equal.
- However, attrition is slightly higher among female customers.

- Inference: Gender does not seem to be a strong indicator of churn, though females show a marginally higher attrition rate.

2. Education Level vs Attrition Flag -
- Most customers are graduates or have completed high school.

- The attrition rate appears higher among "Graduate" and "High School" groups.

- Inference: Higher education levels do not necessarily reduce customer churn.

3. Marital Status vs Attrition Flag -
- Married customers form the largest group, followed by single customers.

- The attrition rate is highest among married customers.

- Inference: Marital status alone is not a strong predictor of churn, but married customers may have different banking needs affecting their retention.

4. Income Category vs Attrition Flag -
- Customers earning between $60K - $80K are the largest group.

- Attrition is more evenly spread across income categories, but lower-income groups (<$40K) show slightly higher attrition.

- Inference: Income level has some effect on churn, with lower-income groups possibly being more prone to closing their accounts.

5. Card Category vs Attrition Flag -
- The majority of customers have Blue cards.

- Most of the attrition happens in the Blue category.

- Inference: Premium cardholders (Gold, Silver, Platinum) tend to have lower attrition, possibly due to better benefits.

6. Total Transaction Amount vs Attrition Flag -
- Attrited customers generally have lower total transaction amounts.

- Existing customers tend to have more frequent and higher transaction amounts.

- Inference: Customers who spend more and make frequent transactions are less likely to churn.

7. Total Transaction Count vs Attrition Flag -
- Attrited customers make fewer transactions.

- Existing customers show a higher median number of transactions.

- Inference: Transaction activity is a significant predictor of customer retention.

8. Total Transaction Change (Q4-Q1) vs Attrition Flag -
- A decline in transactions over quarters is observed among attrited customers.

- Inference: A drop in transaction count is a possible early indicator of customer churn.

9. Total Amount Change (Q4-Q1) vs Attrition Flag -
- Attrited customers show a reduction in spending compared to existing customers.

- Inference: Decreasing spending habits can signal potential churn.

10. Average Utilization Ratio vs Attrition Flag -
- Attrited customers have a lower utilization ratio.

- Inference: Customers who utilize a larger portion of their available credit are more engaged and less likely to churn.

11. Customer Age vs Attrition Flag -
- The age distribution of both existing and attrited customers is similar.

- Inference: Age does not seem to be a strong predictor of churn.

12. Dependent Count vs Attrition Flag -
- There is no significant difference in dependent count between the two groups.

- Inference: The number of dependents does not impact customer attrition.

13. Months on Book vs Attrition Flag -
- Attrited customers have slightly fewer months on book.

- Inference: Customers who have been with the bank for a longer period are more likely to stay.

14. Months Inactive vs Attrition Flag -
- Attrited customers have higher inactive months.

- Inference: More inactivity increases the likelihood of churn.

15. Contact Count in Last 12 Months vs Attrition Flag -
- Attrited customers tend to have a slightly higher number of contacts.

- Inference: Increased customer service interactions might indicate dissatisfaction before account closure.

16. Credit Limit vs Attrition Flag -
- Attrited customers have a slightly lower credit limit.

- Inference: Higher credit limits might be associated with more engaged customers.

17. Total Revolving Balance vs Attrition Flag -
- Existing customers have a higher total revolving balance.

- Inference: Customers who use their revolving balance more are likely to remain active.

18. Average Open to Buy vs Attrition Flag -
- Existing customers have a higher "Open to Buy" amount.

- Inference: Financial flexibility (high available credit) may contribute to retention.

## Key insights
- Transaction behavior (amount, count, and changes over time) is a strong predictor of churn.

- Longer inactivity periods correlate with higher attrition.

- Customers with lower utilization ratios and fewer transactions are more likely to churn.

- Premium cardholders exhibit lower attrition rates.

- Credit limits, revolving balances, and "open to buy" amounts influence retention.
"""

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["Total_Trans_Amt"], y=df["Total_Trans_Ct"], hue=df["Attrition_Flag"], alpha=0.7)
plt.title("Total Transaction Amount vs Total Transaction Count")
plt.xlabel("Total Transaction Amount")
plt.ylabel("Total Transaction Count")
plt.show()

pivot_table = df.pivot_table(index="Income_Category", columns="Attrition_Flag", values="Total_Trans_Amt", aggfunc="mean")
print(pivot_table)

"""###Observations
1. Scatter Plot: Total Transaction Amount vs Total Transaction Count
Positive correlation between transaction amount & count.

Existing Customers have higher transactions, while Attrited Customers show lower values.

Low transaction activity is a strong predictor of churn.

- Inference: Customers with higher transactions are less likely to churn. The bank should engage low-activity users to reduce attrition.

2. Pivot Table: Income Category vs Total Transaction Amount
Existing Customers spend more across all income categories.

Higher-income groups transact more & churn less, while lower-income customers show higher attrition.

Possible data error ("abc") needs cleaning.

-  Inference: Retention efforts should focus on low-income & low-transaction customers with targeted incentives.

### Pairplot (for churn vs. usage)
"""

import seaborn as sns

# Sample the data for performance
sample_df = df.sample(1000, random_state=42)

# Plot pairplot
sns.pairplot(sample_df, hue="Attrition_Flag", vars=['Total_Trans_Amt', 'Total_Trans_Ct', 'Avg_Utilization_Ratio', 'Credit_Limit'])
plt.suptitle("Pairplot of Key Usage Metrics vs Churn", y=1.02)
plt.show()

"""### Bubble Plot (Cluster Analysis)"""

import plotly.express as px

fig = px.scatter(
    df, x='Total_Trans_Amt', y='Total_Trans_Ct',
    color='Customer_Cluster',
    size='Avg_Utilization_Ratio',
    hover_data=['Attrition_Flag', 'Credit_Limit'],
    title='Customer Segmentation by Transaction Behavior (Clusters)'
)
fig.show()

"""### Summary Table of Numerical Feature Distributions
We’ll generate a table that includes mean, median, std, min, max, skewness for all numerical features.
"""

# Summary statistics with skew
summary_stats = df.describe().T
summary_stats["median"] = df.median()
summary_stats["skew"] = df.skew()
summary_stats = summary_stats[["mean", "median", "std", "min", "25%", "50%", "75%", "max", "skew"]]
summary_stats.round(2)

"""## Encoding Categorical Variables

Cap extreme outliers (winsorization)
"""

from sklearn.preprocessing import LabelEncoder

# Binary encoding for Attrition_Flag (Target Variable)
df["Attrition_Flag"] = df["Attrition_Flag"].map({"Existing Customer": 0, "Attrited Customer": 1})

# Binary encoding for Gender
df["Gender"] = df["Gender"].map({"M": 0, "F": 1})

# One-hot encoding for categorical variables
df = pd.get_dummies(df, columns=["Education_Level", "Marital_Status", "Income_Category", "Card_Category"], drop_first=True)

# Display first few rows after encoding
df.head()

"""#  Outlier Detection & Treatment
Using the Interquartile Range (IQR) method to detect and handle outliers for numerical variables.

"""

# Select numerical columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

# Remove the target variable from outlier treatment
num_cols = num_cols.drop("Attrition_Flag")

# Function to cap outliers
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])

# Apply to all numerical columns except target
for col in num_cols:
    cap_outliers(df, col)

# Check if outliers are handled
df.describe()

"""### Outlier Detection - Observations
- Most numerical features do not have extreme outliers.

- Credit-related variables (Credit_Limit and Avg_Open_To_Buy) show high values, likely due to premium customers.

- Capping at the 99th percentile ensures extreme values don’t impact model performance while retaining valuable information.clustering.

## Train-test splitting to prepare for model building. ​
"""

from sklearn.model_selection import train_test_split

# Separate features and target variable
X = df.drop(columns=["Attrition_Flag"])  # Features
y = df["Attrition_Flag"]  # Target variable

# Split into train (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Display shapes to confirm split
X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""The dataset has been successfully split into:

- Training set: 8,101 samples

- Test set: 2,026 samples

Next, we'll start model building with five different algorithms

###  Customer Segmentation via Clustering (K-Means)
We’ll create clusters of customers based on selected behavior-related features (like usage, income proxy, and transactions), then profile these clusters.
"""

from sklearn.cluster import KMeans

# Selecting features for clustering
cluster_features = ['Total_Trans_Amt', 'Total_Trans_Ct', 'Avg_Utilization_Ratio', 'Credit_Limit', 'Months_Inactive_12_mon']

# Standardize
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[cluster_features])

# Elbow Method to find optimal clusters
inertia = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(range(1, 10), inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('No. of Clusters')
plt.ylabel('Inertia')
plt.show()

# Choose k=4 based on elbow curve
kmeans = KMeans(n_clusters=4, random_state=42)
df['Customer_Cluster'] = kmeans.fit_predict(scaled_features)

# Analyze clusters
cluster_profile = df.groupby('Customer_Cluster')[cluster_features].mean()
print(cluster_profile)

"""# Model Building (Original Data)

-- We'll train five models using:

- Decision Tree Classifier

- Random Forest Classifier

- XGBoost Classifier

- AdaBoost Classifier

- Gradient Boosting Classifier

-- Metrics for Evaluation:
- Accuracy: Measures overall correctness.

- Precision & Recall: Important for handling class imbalance.

- F1-Score: Balances precision and recall.

- ROC-AUC Score: Evaluates overall model performance
"""

# Check columns with missing values
print(df.isnull().sum()[df.isnull().sum() > 0])

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# Dictionary to store model performances
model_performance = {}

# Function to train and evaluate a model
def train_evaluate_model(model, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Compute metrics
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Store performance
    model_performance[model_name] = {
        "Accuracy": accuracy,
        "ROC-AUC": roc_auc,
        "Precision": report["1"]["precision"],
        "Recall": report["1"]["recall"],
        "F1-Score": report["1"]["f1-score"],
    }

# Train models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

for name, model in models.items():
    train_evaluate_model(model, name)

# Convert results to DataFrame for better visualization
model_results_df = pd.DataFrame(model_performance).T
model_results_df

"""#### Observation :
- Best Overall Model: XGBoost

- Highest ROC-AUC: 0.992 (excellent discriminatory power)

- Highest F1-score: 0.898 (balance between precision and recall)

- Strong Recall: 0.868 (important for catching churners)

- Gradient Boosting also performs very well, slightly below XGBoost in F1-score and ROC-AUC.

- Decision Tree lags behind, which is expected for a simple model without ensemble learning.

- Random Forest shows very high precision (0.938), meaning it makes few false positives — great if the bank wants fewer false alarms.

- AdaBoost is solid but falls behind others in recall (0.720) — it might miss more churners.

### Inference
- XGBoost is currently the best model in terms of balanced performance and ROC-AUC, which is very important for churn prediction.

- Gradient Boosting is a close second and may benefit from tuning.

- Decision Tree and AdaBoost may not generalize as well without improvements.

## Using SMOTE to handle class imbalance
"""

from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Separate features and target
X = df.drop("Attrition_Flag", axis=1)
y = df["Attrition_Flag"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Apply SMOTE to oversample the minority class
smote = SMOTE(random_state=42)
X_train_oversampled, y_train_oversampled = smote.fit_resample(X_train, y_train)

# Check class distribution
print("Before Oversampling:\n", y_train.value_counts())
print("\nAfter Oversampling:\n", y_train_oversampled.value_counts())

"""## Training Models on Oversampled Data"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

models_os = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

# Store results
results_os = []

# Evaluation function
def train_evaluate_model_os(model, name):
    model.fit(X_train_oversampled, y_train_oversampled)
    y_pred = model.predict(X_test)
    results_os.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred)
    })

# Run for each model
for name, model in models_os.items():
    train_evaluate_model_os(model, name)

# Show results
import pandas as pd
results_df_os = pd.DataFrame(results_os)
results_df_os.sort_values(by="F1-Score", ascending=False)

"""## Key insights
- XGBoost outperforms all models in every metric and shows excellent balance between precision and recall, making it a top candidate for final model selection.

- Gradient Boosting and Random Forest also performed well and are strong candidates for further tuning.

- AdaBoost and Decision Tree lag slightly, especially in precision, suggesting more false positives.

##  Model Building – Undersampled Data
"""

from imblearn.under_sampling import RandomUnderSampler

# Apply undersampling to the training data
rus = RandomUnderSampler(random_state=42)
X_train_under, y_train_under = rus.fit_resample(X_train, y_train)

# Check new class distribution
print("Before Undersampling:\n", y_train.value_counts())
print("\nAfter Undersampling:\n", y_train_under.value_counts())

"""## Training the Same 5 Models on Undersampled Data"""

# Store results for undersampling
results_under = []

# Evaluation function
def train_evaluate_model_under(model, name):
    model.fit(X_train_under, y_train_under)
    y_pred = model.predict(X_test)
    results_under.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred)
    })

# Train and evaluate
for name, model in models_os.items():
    train_evaluate_model_under(model, name)

# Show results
results_df_under = pd.DataFrame(results_under)
results_df_under.sort_values(by="F1-Score", ascending=False)

"""## Key insights -

- XGBoost remains the strongest performer:
Best F1-score and ROC-AUC, and maintains high recall, which is crucial for catching churners.
Precision dropped slightly compared to oversampled results, which is normal in undersampling.

-  Gradient Boosting is a very close second.
Excellent recall and almost identical F1-score to XGBoost.

- Random Forest is still reliable.
Solid F1-score, but a slight drop compared to oversampled version.

-  AdaBoost and Decision Tree:
Lower precision and F1, indicating higher false positives — not ideal for production.

## Setup for Hyperparameter Tuning

- Use a stratified KFold for balanced validation.

- Tune with RandomizedSearchCV.

- Evaluate on the test set using the same metrics: Accuracy, ROC-AUC, Precision, Recall, F1-score.

### Random Forest - Tuning
"""

# Prepare features and target
X = df.drop("Attrition_Flag", axis=1)
y = df["Attrition_Flag"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42, test_size=0.2
)

# Stratified K-Fold cross-validator
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)  # Reduced to 3 for speed

# Reduced parameter grid for faster RandomizedSearchCV
rf_params = {
    "n_estimators": [100, 200],               # reduced from 3 values to 2
    "max_depth": [None, 10, 20],              # reduced to 3 values
    "min_samples_split": [2, 5],              # reduced
    "min_samples_leaf": [1, 2],               # reduced
    "bootstrap": [True]                       # single value for now
}

# Random Forest with RandomizedSearchCV
rf = RandomForestClassifier(random_state=42)
rf_search = RandomizedSearchCV(
    rf,
    rf_params,
    cv=cv,
    n_iter=10,                  # reduced to 10 to avoid long execution
    scoring='f1',
    random_state=42,
    n_jobs=-1,
    verbose=1
)

# Fit the search
rf_search.fit(X_train, y_train)

# Best model
best_rf = rf_search.best_estimator_

# Optional: Evaluate
y_pred = best_rf.predict(X_test)
print("F1 Score:", f1_score(y_test, y_pred))

"""### Random Forest - Tuning"""

from sklearn.ensemble import GradientBoostingClassifier

gb_params = {
    'n_estimators': [100, 150],       # Reduced values
    'learning_rate': [0.05, 0.1],     # Balanced learning rates
    'max_depth': [3, 4],              # Commonly effective depths
    'subsample': [0.8],               # Only one to reduce space
    'min_samples_split': [2, 5]
}

gb = GradientBoostingClassifier(random_state=42)

gb_search = RandomizedSearchCV(
    gb,
    gb_params,
    cv=2,                            #  reduced to 2 folds
    n_iter=5,                        # trying just 5 combinations
    scoring='f1',
    random_state=42,
    n_jobs=-1,
    verbose=1
)

gb_search.fit(X_train, y_train)
best_gb = gb_search.best_estimator_

"""### XGBoost - Tuning"""

xgb_model = xgb.XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42,
    n_jobs=-1
)

xgb_params = {
    'n_estimators': [100, 150],        # Lowered
    'learning_rate': [0.05, 0.1],      # Safer, faster
    'max_depth': [3, 5],               # Efficient range
    'subsample': [0.8],
    'colsample_bytree': [0.8]
}

xgb_search = RandomizedSearchCV(
    xgb_model,
    xgb_params,
    cv=2,
    n_iter=5,                         # Just 5 iterations
    scoring='f1',
    random_state=42,
    n_jobs=-1,
    verbose=1
)

xgb_search.fit(X_train, y_train)
best_xgb = xgb_search.best_estimator_

"""## Evaluating Tuned Models"""

def evaluate_model(model, name):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_proba)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"\n {name} Evaluation:")
    print(f"Accuracy: {acc:.4f}")
    print(f"ROC-AUC: {roc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1-Score: {f1:.4f}")
    return [name, acc, roc, prec, rec, f1]

results = []
results.append(evaluate_model(best_rf, "Random Forest (Tuned)"))
results.append(evaluate_model(best_gb, "Gradient Boosting (Tuned)"))
results.append(evaluate_model(best_xgb, "XGBoost (Tuned)"))

"""##Observations
--- XGBoost (Tuned) is your top performer across most metrics, especially in:

1. Accuracy

2. ROC-AUC

3. F1-Score (balanced harmonic mean)

4. Recall (important for retaining customers!)

--- Gradient Boosting (Tuned) is a very close second, with slightly better precision but lower recall.

--- Random Forest (Tuned) still performs well, but lags behind in recall and F1-Score.

##  Pipeline and ColumnTransformer

- Now that we have a final model, let's use pipelines to put the model into production. We know that we can use pipelines to standardize the model building, but the steps in a pipeline are applied to each and every variable.

- We personalize the pipeline to perform different preprocessing steps on different columns by using Column Transformer
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

# Split features and target
X = df.drop("Attrition_Flag", axis=1)
y = df["Attrition_Flag"]

# Numerical & categorical columns
num_cols = X.select_dtypes(include=['float64', 'int64']).columns.tolist()
cat_cols = X.select_dtypes(include=['object']).columns.tolist()

# Preprocessor
preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(drop="first", handle_unknown='ignore'), cat_cols)
])

# Pipeline with classifier
rf_pipeline = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Fit the model
rf_pipeline.fit(X_train, y_train)

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Re-split just in case
X = df.drop("Attrition_Flag", axis=1)
y = df["Attrition_Flag"]

# Identify numeric and categorical columns
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Define transformers
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_features)
    ]
)

# Define the full pipeline with XGBoost
xgb_pipeline = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("classifier", XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42))
])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# Fit the pipeline
xgb_pipeline.fit(X_train, y_train)

# Evaluate performance
y_pred = xgb_pipeline.predict(X_test)
y_proba = xgb_pipeline.predict_proba(X_test)[:, 1]

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("ROC-AUC Score:", roc_auc_score(y_test, y_proba))

ConfusionMatrixDisplay.from_estimator(xgb_pipeline, X_test, y_test, cmap="Blues")
plt.title("Confusion Matrix - XGBoost Pipeline")
plt.show()

"""- High Recall (86%) for churners: We are catching the majority of customers likely to leave, which is critical for retention strategies.

- Low False Positive Rate: Only 24 non-churners misclassified as churn — manageable for customer outreach.

- ROC-AUC near 1.0: Exceptional separation between churn and non-churn classes.

## Final Model Comparison Table
"""

# Final model results
import pandas as pd

results_df = pd.DataFrame(results, columns=["Model", "Accuracy", "ROC-AUC", "Precision", "Recall", "F1-Score"])
results_df = results_df.sort_values(by="F1-Score", ascending=False)
display(results_df)

"""## Final Model Selection
Based on F1-score and ROC-AUC, **XGBoost (Tuned)** outperforms all other models with strong recall, making it ideal for identifying churn-prone customers.

## Bar Plot of Model Comparison
"""

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.barplot(data=results_df, x="Model", y="F1-Score", palette="viridis")
plt.title("Model Comparison - F1 Score")
plt.ylabel("F1 Score")
plt.xticks(rotation=30)
plt.show()

"""## Visual Summaries"""

from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(best_xgb, X_test, y_test, cmap='Blues')
plt.title("Confusion Matrix - XGBoost")
plt.show()

from xgboost import plot_importance

plot_importance(best_xgb, max_num_features=10)
plt.title("Top 10 Features - XGBoost")
plt.show()

"""##  Actionable Insights

1. Customers with fewer transactions and lower spending are more likely to churn.
2. Low card utilization and long periods of inactivity signal dissatisfaction.
3. Premium card holders (Gold, Platinum) show higher retention rates.

##  Recommendations

1. Offer retention incentives (cashbacks, discounts) to low-spend users.
2. Launch automated follow-ups after 2 months of inactivity.
3. Promote premium cards to high-engagement customers for improved retention.

## Conclusion

- In this project, we developed a machine learning solution to identify customers likely to churn from Thera Bank's credit card services. Using EDA, feature engineering, and multiple classification models, we found that **XGBoost** offered the best performance, especially in terms of **recall and F1-score**.

- With actionable business insights and targeted retention strategies, Thera Bank can reduce churn, retain high-value customers, and improve long-term profitability.
"""