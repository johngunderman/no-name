from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def top_stories():
    return render_template('stories.html', page_name="Top Stories")

@app.route('/new')
def new_stories():
    return render_template('stories.html', page_name="New Stories")


if __name__ == '__main__':
    app.run()

