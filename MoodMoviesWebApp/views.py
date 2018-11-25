"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import *
from MoodMoviesWebApp import *
from MoodMoviesWebApp.Mov import *
from MoodMoviesWebApp.mlink import *

mood="ERROR"
def mg(a):
    s="Drama"
    x=a.lower()
    if(x=="happy"):
        s="Comedy"
    elif(x=="sad"): 
        s="Drama"
    else:
        s="Drama"
    return s

@app.route("/", methods=['GET', 'POST'])
def home():
    global mood
    if request.method == 'POST':
        mood=request.form['Form1']
        return redirect(url_for('red'))
    return render_template(
        'index.html',
        title="Mood Movies",
        year=datetime.now().year,
        message="Welcome"
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
    return render_template('Redirect.html', r_url=murl(mood),year=67)