from email.policy import default
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
    name = db.Column(db.String, unique=True, nullable=False)
    primary_muscle = db.Column(db.String, nullable=False, default='unknown')
    region = db.Column(db.String())
    movement_type = db.Column(db.String())
    difficulty = db.Column(db.String)
    description = db.Column(db.String)

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "primary_muscle": self.primary_muscle,
            "region": self.region,
            "movement_type": self.movement_type,
            "difficulty": self.difficulty,
            "description": self.description
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    