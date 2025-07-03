from flask import Flask, render_template, Blueprint
from config import Config
from app.base import db
from app.actor import Actor
from app.movie import Movie

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/movies')
def show_movies():
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)

@main_bp.route('/actors')
def show_actors():
    actors = Actor.query.all()
    return render_template('actors.html', actors=actors)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

        if not Movie.query.first():
            # Перший фільм і актори
            actor1 = Actor(name="Leonardo DiCaprio")
            actor2 = Actor(name="Joseph Gordon-Levitt")
            movie1 = Movie(title="Inception")
            movie1.actors.extend([actor1, actor2])

            

            db.session.add_all([movie1])
            db.session.commit()

    app.register_blueprint(main_bp)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

