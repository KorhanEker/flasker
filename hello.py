from flask import Flask, render_template


# create a flask instance
app = Flask(__name__)


# create a route decorator
@app.route('/simpleline')
def simpleline():
    return "<h1>Hello World!</h1>"


# create a route decorator
@app.route('/')
def index():
    stuff = "This is <strong>Bold</strong> text."
    my_list = ['Pepperoni', 'Cheese', 'Mushroom', 41]
    return render_template("index.html", stuff=stuff, list=my_list)


# localhost:5000/user/john
@app.route('/user/<username>')
def user(username):
    # return f"<h1>Hello {username}.</h1>"
    return render_template("user.html", name=username)


# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)

