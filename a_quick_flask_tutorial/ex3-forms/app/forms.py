from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    name = StringField("What's your name?", validators=[DataRequired()])
    gender = IntegerField('Gender? 0=Male, 1=Female', validators=[NumberRange(min=0, max=1)])

    stillfollowing = BooleanField(label='Still following along?')

    submit = SubmitField('Submit')

