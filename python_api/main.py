import csv
from fastapi import FastAPI

app = FastAPI()


class Movie:
    def __init__(self, movie_id, title, genres):
        self.id = movie_id
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.id = movie_id
        self.imdbId = imdb_id
        self.tmdbId = tmdb_id

class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.tag = tag
        self.timestamp = timestamp


def load_data(file_path, model_class):
    data_list = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                obj = model_class(*row)
                data_list.append(obj.__dict__)
    except FileNotFoundError:
        return {"error": f"Plik {file_path} nie został znaleziony."}
    return data_list

# endpointy
@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/movies")
def get_movies():
    return load_data('movies.csv', Movie)


@app.get("/links")
def get_links():
    return load_data('links.csv', Link)

@app.get("/ratings")
def get_ratings():
    return load_data('ratings.csv', Rating)

@app.get("/tags")
def get_tags():
    return load_data('tags.csv', Tag)