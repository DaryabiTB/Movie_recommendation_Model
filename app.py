import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommender System")

movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))

all_movies_list = pd.DataFrame(movie_dict)

# input value for the select input.
option = st.selectbox(
    'Select Your Movie', all_movies_list['title'].values)

similarity = pickle.load(open("similarity.pkl", 'rb'))


def recommend(selected_movie_name):
    # find the given movie index in the newDF list

    # newDF[newDF['title'] == movie].index  ==== Int64Index([119], dtype='int64')
    movie_index = all_movies_list[all_movies_list['title'] == selected_movie_name].index[0]

    # similarity gives us the distances between the given movie with all other movies in the list.
    # similarity[0] ==== array([1.        , 0.44556639, 0.31354672, ..., 0.05292561, 0.        ,
    #                          0.        ])
    distance = similarity[movie_index]

    # sorting and keeping the indexes safe. top five , it returns the movies indexes and its distance.
    recommend_movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    # movies_list is a tuple with index and distance value. we are getting the title from the indexes
    # i[0] is the index from tuple (1111, 0.0000469) in movies_list tuple
    # iloc[i[0]] is row in the data frame
    recommended_list = []
    for i in recommend_movies_list:
        recommended_list.append(all_movies_list.iloc[i[0]].title)
    return recommended_list


if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
