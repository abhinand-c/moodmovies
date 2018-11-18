from imdb import *
x=IMDb()
def retname(gen):
    top = x.get_top250_movies()
    for i in top:
        a=x.get_movie(i.movieID)
        if(gen in a['genres']):
            return a
