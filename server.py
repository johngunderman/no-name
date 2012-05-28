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
        return render_template('login.html')
    elif request.method == "POST":
        un = User.query.filter_by(username=request.form['username']).first()
        if not un:
            session['error'] = "Invalid Username!"
            return redirect(url_for('login'))
        else:
            if bcrypt.hashpw(request.form['password'], un.password) == un.password:
                session['user'] = un.id
                return redirect('/')
            else:
                session['error'] = "Invalid Password!"
                return redirect('/login')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'N:COgfe)(*LG#HPSVTHSUCG#RCGNTJQHKWMQBUNC#<RP*CGDJWKHbmjhn'
    database.init_db()
    app.run()
