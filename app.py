import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the movies dictionary (this assumes you already have a pickle file)
file_path = "/Users/states/Downloads/movie_dict.pkl"  # Change to your file path
with open(file_path, 'rb') as file:
    movies_dict = pickle.load(file)

# Convert the dictionary to a DataFrame
movies = pd.DataFrame(movies_dict)

# Load the similarity matrix
similarity_path = "/Users/states/Downloads/similarity.pkl"  # Change to your file path
with open(similarity_path, 'rb') as file:
    similarity = pickle.load(file)

# Streamlit app title
st.title('Simple Movie Recommender System')

# Dropdown to select a movie for recommendation
movie_option = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Button to trigger the recommendation
if st.button('Recommend'):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie_option].index[0]
    
    # Get similarity scores for the selected movie
    similar_movies = list(enumerate(similarity[movie_index]))
    
    # Sort movies based on similarity scores
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:6]
    
    # Display the top 5 similar movies
    st.write(f"Top 5 recommended movies similar to: {movie_option}")
    for idx, (movie_idx, _) in enumerate(sorted_similar_movies):
        st.write(f"{idx + 1}. {movies.iloc[movie_idx]['title']}")
