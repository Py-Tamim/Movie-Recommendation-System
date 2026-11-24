# Movie Recommendation System Using Machine Learning 🎬

A Python-based movie recommendation system that suggests movies based on user-selected genres and descriptions.

The project uses the **TMDB API** to retrieve movie information and **TF-IDF Vectorization with Cosine Similarity** to rank movies according to the user's preferences.

## 📌 Project Overview

The system combines two recommendation approaches:

1. **Genre-Based Filtering:** Finds movies based on selected genres and sub-genres.
2. **Content-Based Filtering:** Compares the user's description with movie overviews using TF-IDF and Cosine Similarity.

If no description is provided, movies are displayed based on their TMDB ratings.

## ✨ Key Features

- Search using one main genre and two optional sub-genres.
- Recommend movies based on user descriptions.
- Retrieve movie information directly from TMDB.
- Filter out movies with fewer than 1,000 votes.
- Rank movies using text similarity or TMDB ratings.
- Display five recommendations at a time.
- Simple interactive terminal interface.

## 🤖 Recommendation Techniques

**1. Genre-Based Filtering**

The system converts selected genres into TMDB genre IDs and uses them to retrieve matching movies.

**2. TF-IDF Vectorization**

Converts movie overviews and the user's description into numerical vectors.

**3. Cosine Similarity**

Measures the similarity between the user's description and each movie overview. Movies with higher similarity scores appear first.

\[
\text{Cosine Similarity}(A,B)=
\frac{A\cdot B}{\|A\|\|B\|}
\]

## 🔄 How It Works

1. The user enters a genre, optional sub-genres, and a movie description.
2. The system validates the selected genres.
3. It retrieves up to three pages of movie results from TMDB.
4. Movie information is processed using Pandas.
5. TF-IDF and Cosine Similarity rank movies when a description is provided.
6. The system displays five movies at a time and allows users to request more.

## 🖥️ Example Input

```text
Genre: Action
Sub_Genre_1: Thriller
Sub_Genre_2: Mystery
Description: A detective investigating a dangerous criminal organization.
```

The system returns matching movie titles, ratings, and overviews.

*Note: Actual recommendations depend on TMDB API results.*

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | TMDB API requests |
| Pandas | Movie data processing |
| Scikit-learn | Text processing |
| TF-IDF | Text vectorization |
| Cosine Similarity | Text similarity calculation |
| TMDB API | Movie information |

## 🌐 TMDB API Setup

This project requires a personal TMDB API key.

1. Create an account at [TMDB](https://www.themoviedb.org/).
2. Visit [TMDB API Settings](https://www.themoviedb.org/settings/api).
3. Generate an API key.
4. Add it to the Python script:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

**Important:** Never upload your private API key to a public GitHub repository.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install the required libraries:

```bash
pip install requests pandas scikit-learn
```

Run the project:

```bash
python movie_recommendation.py
```

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── movie_recommendation.py
├── requirements.txt
└── README.md
```

## ⚠️ Limitations

- Requires an internet connection and a valid TMDB API key.
- Retrieves only three pages of results per search (up to approximately 60 movies).
- Uses movie overviews for text similarity.
- Does not consider user ratings or watch history.
- Uses `msvcrt` for the Esc key, making the current exit mechanism Windows-specific.

## 🚀 Future Improvements

- Add a graphical interface using Streamlit or Tkinter.
- Include movie posters, trailers, and release dates.
- Improve recommendations using actors, directors, and keywords.
- Implement collaborative or hybrid filtering.
- Use advanced NLP models such as Sentence Transformers.
- Add user accounts and personalized watchlists.

## 🤝 AI Assistance & Acknowledgement

AI tools were used as supporting resources during research and development, mainly to:

- Explore and refine the project idea.
- Identify suitable movie datasets and data sources, including TMDB.
- Compare recommendation techniques and select suitable approaches.
- Understand TF-IDF, Cosine Similarity, and API integration.

I used AI as a learning and research assistant. I reviewed the suggestions and applied them during my own development and learning process.

---

This project is developed for educational purposes. Movie information is retrieved through the TMDB API and is subject to its terms and attribution requirements.
