from MoodMoviesWebApp.class1 import *

u={}
x=""
@app.route('/login', methods=['GET', 'POST'])
def login():
    global x
    if request.method == 'POST':
        x=request.form['UID'] 
        u[x].user_id(x)
        u[x].pcode(request.form['Pass'])
        return redirect(url_for('home'))
    return render_template('login.html',title="Login",year=datetime.now().year,message="Pikachu")


def retnam():
      return u[x].uid()
