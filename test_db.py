from db_functions import *

# Add a movie
m = add_movie("The Matrix", 1999, 8.7)
print("Inserted movie ID:", m)

# Add genres
g1 = add_genre("Action")
g2 = add_genre("Sci-Fi")

# Link movie ↔ genres
link_movie_genre(m, g1)
link_movie_genre(m, g2)

# Add actor
a = add_actor("Keanu Reeves")
link_movie_actor(m, a)

# Query
print("Search for 'Matrix':")
print(search_movies("Matrix"))

print("Fetch by ID:")
print(get_movie_by_id(m))
