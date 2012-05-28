import database
from database import db_session
from models import User, Story, Vote

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

@app.route('/show/')
@app.route('/show/<id>')
def show_story(id=None):
    if id is None:
        return render_template('not_found.html', page_name="404"), 404
    story = Story.query.get(id)
    if story == None:
        return render_template('not_found.html', page_name="404"), 404
    return render_template('show.html', page_name=story.title, story=story)

@app.route('/user/')
@app.route('/user/<id>')
def show_user(id=None):
    if id is None:
        return render_template('not_found.html', page_name="404"), 404
    user = User.query.get(id)
    if user == None:
        return render_template('not_found.html', page_name="404"), 404
    return render_template('user.html', page_name=user.username, user=user)

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

@app.route('/logout')
def logout():
    del session['user']
    return redirect('/')

@app.route('/vote/<id>/<direction>')
def vote(id, direction):
    if 'user' not in session:
        return redirect('/login')
    v = (Vote.query.filter_by(user_id=session['user'], story_id=id).first() or Vote(session['user'],id,direction))
    db_session.add(v)
    db_session.commit()
    return redirect(url_for('top_stories'))

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'N:COgfe)(*LG#HPSVTHSUCG#RCGNTJQHKWMQBUNC#<RP*CGDJWKHbmjhn'
    database.init_db()
    app.run()
