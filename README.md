#  Car Price Prediction — AI SaaS Dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1fc8d2e8-c31c-45b7-ba5d-43d87cc5489f" />


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fdc9d193-95bd-43ef-8e54-3ade9e50a49a" />
Here’s a **professional GitHub README.md** for your 🚗 Car Price Prediction SaaS Project (Streamlit + ML + Glassmorphism UI).
You can directly paste this into your repo 👇

---


![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

##  Project Overview

This project is an **AI-powered SaaS dashboard** that predicts the **selling price of used cars** using machine learning.
It features a **modern glassmorphism UI**, interactive inputs, and real-time predictions using a trained **Random Forest model**.

---

##  Live Features

 Modern Glassmorphism UI
 Real-time Car Price Prediction
 Feature Importance Visualization
 Price Range Forecast Chart
 Interactive Streamlit Dashboard
 SaaS-style clean design

---

##  Project Structure

```
CAR_PRICE_PROJECT/
│
├── data/
│   └── car_prediction_data.csv
│
├── model/
│   ├── car_price_model.pkl
│   ├── fuel_encoder.pkl
│   ├── seller_encoder.pkl
│   └── transmission_encoder.pkl
│
├── templates/
│   └── index.html
│
├── aa.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## Dataset Features

| Feature       | Description                                    |
| ------------- | ---------------------------------------------- |
| Car_Name      | Name of the car (removed during preprocessing) |
| Year          | Year of purchase                               |
| Present_Price | Current showroom price                         |
| Kms_Driven    | Distance driven                                |
| Fuel_Type     | Petrol / Diesel / CNG                          |
| Seller_Type   | Dealer / Individual                            |
| Transmission  | Manual / Automatic                             |
| Owner         | Number of previous owners                      |
| Selling_Price | Target variable                                |

---

##  Machine Learning Model

* Algorithm: **Random Forest Regressor**
* Libraries: scikit-learn, pandas, numpy
* Encoding: Label Encoding for categorical features
* Evaluation Metrics:

  * MAE (Mean Absolute Error)
  * RMSE (Root Mean Squared Error)
  * R² Score

---

##  UI Features (Streamlit SaaS Design)

* Glassmorphism card layout 💎
* Animated gradient background 🌈
* Sidebar input controls ⚙️
* Metric dashboards 📊
* Feature importance graph 🔥
* Prediction range visualization 📈

---

##  Installation & Setup

###  Clone Repository

```bash
git clone https://github.com/VinithaAbhinasshree9/car-price-dashboard.git
cd car-price-dashboard
```

---

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  Run Streamlit App

```bash
streamlit run app.py
```

---

## Requirements

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

---

##  How It Works

1. User enters car details (year, fuel type, kms, etc.)
2. Data is encoded using saved label encoders
3. Model predicts selling price
4. UI displays:

   * Predicted price 
   * Feature impact 
   * Price range forecast 

---

##  Model Performance

* High accuracy using ensemble learning
* Handles nonlinear relationships effectively
* Reduces overfitting using multiple decision trees

---

##  Future Enhancements

* Add XGBoost / LightGBM models
* Deploy on Streamlit Cloud / Hugging Face
* Add database logging (SQLite/Firebase)
* Export prediction report (PDF)
* Add login authentication system
* Power BI integration dashboard

---

##  Author

**Vinitha Abhinashree M**
AI & Data Science Enthusiast 
Passionate about Machine Learning, Generative AI, and SaaS Apps

---

## ⭐ If you like this project

Give a ⭐ on the repo and share it!

---

If you want next upgrade, I can also build:
👉 **GitHub portfolio homepage for all your AI projects (ultra premium UI)**
