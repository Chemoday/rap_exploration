from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, validators
from wtforms.validators import DataRequired


class AssesmentForm(FlaskForm):

    choices = [
        ('0', '0'), # data, label
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    label_0 = RadioField('label_0', choices=choices, default='0', validators=[validators.DataRequired()]) #add a validator
    label_1 = RadioField('label_1', choices=choices, default='0', validators=[validators.DataRequired()]) #add a validator
    label_2 = RadioField('label_2', choices=choices, default='0', validators=[validators.DataRequired()]) #add a validator
    label_3 = RadioField('label_3', choices=choices, default='0', validators=[validators.DataRequired()]) #add a validator
    label_4 = RadioField('label_4', choices=choices, default='0', validators=[validators.DataRequired()]) #add a validator
    label_5 = RadioField('label_5', choices=choices, default='0', validators=[validators.DataRequired()]) #add a validator
    submit = SubmitField('Analyze')
