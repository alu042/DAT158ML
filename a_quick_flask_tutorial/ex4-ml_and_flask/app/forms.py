from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    rcount = IntegerField('Number of readmissions past 180 days', validators=[DataRequired()])
    gender = IntegerField('Gender. 0=Male, 1=Female', validators=[NumberRange(min=0, max=1)])

    bmi = FloatField('Average BMI during encounter')
    sodium = FloatField('Average sodium level during encounter')

    asthma = BooleanField(label='Asthma')
    irondef = BooleanField(label='Iron deficiency')
    depress = BooleanField(label='Depression')
    malnutrition = BooleanField(label='Malnutrition')

    submit = SubmitField('Submit')

