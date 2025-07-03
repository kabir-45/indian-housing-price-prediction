# 🏠 Indian Housing Price Prediction

## 📌 About

This project aims to predict housing prices in major Indian Tier-1 cities using machine learning techniques. The dataset includes information about location, number of bedrooms, square footage, and various other features relevant to real estate.

The goal is to provide an accurate price prediction model that can help potential buyers, real estate developers, and investors make informed decisions. The model has been trained using a regression approach and the performance has been validated using standard evaluation metrics.

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kabir-45/indian-housing-price-prediction.git
   cd indian-housing-price-prediction

2. **Run Kaggle Notebook**  
   [Indian Tier-1 City Housing Price Prediction – Kaggle Notebook](https://www.kaggle.com/code/shortyrex/indian-tier-1-city-housing-price-prediction)

   
## 🚀 Deployment

The model has been deployed using **Streamlit** to provide a user-friendly web interface.  
Users can enter key features such as **location**, **number of rooms**, **furnishing type**, and more — and receive a **predicted price range** instantly.

![Input Form](images/Screenshot%202025-07-03%20173819.png)          ![Prediction Output](images/Screenshot%202025-07-03%20173910.png)

## 🚀 Streamlit App

To run the interactive app:

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run HomePage.py
