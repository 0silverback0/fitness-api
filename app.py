import json
from sqlite3 import IntegrityError
from flask import Flask, render_template, request, redirect, jsonify
from models import connect_db, db, Exercise
from forms import DataForm
from flask_migrate import Migrate
import os
from flask_cors import CORS
from sqlalchemy import exc 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')

CORS(app)

with app.app_context():
    connect_db(app)
    migrate = Migrate(app, db)

@app.route('/')
def home():
    return redirect('/get-exercises')

@app.route('/get-exercises')
def get_exercises():
    exercises = Exercise.query.all()
    try:
        return jsonify({
            'success': True,
            "exercises" : [exercise.format() for exercise in exercises]
        })
    except Exception as error:
        return jsonify({
            'success': False,
            'error': str(error)
        })

@app.route('/search')
def search():
    """ Get all exercises by name matching the search term """
    term = request.args.get('exercise')
    try:
        exercise = Exercise.query.filter(Exercise.name.ilike(f'%{term}%')).first()
        return jsonify({
            'id': exercise.id,
            'name': exercise.name,
            'primary_muscle': exercise.primary_muscle,
            'similar_exercises': [ex.format() for ex in Exercise.query.filter_by(primary_muscle=exercise.primary_muscle).all() if exercise.id != ex.id],
            'region': exercise.region,
            'movememnt_type': exercise.movement_type,
            'term': term
        })
    except exc.MultipleResultsFound as error:
        return jsonify({
            'error': str(error),
            'success': False
        })
    except exc.NoResultFound as error:
        return jsonify({
            'error': str(error),
            'success': False
        })
    except AttributeError as error:
         return jsonify({
            'error': str(error),
            'success': False
        })

@app.route('/search/<primary_muscle>')
def search_by_primary_muscle(primary_muscle):
    exercises = Exercise.query.filter(Exercise.primary_muscle.ilike(f'%{primary_muscle}%')).all()

    if exercises ==[]:
         return jsonify({
            'success': False,
            'error': 'check you spelling'
        })
    else:

        try:
            
            return jsonify({
                'success': True,
                'primary_muscle': primary_muscle,
                'exercises': [ex.format() for ex in exercises]
            })

        except Exception as error:
            return jsonify({
                'success': False,
                'error': str(error)
            })

###### ADMIN DASHBOARD #######


###### ADMIN HOME ######
@app.route('/admin')
def dashboard():
    exercises = Exercise.query.all()
    form = DataForm()
    return render_template('add-exercise.html', exercises=exercises, form=form)


####### ADD EXERCISE #########
@app.route('/add-exercise', methods=['POST'])
def add_exercise():
    form = DataForm()
    try:
        if form.validate_on_submit():
            name = form.name.data
            primary_muscle = form.primary_muscle.data
            region = form.region.data
            movement_type = form.movement_type.data

            new_exercise = Exercise(name=name, primary_muscle=primary_muscle,
            region=region,movement_type=movement_type)
            new_exercise.insert()

            return redirect('/admin')
    except Exception as error:
        return jsonify({
            'success': False,
            'error': str(error)
        })
    #### returns here when error ####
    return redirect('/admin')
    


######## EDIT EXERCISE ########
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_exercise(id):
    exercise = Exercise.query.get(id)
    exercise.format()
    form = DataForm(obj=exercise)

    try:
        if form.validate_on_submit():
            exercise.name = form.name.data
            exercise.primary_muscle = form.primary_muscle.data
            # exercise.similar_exercises = form.similar_exercises.data.split(',')
            exercise.region = form.region.data
            exercise.movement_type = form.movement_type.data

            exercise.update()

            return redirect('/admin')
    except Exception as e:
        print(e)
   
    return render_template('edit-exercise.html', form=form, exercise=exercise)


###### DELETE EXERCISE ######
@app.route('/delete/<int:id>')
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    exercise.delete()
    return redirect('/admin')