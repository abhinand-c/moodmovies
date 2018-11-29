"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import *
from MoodMoviesWebApp import *
from MoodMoviesWebApp.Mov import *
from MoodMoviesWebApp.mlink import *
from MoodMoviesWebApp.emogen import *
from MoodMoviesWebApp.class1 import *
#from MoodMoviesWebApp.login import *

mood=""
lang=""


@app.route("/", methods=['GET', 'POST'])
def home():
    global mood
    global lang
    if request.method == 'POST':
        mood=request.form['Form1']
        lang=request.form['F2']
        return render_template('Redirect.html', r_url=murl(ea(mood),lang),year=67)
        #return redirect(url_for('red'))
    return render_template(
        'index.html',
        title="Mood Movies",
        year=datetime.now().year,
        message="Charizard"
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact ME???.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='We are legends'
    )

@app.route('/rd',methods=['POST','GET'])
def red():
    global mood
    return render_template('Redirect.html', r_url=murl(ea(mood),lang),year=67)
