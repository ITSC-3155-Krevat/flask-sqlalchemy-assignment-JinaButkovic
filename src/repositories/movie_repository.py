from models import Movie
from models import db
class MovieRepository:
    

    def get_all_movies(self):
        # TODO get all movies from the DB
        Movie.query.all()
        return None

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        Movie.query.get(movie_id)
        return None

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_movie = Movie(title='West Side Story', director='Steven Spielberg', rating='4.3')
        db.session.add(new_movie)
        db.session.commit()
        return None

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        #https://docs.sqlalchemy.org/en/14/core/operators.html was used to read and impliment the ilike operator which gets all movie titles matching case insenstivie substring.
        print(('title').ilike('word'))
        return None


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
