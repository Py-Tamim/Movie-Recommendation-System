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

movies = []                      # Ask the API for movies (3 pages = 60 movies), best rated first
for page in [1, 2, 3]:
    params = {
        "api_key": API_KEY,
        "with_genres": ",".join(ids),
        "sort_by": "vote_average.desc",
        "vote_count.gte": 1000,
        "page": page,
    }
    data = requests.get("https://api.themoviedb.org/3/discover/movie", params=params).json()
    movies += data.get("results", [])
if not movies:
    print("\nNo movies found. Check your API key or try different genres.")
    exit()

result = pd.DataFrame(movies)

if desc:                       # If a description is given, rank by similarity. Otherwise keep the rating order.
    texts = result["overview"].fillna("").tolist() + [desc]
    matrix = TfidfVectorizer(stop_words="english").fit_transform(texts)
    result["score"] = cosine_similarity(matrix[-1], matrix[:-1])[0]
    result = result.sort_values("score", ascending=False)


print("\nTop movie predictions for you:")

start = 0                     # For continious Searching Movie
while True:
    batch = result.iloc[start:start + 5]

    if batch.empty:
        print("\nNo more movies to show.")
        break

    for _, row in batch.iterrows():
        print(f"\n{row['title']} ({round(row['vote_average'], 1)}/10):")
        print(row["overview"])

    start += 5

    answer = ""
    while answer not in ["yes", "no"]:
        answer = input("\nDo you need more suggestion (yes/ no): ").strip().lower()

    if answer == "no":
        break

# Wait until the Esc key is pressed
print('\nPress "Esc" to exit.')
while msvcrt.getch() != b"\x1b":
    pass