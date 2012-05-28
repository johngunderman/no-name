import database
from models import User, Story

from flask import Flask, url_for, request, session, redirect, render_template
import bcrypt


app = Flask(__name__)


@app.route('/')
@app.route('/top')
def top_stories():
    stories = Story.query.all()
    return render_template('stories.html', page_name="Top Stories", stories=stories)

@app.route('/new')
def new_stories():
    stories = Story.query.all()
    return render_template('stories.html', page_name="New Stories", stories=stories)

def hello_world():
    if 'user' in session:
        return 'Youre user: #' + str(session['user'])
    else:
        return 'Hello world! <a href="/login">Log In?</a>'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        # MAKE ME A TEMPLATEEEEEEE
        return """<form method='POST'>
                <b>Username:</b> <input type='text' name='username' /><br>
                <b>Password:</b> <input type='password' name='password' /><br>
                <input type='submit' />
                </form>"""
    elif request.method == "POST":
        un = User.query.filter_by(username=request.form['username']).first()
        if not un:
            session['error'] = "Invalid Username!"
            return redirect(url_for('login'))
        else:
            if bcrypt.hashpw(request.form['password'], un.password) == un.password:
                session['user'] = un.id
                return redirect(url_for('hello_world'))
            else:
                session['error'] = "Invalid Password!"
                return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'N:COgfe)(*LG#HPSVTHSUCG#RCGNTJQHKWMQBUNC#<RP*CGDJWKHbmjhn'
    database.init_db()
    app.run()
