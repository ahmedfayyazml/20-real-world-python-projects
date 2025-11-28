from flask import Flask, render_template

import  pandas as pd

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

app.route("/about")
def about():
    return  render_template("about.me")

@app.route("/api/v1/<station>/<date>")
def api_station(station,date):
    temperature = 23
    return {
        "temperature": temperature,
        "station": station,
        "date":date
    }
if __name__ == "__main__":
    app.run(debug=True)
