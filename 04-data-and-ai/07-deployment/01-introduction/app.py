from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Flask Framework"


@app.route("/index")
def index():
    return "Welcome to Index Page"


@app.route("/about")
def about():
    return "About Page"


@app.route("/contact")
def contact():
    return "Contact Page"


if __name__ == "__main__":
    app.run(debug=True)