import requests
import msvcrt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

API_KEY = "Use your API Key"        # TMDB API Key (Use Your one)

# You need to apply for TMDB API Key

genre_ids = {                   # TMDB uses a number for each genre
    "action": 28, "adventure": 12, "animation": 16, "comedy": 35,
    "crime": 80, "documentary": 99, "drama": 18, "family": 10751,
    "fantasy": 14, "history": 36, "horror": 27, "music": 10402,
    "mystery": 9648, "romance": 10749, "scifi": 878, "sciencefiction": 878,
    "thriller": 53, "war": 10752, "western": 37,
}

def clean(text):                # Make text lowercase and remove spaces/dashes so "Sci Fi" becomes "scifi"
    return text.lower().replace(" ", "").replace("-", "")
print("=" * 34 + " Welcome " + "=" * 34)
print("Give me some information:")
genre = input("Genre: ")
sub1 = input("Sub_Genre_1 (press enter to skip): ")
sub2 = input("Sub_Genre_2 (press enter to skip): ")
desc = input("Description (press enter to skip): ")

ids = []                         # Turn the typed genres into TMDB genre numbers
for g in [genre, sub1, sub2]:
    if g:
        if clean(g) not in genre_ids:
            print("Unknown genre:", g)
            exit()
        ids.append(str(genre_ids[clean(g)]))

