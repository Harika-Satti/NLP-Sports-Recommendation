# 🛍️ Amazon Sports Product Recommendation System

## 📌 Overview
This project implements a Content-Based Recommendation System that suggests similar sports products based on textual product descriptions.

The system uses TF-IDF Vectorization and Cosine Similarity to compute similarity between products and recommend the most relevant items.

The application is built using Streamlit to provide an interactive and user-friendly interface.

## 🚀 Features
- Search products using partial product names (e.g., Nike, Racket, Shoes)
- TF-IDF based text vectorization
- Cosine similarity for product matching
- Interactive web application using Streamlit
- Displays top recommended products with similarity scores

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Natural Language Processing (TF-IDF)

## ⚙️ How It Works
1. Load the sports product dataset
2. Clean and preprocess product descriptions
3. Convert text into TF-IDF vectors
4. Compute cosine similarity between products
5. Return top 5 most similar products

## 📂 Project Structure

NLP-Sports-Recommendation/
│
├── app.py
├── recommendation.py
├── Sports-Amazon dataset.csv
├── requirements.txt
└── README.md

## ▶️ How to Run the Project

### Step 1: Install Dependencies

pip install -r requirements.txt

If requirements.txt is not available:

pip install streamlit pandas scikit-learn

### Step 2: Run the Application

streamlit run app.py

### Step 3: Open in Browser

Streamlit will automatically open:
http://localhost:8501

## 📊 Recommendation Logic
- TF-IDF Vectorizer converts product descriptions into numerical feature vectors.
- Cosine similarity calculates similarity between products.
- The system returns the top 5 most similar items.

## 🎯 Future Enhancements
- Add collaborative filtering (Hybrid Recommendation)
- Improve UI design
- Add product images
- Add evaluation metrics (Precision@K, Recall@K)
- Deploy on Streamlit Cloud

## 👩‍💻 Author
Harika Satti  
Aspiring Data Scientist | Machine Learning Enthusiast
