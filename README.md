# **Insurance Premium Prediction Using Machine Learning**

## **Project Overview**
This project focuses on predicting **insurance premiums** using various machine learning models. It evaluates models such as **Linear Regression**, **Ridge Regression**, and **XGBoost**, ultimately selecting the most accurate model based on evaluation metrics. The project also highlights feature importance, residual analysis, and identifies extreme errors in predictions.

---

## **Table of Contents**
1. [Dataset Description](#dataset-description)
2. [Project Workflow](#project-workflow)
3. [Models Evaluated](#models-evaluated)
4. [Model Comparison](#model-comparison)
5. [Residual Analysis](#residual-analysis)
6. [Extreme Error Analysis](#extreme-error-analysis)
7. [Model Deployment Artifacts](#model-deployment-artifacts)
8. [Technologies Used](#technologies-used)
9. [Setup Instructions](#setup-instructions)
10. [Results and Conclusion](#results-and-conclusion)

---

## **Dataset Description**
The dataset contains features such as **age, BMI, risk score, region, gender, income levels**, and other relevant attributes related to individuals. The target variable is the **insurance premium**.

---

## **Project Workflow**
The project workflow consists of the following stages:

1. **Data Preprocessing**
   - Handling missing values (if any).
   - Scaling numeric features.
   - Encoding categorical features.

2. **Feature Selection**
   - Using **Variance Inflation Factor (VIF)** to remove multicollinearity among features.

3. **Model Training and Evaluation**
   - Linear Regression
   - Ridge Regression
   - XGBoost (with Hyperparameter Tuning)

4. **Residual Analysis**
   - Distribution of prediction errors to assess the model’s performance.

5. **Extreme Error Analysis**
   - Identifying predictions with significant deviations (greater than 10%).

6. **Model Deployment**
   - Saving the best-performing model and scaler for deployment.

---

## **Models Evaluated**
Three regression models were trained and evaluated:

1. **Linear Regression**
   - A baseline model for predicting insurance premiums.

2. **Ridge Regression**
   - Applied Ridge regularization to reduce overfitting.

3. **XGBoost**
   - A highly efficient and accurate gradient boosting model.

### **Model Performance Comparison**
| Metric                 | Linear Regression | Ridge Regression | XGBoost (Best) |
|------------------------|------------------|------------------|---------------|
| **Train Score (R²)**   | 0.9351           | 0.9351           | 0.9976        |
| **Test Score (R²)**    | 0.9342           | 0.9342           | 0.9939        |
| **MSE**                | 4619784.93       | 4619774.34       | 433690.43     |
| **RMSE**               | 2149.36          | 2149.37          | 658.55        |

**Conclusion**: The **XGBoost model** achieved the best performance with the lowest error and highest accuracy.

---

## **Feature Importance**
### **Linear Regression Feature Importance**
- Features like `insurance_plan`, `age`, and `normalized_risk_score` had the highest impact.

### **XGBoost Feature Importance**
- Top features:
  - `age`
  - `insurance_plan`
  - `normalized_risk_score`

![XGBoost Feature Importance](path/to/xgboost_feature_importance.png)

---

## **Residual Analysis**
To analyze prediction accuracy, the residuals (difference between actual and predicted values) were visualized:

- **Residual Distribution**: Shows most predictions are close to 0 error, with a slight right skew.
  
```python
sns.histplot(results_df['diff_pct'], kde=True)
plt.title('Distribution of Residuals')
```

![Residual Distribution](path/to/residual_distribution.png)

---

## **Extreme Error Analysis**
To identify extreme predictions where the percentage error exceeded 10%, the following logic was applied:

```python
extreme_error_threshold = 10
extreme_results_df = results_df[np.abs(results_df['diff_pct']) > extreme_error_threshold]
```

- **Extreme Errors**: ~2% of test predictions exceeded the 10% error threshold.

---

## **Model Deployment Artifacts**
The best-performing **XGBoost model** and **scaler** were serialized using `joblib` for easy reuse and deployment.

- **Model File**: `artifacts/model.joblib`
- **Scaler File**: `artifacts/scaler.joblib` (includes the scaler and columns to scale)

Code snippet for saving artifacts:

```python
from joblib import dump

dump(best_model, "artifacts/model.joblib")
scaler_with_cols = {
    'scaler': scaler,
    'cols_to_scale': cols_to_scale
}
dump(scaler_with_cols, "artifacts/scaler.joblib")
```

---

## **Technologies Used**
- **Programming Language**: Python  
- **Libraries**:
  - `Pandas`, `NumPy`: Data manipulation
  - `Scikit-learn`: Model training and evaluation
  - `XGBoost`: Advanced gradient boosting
  - `Matplotlib`, `Seaborn`: Data visualization
  - `joblib`: Model serialization  

---

## **Setup Instructions**
Follow these steps to set up and run the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/insurance-premium-prediction.git
   cd insurance-premium-prediction
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Project**
   - Load the dataset and run the Python scripts sequentially to train, evaluate, and analyze models.

5. **View Results**
   - Outputs, graphs, and residual analysis will be displayed.

---

## **Results and Conclusion**
- **Best Model**: XGBoost with hyperparameter tuning.
- The model achieved **high accuracy** with an **RMSE of 658.55**.
- **Feature Importance**: `age`, `insurance_plan`, and `normalized_risk_score` were identified as the most critical predictors.
- The residual analysis confirmed that the model performs well, with **98% predictions** within the 10% error threshold.

---

## **Future Scope**
- Experiment with additional feature engineering techniques.
- Explore ensemble methods like Stacking or Blending.
- Deploy the model as a REST API using Flask or FastAPI.

---

## **Acknowledgments**
Special thanks to open-source libraries like **Scikit-learn**, **XGBoost**, and visualization tools for enabling this project.

---


