# app.py
import streamlit as st
from recommendation import load_data, build_tfidf_matrix, get_recommendations

st.set_page_config(page_title="Amazon Product Recommendation", layout="wide")
st.title("🛍️ Amazon Product Recommendation System")

# ---------------- Load Data ----------------
@st.cache_data
def load_dataset():
    return load_data("Sports-Amazon dataset.csv")


df = load_dataset()

# ---------------- Build TF-IDF Matrix ----------------
@st.cache_data
def build_matrix():
    return build_tfidf_matrix(df['item_profile'])

tfidf_matrix = build_matrix()

# ---------------- User Input ----------------
product_input = st.text_input(
    "Enter part of a product name (example: Nike, Racket, Shoes):"
)


if st.button("Get Recommendations"):
    if product_input.strip() == "":
        st.warning("Please enter a product name!")
    else:
        recommendations = get_recommendations(product_input.strip(), df, tfidf_matrix, top_n=5)
        if isinstance(recommendations, str):
            st.error(recommendations)
        else:
            st.subheader("Recommended Products:")
            st.table(recommendations)
