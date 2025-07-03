from app.base import db
from app.associations import movie_actor

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    actors = db.relationship(
        'Actor',
        secondary=movie_actor,
        backref=db.backref('movies', lazy='dynamic')
    )
