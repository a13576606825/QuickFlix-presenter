"""
Core: Implements all core functions required
~~~
"""
import logging
from difflib import SequenceMatcher

from store.read import get_movies, get_reviews, get_movie_info


log = logging.getLogger(__name__)

BLUR_MATCH_NUMBER = 5

def similar(a, b):
    '''
    compare similarity of two string
    '''
    return SequenceMatcher(None, a, b).ratio()


def blur_match(query):
    '''
    find the most N similar movies in dbs
    '''
    movieTitleList = get_movies()
    rankedMovieTitles = []
    for title in movieTitleList:
        rankedMovie = {'title': title, 'rank': similar(query, title)}
        rankedMovieTitles.append(rankedMovie)
    def getMovieRank(movie):
        return movie['rank']
    rankedMovieTitles.sort(key=getMovieRank , reverse=True)

    N = BLUR_MATCH_NUMBER if len(rankedMovieTitles) >= BLUR_MATCH_NUMBER else len(rankedMovieTitles)
    isBlur = rankedMovieTitles[0]['rank'] < 1
    return isBlur, rankedMovieTitles[:N]

def retrieveResult(title):
    '''
    retrieve movie review results by a movie title
    '''
    return get_reviews(title)
    for i in range(10):
        results.append(a)
    return results

def retrieve_movie_info(title):
    '''
    retrieve movie info by a movie title
    '''
    return get_movie_info(title)
