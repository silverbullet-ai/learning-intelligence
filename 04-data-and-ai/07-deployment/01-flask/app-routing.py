from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("student-form.html")


@app.route("/submit", methods=["POST"])
def submit():

    science = int(request.form["science"])
    maths = int(request.form["maths"])
    python = int(request.form["python"])
    ai = int(request.form["ai"])

    average = (science + maths + python + ai) / 4

    return redirect(
        url_for(
            "result",
            score=int(average)
        )
    )


@app.route("/result/<int:score>")
def result(score):

    status = "Pass" if score >= 50 else "Fail"

    return render_template(
        "result.html",
        score=score,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)