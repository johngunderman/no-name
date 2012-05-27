from flask import Flask, url_for, request, session, redirect, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(40))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User {0}>".format(self.username)

@app.route('/')
@app.route('/top')
def top_stories():
    return render_template('stories.html', page_name="Top Stories")

@app.route('/new')
def new_stories():
    return render_template('stories.html', page_name="New Stories")

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
    app.run()
