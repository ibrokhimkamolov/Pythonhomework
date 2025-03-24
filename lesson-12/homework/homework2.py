import requests
import random

def get_api_key():
    return "f1e38f587d7edc07e0ed0feb6a5790c8"  # Replace with your TMDB API Key

def get_genre_id(genre_name):
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": get_api_key(), "language": "en-US"}
    response = requests.get(url, params=params).json()
    
    genres = {genre["name"].lower(): genre["id"] for genre in response.get("genres", [])}
    return genres.get(genre_name.lower())

def get_movies_by_genre(genre_id):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": get_api_key(),
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc"
    }
    response = requests.get(url, params=params).json()
    return response.get("results", [])

def recommend_movie(genre_name):
    genre_id = get_genre_id(genre_name)
    if not genre_id:
        print("Genre not found. Please try again.")
        return
    
    movies = get_movies_by_genre(genre_id)
    if not movies:
        print("No movies found for this genre.")
        return
    
    movie = random.choice(movies)
    print(f"Recommended Movie: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"TMDB Rating: {movie['vote_average']}/10")

def main():
    genre = input("Enter a movie genre: ")
    recommend_movie(genre)

if __name__ == "__main__":
    main()