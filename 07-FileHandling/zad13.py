movie_titles=["The Hunger Games", "The Eras Tour", "Miss Americana", "Harry Potter", "Mamma Mia"]
file=open("movies.txt", 'w')
for movie in movie_titles:
    file.write(movie+"\n")

file.close()