from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/<string:name>")
def hello(name):
    return render_template("hello.html", name=name.capitalize())

@app.route("/friday")
def friday():
    today = datetime.datetime.now()
    day = today.weekday()

    if day == 4:
        text= 'But I work on Saturdays -_-.'
        return render_template("friday.html", result="YES, Its Friday :)", text= text)
    else:
        text= 'Still Gotta Work Tomorrow!!'
        return render_template("friday.html", result="NOPE, Its not NOT :(", text= text)


if __name__ == '__main__':
    app.run(debug=True)