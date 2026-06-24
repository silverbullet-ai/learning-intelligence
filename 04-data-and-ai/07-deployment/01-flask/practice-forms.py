from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    if request.method == "POST":

        username = request.form["username"]

        return f"Feedback received from {username}"

    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)