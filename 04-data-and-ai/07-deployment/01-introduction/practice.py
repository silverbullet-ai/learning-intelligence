from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page"


@app.route("/services")
def services():
    return "Services Page"


@app.route("/portfolio")
def portfolio():
    return "Portfolio Page"


@app.route("/contact")
def contact():
    return "Contact Page"


if __name__ == "__main__":
    app.run(debug=True)