import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

        temp = poster[
            poster["tmdb_id"] == movies.iloc[i[0]]["movie_id"]
        ]["poster"]

        if len(temp) > 0:
            recommended_posters.append(temp.values[0])
        else:
            recommended_posters.append(None)

    return recommended_movies, recommended_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

poster = pickle.load(open('poster.pkl', 'rb'))

# Optional: fix datatype mismatch
movies["movie_id"] = movies["movie_id"].astype(str)
poster["tmdb_id"] = poster["tmdb_id"].astype(str)

st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])