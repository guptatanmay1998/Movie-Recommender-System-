import streamlit as st
import pickle
import pandas as pd
import requests



def get_posters(index):
    #st.text(index)
    url = "https://api.themoviedb.org/3/movie/{}".format(index)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjOWYzZmFkOTFlNzAzNGM0YTYzMGM0MWU0OGMyNTNiNSIsInN1YiI6IjY1ODI5MDE3OTkyZmU2M2UzNjcyMzNhZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.z1klD-zi15Z_jdmgTlMX0H8xm1nOk0kzMJT5VZmuwB0"
    }

    response = requests.get(url, headers=headers)
    return "https://image.tmdb.org/t/p/w780" +response.json()['poster_path']
def recommend_movie(movie):
    index=movies_df[movies_df['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in distances[1:6]:
        recommended_movies.append(movies_df.iloc[i[0]].title)
        movie_id=movies_df.iloc[i[0]].movie_id
        recommended_movies_posters.append(get_posters(movie_id))
    return recommended_movies,recommended_movies_posters

st.title("Movies Recommender System")

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies_df=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie=st.selectbox('Which movie you want to choose',movies_dict['title'].values())

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend_movie(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])