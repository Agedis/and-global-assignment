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
- Regularized models: **Ridge**, and **ElasticNet**  

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

python app.py (the server will start locally by default assuming all the necessary packages are installed)
```

# Example JSON request
{
  "age": 19,
  "sex": 1,
  "bmi": 140,
  "children": 0,
  "smoker": 0,
  "region_northwest": 0,
  "region_southeast": 0,
  "region_southwest": 1
}
# Example output
{
  "predicted_insurance_cost": 45231.78
}

## 📦 Packages Used  

The project makes use of the following Python packages:  

- [scikit-learn](https://scikit-learn.org/stable/) – Machine learning models (Linear Regression, Ridge, Lasso, ElasticNet)  
- [numpy](https://numpy.org/) – Numerical computations  
- [pandas](https://pandas.pydata.org/) – Data manipulation and preprocessing  
- [matplotlib](https://matplotlib.org/) – Data visualization  
- [seaborn](https://seaborn.pydata.org/) – Statistical data visualization  
- [flask](https://flask.palletsprojects.com/) – Web framework for deployment  
- [json](https://docs.python.org/3/library/json.html) – JSON parsing and formatting  
- [sys](https://docs.python.org/3/library/sys.html) – System-specific parameters and functions 
