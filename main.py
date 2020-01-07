from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)
GoogleMaps(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/services", methods=["GET"])
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET"])
def contact():
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=122.1419,
        markers=[(37.4419,-122.1419)]
    )

    return render_template("contact.html", mymap=mymap)


if __name__ == '__main__':
    app.run(debug=True)