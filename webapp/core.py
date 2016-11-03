import logging
from difflib import SequenceMatcher

from store.read import get_movies, get_reviews, get_movie_info

log = logging.getLogger(__name__)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def blur_match(query):

    # movieTitleList = ['The Shawshank Redemption',
    # 'The Godfather',
    # 'The Godfather 2',
    # 'The Dark Knight',
    # "Schindler's List",
    # '12 Angry Men',
    # 'Pulp Fiction',
    # 'The Lord Of The Rings: The Return Of The King']
    movieTitleList = get_movies()
    rankedMovieTitles = []
    for title in movieTitleList:
        rankedMovie = {'title': title, 'rank': similar(query, title)}
        rankedMovieTitles.append(rankedMovie)
    def getMovieRank(movie):
        return movie['rank']
    rankedMovieTitles.sort(key=getMovieRank , reverse=True)

    N = 5 if len(rankedMovieTitles) >= 5 else len(rankedMovieTitles)
    isBlur = rankedMovieTitles[0]['rank'] < 1
    return isBlur, rankedMovieTitles[:N]

def retrieveResult(title):
    a = {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."}
    results = [
    {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."},

    {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."},

    {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."},
    ]
    return get_reviews(title)
    for i in range(10):
        results.append(a)
    return results
def retrieve_movie_info(title):
    return get_movie_info(title)
