# recommendation.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------- Load Dataset -----------------
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["item_profile"])  # Ensure item_profile exists
    df.reset_index(drop=True, inplace=True)
    return df

# ----------------- Build TF-IDF Matrix -----------------
def build_tfidf_matrix(text_series):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(text_series)
    return tfidf_matrix

# ----------------- Recommendation Function -----------------
def get_recommendations(product_name, df, tfidf_matrix, top_n=5):
    
    # Case-insensitive partial match
    matches = df[df['item_profile'].str.contains(product_name, case=False, na=False)]
    
    if matches.empty:
        return f"Product containing '{product_name}' not found in dataset."
    
    # Take first matched product
    idx = matches.index[0]
    
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    # Get top N similar products (excluding itself)
    sim_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]
    
    recommended = df.iloc[sim_indices][
        ['item_profile', 'sport_type', 'product_type', 'brand', 'rating']
    ].copy()
    
    recommended['similarity_score'] = cosine_sim[sim_indices]
    
    return recommended
