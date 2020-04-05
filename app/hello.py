from flask import Flask, url_for, request
from flask import render_template
from re import escape

app = Flask(__name__)
print(app)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about', methods=["GET", "POST"])
def about():
    if request.method == "POST":
        return "This is about POST"
    elif request.method == "GET":
        return 'This is about GET'


@app.route('/result/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks=score)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run()
