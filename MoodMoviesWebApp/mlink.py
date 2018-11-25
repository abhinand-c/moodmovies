
def murl(genre,lang="",lrating="",urating=""):
    genre=genre.lower()
    return "https://www.imdb.com/search/title?user_rating="+ lrating +","+urating+"&genres="+ genre+"&languages="+lang


