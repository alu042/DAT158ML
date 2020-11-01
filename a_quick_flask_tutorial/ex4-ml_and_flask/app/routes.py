from app import app
from flask import render_template, session, redirect, url_for
import pickle

from app.forms import DataForm
from app.predict import predict


app.config['SECRET_KEY'] = 'DAT158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    """
    We grab the form defined in `forms.py`. 
    If the form is submitted (and passes the validators) 
    then we grab all the values entered by the user and 
    predict. 
    """

    form = DataForm()
    
    if form.validate_on_submit():

        # If the form is submitted, store all the inputs in session
        for fieldname, value in form.data.items():
            #print(fieldname, value)
            session[fieldname] = value

        # Make predictions and store in session
        pred = predict(session)
        session['pred'] = pred

        return redirect(url_for('index'))

    return render_template('index.html', form=form)



@app.route('/dashboard')

def dashboard():
    return render_template('dashboard.html')
