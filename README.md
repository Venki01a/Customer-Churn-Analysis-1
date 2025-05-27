# 📊 Customer Churn Prediction using XGBoost
---
Welcome to the Customer Churn Prediction project!  
This application predicts whether a customer will leave the bank or not based on key financial and personal features, using a powerful XGBoost machine learning model.

✅ Key Highlights:
- Built using XGBoost Classifier for high prediction accuracy.
- Streamlit app for interactive and user-friendly predictions.
- Integrated StandardScaler to maintain consistent feature scaling.
- Pickle files used for efficient model and scaler storage.
- Trained on real-world customer churn dataset (`Churn_Modelling.csv`).

---

# 🚀 Features

- 📈 Predicts customer churn based on financial parameters like Credit Score, Balance, and Salary.
- 🖥️ Simple and elegant Streamlit interface to input customer details and get real-time predictions.
- 💾 Model and scaler loaded dynamically using `pickle`.
- 📊 Clean preprocessing ensuring high model performance and reliability.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|:-----------|:--------|
| Python | Core programming language |
| XGBoost | Model training and prediction |
| Streamlit | Web app deployment |
| Pickle | Saving and loading models/scalers |
| Pandas & NumPy | Data handling and preprocessing |

---


---

### 📂 Project Structure

```
├── Customer churn1.ipynb         # Jupyter Notebook for training the XGBoost model
├── scaler.pkl                   # Saved StandardScaler object for input feature scaling
├── churn_model.pkl              # Trained XGBoost model file
├── Churn_Modelling.csv          # Dataset used for training and testing
├── churn.py                     # Streamlit application for prediction (main app)
├── README.md                    # Project documentation file
├── requirements.txt             # Python dependencies
```



---


# 📢 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

# 🎯 Future Improvements

- Add more advanced feature engineering (e.g., encode Geography and Gender smartly).
- Deploy the app using cloud services like AWS, GCP, or Streamlit Cloud.
- Improve UI/UX with better form design and loading animations.

---

# 🙌 Acknowledgements

Thanks to the creators of the [Churn Modelling Dataset](https://www.kaggle.com/) for providing valuable data for machine learning projects.

---
