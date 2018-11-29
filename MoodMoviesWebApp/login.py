from MoodMoviesWebApp.class1 import *
from MoodMoviesWebApp.views import *
from datetime import datetime

u={}
x=""
users={}
def login23():
    global x
    if request.method == 'POST':
        x=request.form['UID'] 
        u[x].user_id(x)
        u[x].pcode(request.form['Pass'])
        return redirect(url_for('home'))
    return render_template('login.html',title="Login",year=datetime.now().year,message="Pikachu")


def retnam(x):
      return u[x].uid()


@app.route('/login', methods=['GET', 'POST'])
def login():
	global mood,lang,users
	if user.cuser!="PIKACHU" :
		return redirect(url_for('home'))
	if request.method == 'POST':
		ID=request.form['UID']
		passcode=request.form['Pass']
		if(ID in users):
			user.cuser=ID
			return redirect(url_for('home'))
		else:
			return render_template('login.html',title="Login",year=datetime.now().year,msg="Invalid Credentials")
	return render_template('login.html',title="Login",year=datetime.now().year)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	global mood,lang,users
	user.cuser="PIKACHU"
	return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	global mood,lang,users
	user.cuser="PIKACHU"
	if request.method == 'POST':
		x=request.form['UID']
		users[x]=user()
		users[x].user_id(x)
		users[x].pcode(request.form['Pass'])
		return redirect(url_for('home'))
	return render_template('signup.html',title="Signin",year=datetime.now().year,message="Pikachu")