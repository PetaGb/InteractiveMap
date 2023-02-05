from flask import Flask, render_template

from map import map_fig

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("map_template.html", fig=map_fig())

if __name__ == "__main__":
    app.run(debug=True)