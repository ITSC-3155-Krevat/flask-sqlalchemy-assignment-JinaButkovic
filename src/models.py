# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# CREATE TABLE movie (
#     movie_id INT          AUTO_INCREMENT,
#     title    VARCHAR(255) NOT NULL,
#     director VARCHAR(255) NOT NULL,
#     rating   INT NOT      NULL,
#     PRIMARY KEY (movie_id)
# );

class Movie(db.Model):  
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Movie({self.movie_id}, {self.title}, {self.director}, {self.rating})'
    