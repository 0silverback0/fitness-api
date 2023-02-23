from flask import Flask, render_template, request, redirect, jsonify
from models import connect_db, db, Exercise
from flask_migrate import Migrate
import os
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
CORS(app)

with app.app_context():
    connect_db(app)
    migrate = Migrate(app, db)

@app.route('/')
def home():
    # exercises = Exercise.query.all()
    
    # return jsonify({
    #     'name': [exercise.name for exercise in exercises],
    #     'success': True
    # })
    return redirect('/get-exercises')

@app.route('/get-exercises')
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify({
        # 'exercise': [exercise.name for exercise in exercises],
        # 'similar exercises': [exercise.similar_exercises for exercise in exercises],
        'success': True,
        "exercises" : [exercise.format() for exercise in exercises]
    })

###### ADMIN DASHBOARD #######

@app.route('/add-exercise', methods=['POST'])
def add_exercise():
    name = request.form.get('exercise')
    primary_muscle = request.form.get('primary-muscle')
    similar_exercises = request.form.get('similar-exercises')
    similar_exercises = similar_exercises.split(',')
    print(similar_exercises)

    new_exercise = Exercise(name=name, primary_muscle=primary_muscle, similar_exercises=similar_exercises)
    db.session.add(new_exercise)
    db.session.commit()

    return redirect('/')

@app.route('/admin')
def dashboard():
    exercises = Exercise.query.all()
    return render_template('add-exercise.html', exercises=exercises)