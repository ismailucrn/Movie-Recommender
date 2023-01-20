import streamlit as st
import rec_funct
import pandas as pd
from rec_funct import df2  

st.title("Movie Recommender")


def get_image_url_from_loc_by_name(name):
    print(name)
    deneme = (df2.loc[df2["original_title"] == name]).to_dict()
    print(deneme)
    return deneme

movies_label = ["1","2","3","4","5"]
movie_list = []
for i in range(len(movies_label)):
    movie_list.append(st.selectbox(f"Please select number {i+1} movies for recommendation",rec_funct.df2["original_title"].values, key = i))

if st.button("Recommend"):
    for i in range(len(movie_list)):
        if movie_list[i] == "":
            st.write("Please select a movie")
            break
    else:
        st.header("Your recommendations are:")
        local_movie_list = rec_funct.movie_recommender(movie_list)
        for i in range(len(local_movie_list)):
            title_container = st.container()
            col1, col2 = st.columns([1, 2])
            with title_container:
                with col1:
                    st.subheader(local_movie_list[i])
                    st.image((rec_funct.df2.loc[rec_funct.df2["original_title"] == (rec_funct.movie_recommender(movie_list)[i])]["image_url"].iloc[0]),width=200)
                with col2:
                    st.subheader("")
                    st.subheader("")
                    st.subheader("")
                    st.subheader("Description:")
                    st.write((rec_funct.df2.loc[rec_funct.df2["original_title"] == (rec_funct.movie_recommender(movie_list)[i])]["overview"].iloc[0]))
