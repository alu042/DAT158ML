from app import app
from flask import render_template, session

# Necessary for passing the session
app.config['SECRET_KEY'] = 'DAT158'



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    """
    Display the index.html template passing the value of `name` in the 
    current session.
    """

    session['name'] = "[NAME satt i back-end]"

    return render_template('index.html')

