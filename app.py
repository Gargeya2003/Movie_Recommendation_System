import pickle
import streamlit as st
import requests

st.header("Movie Recommendation using ML")
movies = pickle.load(open('artifacts/movieslist.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values

movie = st.selectbox(
    'Type or select a movie to get recommendations',
    movie_list
)

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    poster_path = "http://image.tmdb.org/t/p/w500/" + poster_path

    return poster_path

def recommend_movie(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x : x[1])
    recommended_movies_names = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[i[0]].title)

    return recommended_movies_names, recommended_movies_poster

if st.button('Show Recommendations'):
    recommended_movies, recommended_movies_posters = recommend_movie(movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])
