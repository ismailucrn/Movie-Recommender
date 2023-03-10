import pickle
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


df2 = pickle.load(open(current_dir + "/dataframe.pkl","rb"))
indices = pickle.load(open(current_dir + "/indices.pkl","rb"))
cosine_sim = pickle.load(open(current_dir + "/cosine_sim.pkl","rb"))

def get_recommendations(title, cosine_sim=cosine_sim):

    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = (sorted(sim_scores, key=lambda x: x[1], reverse=True))

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[0:4]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    result = df2['title'].iloc[movie_indices]._values
    # Return the top 10 most similar movies
    return result
    
liste = ["Avatar", "Alvin and the Chipmunks: Chipwrecked", "The Dark Knight Rises", "The Avengers","Spider-Man 3"]


def movie_recommender(liste):
    result = []
    for i in range(len(liste)):
        result.append(get_recommendations(liste[i]))
    result = [item for sublist in result for item in sublist]
    final = []
    for i in range(len(result)):
        final.append(get_recommendations(result[i]))
    final = [item for sublist in final for item in sublist]
    for i in range(len(liste)):
        if liste[i] in final:
            final = list(filter(lambda a: a != liste[i], final))
    movie_dict = {}
    for i in range(len(final)):
        if final[i] in movie_dict:
            movie_dict[final[i]] += 1
        else:
            movie_dict[final[i]] = 1
    movie_dict = {k: v for k, v in sorted(movie_dict.items(), key=lambda item: item[1], reverse=True)}
    return list(movie_dict.keys())[0:5]

#print(movie_recommender(liste))

def movie_dict(liste):
    movie_dict_list = []
    for film in movie_recommender(liste):
        movie_dict_list.append((df2.loc[df2["original_title"] == film]).to_dict())
    return movie_dict_list


a = movie_dict(liste)
print(movie_dict(liste))