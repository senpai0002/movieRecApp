import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))


movieList = movies['title'].values


st.title("Movie Recommender")
selectionValue = st.selectbox("Select movie:", movieList)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie


if st.button("Get Recommendations"):
    movie_name = recommend(selectionValue)
    # c1= st.columns(1)
    # with c1:
    #     st.text(movie_name[0])
    # with c1:
    #     st.text(movie_name[1])
    # with c1:
    #     st.text(movie_name[2])
    # with c1:
    #     st.text(movie_name[3])
    # with c1:
    #     st.text(movie_name[4])
    st.divider()

    st.text(movie_name[0])
    st.text(movie_name[1])
    st.text(movie_name[2])
    st.text(movie_name[3])
    st.text(movie_name[4])