import csv
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    imdbId = Column(String)
    tmdbId = Column(String)


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer)
    movieId = Column(Integer)
    rating = Column(Float)
    timestamp = Column(Integer)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer)
    movieId = Column(Integer)
    tag = Column(String)
    timestamp = Column(Integer)



Base.metadata.create_all(bind=engine)



def init_db():
    db = SessionLocal()
    try:
        if db.query(Movie).first() is None:
            with open('movies.csv', mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                db.bulk_save_objects([Movie(id=r['movieId'], title=r['title'], genres=r['genres']) for r in reader])
            print("✅ Załadowano movies.csv")

        if db.query(Link).first() is None:
            with open('links.csv', mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                db.bulk_save_objects([Link(id=r['movieId'], imdbId=r['imdbId'], tmdbId=r['tmdbId']) for r in reader])
            print("✅ Załadowano links.csv")

        if db.query(Rating).first() is None:
            with open('ratings.csv', mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                db.bulk_save_objects(
                    [Rating(userId=r['userId'], movieId=r['movieId'], rating=r['rating'], timestamp=r['timestamp']) for
                     r in reader])
            print("✅ Załadowano ratings.csv")

        if db.query(Tag).first() is None:
            with open('tags.csv', mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                db.bulk_save_objects(
                    [Tag(userId=r['userId'], movieId=r['movieId'], tag=r['tag'], timestamp=r['timestamp']) for r in
                     reader])
            print("✅ Załadowano tags.csv")

        db.commit()
    except Exception as e:
        print(f"Błąd ładowania: {e}")
        db.rollback()
    finally:
        db.close()


init_db()


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()


@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return db.query(Rating).all()


@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()