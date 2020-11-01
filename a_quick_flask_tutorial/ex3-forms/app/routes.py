from app import app
from flask import render_template, session, redirect, url_for
from app.forms import DataForm



# Necessary for WTForms
app.config['SECRET_KEY'] = 'DAT158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])


def index():

    """
    We grab the form defined in `forms.py`. 
    If the form is submitted (and passes the validators) 
    then we grab all the values entered by the user and 
    display them. 
    """

    form = DataForm()
    
    if form.validate_on_submit():

        # If the form is submitted then store all the inputs in session
        for fieldname, value in form.data.items():
            session[fieldname] = value
        return redirect(url_for('index'))

    return render_template('index.html', form=form)