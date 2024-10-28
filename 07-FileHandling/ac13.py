movie_titles=["The Hunger Games", "The Eras Tour", "Miss Americana", "Harry Potter", "Mamma Mia"]
with open("movies2.txt", 'w')as file:
    for movie in movie_titles:
        file.write(movie+'\n')
