from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    primary_muscle = db.Column(db.String, nullable=False)
    similar_exercises = db.Column(db.ARRAY(db.String))

    def format(self):
        return {
            "name": self.name,
            "primary_muscle": self.primary_muscle,
            "similar_exercises": self.similar_exercises
        }

    