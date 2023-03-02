from flask_wtf import FlaskForm
from wtforms.validators import DataRequired 
from wtforms import StringField, SelectField

class DataForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    primary_muscle = StringField('Primary Muscle', validators=[DataRequired()])
    region = SelectField('Region', choices=[ ('upper anterior', 'upper anterior'),
    ('upper posterior', 'upper posterior'), ('lower anterior', 'lower anterior'),
    ('lower posterior', 'lower posterior')], validators=[DataRequired()])
    movement_type = SelectField('Movement Type', choices=[ ('push', 'push'),
    ('pull', 'pull')], validators=[DataRequired()])
    difficulty = SelectField('Difficulty', choices=[('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])


    