import csv
from fastapi import FastAPI

app = FastAPI()

class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres


@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/movies")
def get_movies():
    movies_list = []


    with open('movies.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:

            movie_obj = Movie(movie_id=row[0], title=row[1], genres=row[2])


            movies_list.append(movie_obj.__dict__)

    return movies_list

class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

@app.get("/tags")
def get_tags():
    tags_list = []

    with open('tags.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            tag_obj = Tag(user_id=row[0], movie_id=row[1], tag=row[2], timestamp=row[3])
            tags_list.append(tag_obj.__dict__)

    return tags_list



class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp



@app.get("/ratings")
def get_ratings():
    ratings_list = []

    with open('ratings.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            rating_obj = Rating(user_id=row[0], movie_id=row[1], rating=row[2], timestamp=row[3])
            ratings_list.append(rating_obj.__dict__)

    return ratings_list