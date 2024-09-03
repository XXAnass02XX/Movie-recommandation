import streamlit as st
import pandas as pd
from users import Person

@st.cache_data
def load_data():
    df_dataSet = pd.read_csv('../../dataset/processed_data_set.csv')
    columns = df_dataSet.columns
    User1 = Person()
    User1.watched_movies = pd.DataFrame(columns=columns)
    return df_dataSet , User1

def get_movie_suggestions(input_text, movies_df):
    if input_text:
        # Filter movies that start with the input text (case insensitive)
        suggestions = movies_df[movies_df['title'].str.contains(f"^{input_text}", case=False)]['title'].tolist()
    else:
        suggestions = []
    return suggestions

if 'df_dataSet' not in st.session_state or 'User1' not in st.session_state:
    st.session_state.df_dataSet, st.session_state.User1 = load_data()

df_dataSet = st.session_state.df_dataSet
User1 = st.session_state.User1

st.title("Movie Recommendation System")

#st.write(df_dataSet['title'])

st.info("Please give us a movie name that you have watched:")
user_input_name = st.text_input("Start typing the movie's name ,e.g : if you want to look for inception just write inc and click enter")

suggestions = get_movie_suggestions(user_input_name, df_dataSet)
selected_movie = st.selectbox("Select a movie:", suggestions)

st.info("Please give us a rating for this movie:")
user_input_rating = st.text_input("type the rating , from -10 to 10 , -10 you hated it and 10 you liked it very much")

if st.button("Add movie and rating"):
    if not selected_movie or not user_input_rating :
        st.warning("Please make sure to select a movie and give us a rating")
    else :
        User1.add_movie(selected_movie,float(user_input_rating),df_dataSet)
        st.success("Your movie has been added")
        st.session_state.User1 = User1 # update the user state

if User1.watched_movies is not None and not User1.watched_movies.empty:
    delete_index = st.number_input("Enter the index of the movie to delete:", min_value=0, max_value=len(User1.watched_movies)-1, step=1)
    if st.button("Delete movie"):
        User1.delete_movie(delete_index)
        st.success(f"Movie at index {delete_index} has been deleted")
        st.session_state.User1 = User1  # update the user state
    st.info("Your watched movies:")
    st.dataframe(User1.watched_movies[['title', 'rating']])

if st.button("get recommendations"):
    if User1.watched_movies is None or len(User1.watched_movies) == 0 : 
        st.error("please select at least one movie")
    else :
        User1.calculate_user_profile()
        movies_rating_prediction = User1.movies_score(df_dataSet)
        st.write(User1.movies_score(df_dataSet)['Movie'].head())
