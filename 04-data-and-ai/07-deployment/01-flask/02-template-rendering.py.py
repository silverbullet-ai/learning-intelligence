from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to Flask Templates</h1>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)