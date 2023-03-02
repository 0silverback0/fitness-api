from flask_wtf import FlaskForm
from wtforms.validators import DataRequired 
from wtforms import StringField, SelectField

class DataForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    primary_muscle = StringField('Primary Muscle', validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    movement_type = StringField('Movement Type', validators=[DataRequired()])
    difficulty = SelectField('Difficulty', choices=[('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])


    