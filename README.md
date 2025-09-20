# Assignment Solutions
Repo for hosting solutions to and global take home assignment 

# Task 1

# Task 2

# Medical Insurance Cost Prediction  

This project trains and deploys a machine learning model that predicts an individual’s medical insurance charges based on demographic and lifestyle features.  

---

## 📊 Dataset  
The model was trained on the [Medical Insurance Cost Dataset](https://www.kaggle.com/datasets/mosapabdelghany/medical-insurance-cost-dataset) from Kaggle.  

**Features include:**  
- `age` (numeric)  
- `sex` (binary: 0 = female, 1 = male)  
- `bmi` (numeric)  
- `children` (numeric)  
- `smoker` (binary: 0 = non-smoker, 1 = smoker)  
- `region` (one-hot encoded: northwest, southeast, southwest, northeast [baseline])  

---

## 🤖 Model  
A **linear regression model** was chosen for its interpretability and suitability for continuous outcomes.  

We compared:  
- Ordinary Linear Regression  
- Regularized models: **Ridge**, **Lasso**, and **ElasticNet**  

**Evaluation Metrics:**  
- Root Mean Squared Error (RMSE)  
- R² Score (on training and test sets)  

📌 Regularization did not significantly improve performance, so **ordinary linear regression** was selected as the final model.  

---

## 🚀 Deployment  
The trained model is deployed using a simple **Flask** web server.  

- Accepts **JSON input** with feature values  
- Returns predicted insurance cost as **JSON output**  

---

## ⚙️ Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/your-username/insurance-cost-prediction.git
cd insurance-cost-prediction
pip install -r requirements.txt
