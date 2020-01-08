from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)
GoogleMaps(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/services", methods=["GET"])
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # mymap = Map(
    #     identifier="view-side",
    #     lat=37.4419,
    #     lng=122.1419,
    #     markers=[(37.4419,-122.1419)]
    # )
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def contact_post():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    phone = request.form.get("phone")
    email = request.form.get("email")
    message = request.form.get("message")

    print(fname)
    print(lname)
    print(phone)
    print(email)
    print(message)

    return redirect(url_for("contact"))
    # return render_template("contact.html")


@app.route("/quote", methods=["GET"])
def quote():
    return render_template("quote.html")


if __name__ == '__main__':
    app.run(debug=True)