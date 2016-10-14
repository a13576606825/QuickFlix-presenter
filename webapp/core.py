import logging
from difflib import SequenceMatcher

log = logging.getLogger(__name__)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def blur_match(query):
    movieTitleList = ['The Shawshank Redemption',
    'The Godfather',
    'The Godfather 2',
    'The Dark Knight',
    "Schindler's List",
    '12 Angry Men',
    'Pulp Fiction',
    'The Lord Of The Rings: The Return Of The King']

    isBlur = True
    maxSimilarity = 0
    matchTitle = None
    for title in movieTitleList:
        curentSimilarity = similar(query, title)
        if curentSimilarity == 1:
            return False, title, maxSimilarity
        elif curentSimilarity > maxSimilarity:
            maxSimilarity = similar(query, title)
            matchTitle = title

    return isBlur, matchTitle, maxSimilarity


def retrieveResult(title):

    results = [
    {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."},

    {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."},

    {'title':'The Magnificent Seven review', 'domain':'Metacritic', 'url':"https://www.theguardian.com/film/2016/sep/22/the-magnificent-seven-review-denzel-washington", 'descripton':"Antoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-stylAntoine Fuqua's superhero-style take on the 1960 western has a starry cast, from Denzel Washington to Ethan Hawke, but his gunslingers ..."},
    ]
    return results
