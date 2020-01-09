from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps, Map
from flask_mail import Mail, Message
import secret

app = Flask(__name__)
GoogleMaps(app)
app.config.update(dict(
    MAIL_SERVER = secret.server,
    MAIL_PORT = secret.port,
    MAIL_USE_TLS = secret.tls,
    MAIL_USE_SSL = secret.ssl,
    MAIL_USERNAME = secret.username,
    MAIL_PASSWORD = secret.password
))

mail = Mail(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/services", methods=["GET"])
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET"])
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

    msg = Message(subject="Customer: " + fname + " " + lname,
                  sender=secret.username,
                  recipients=[secret.rec],
                  body="Customer Name: {0} {1} \nPhone: {2} \nEmail: {3} \nMessage: {4}".format(fname, lname, phone,
                                                                                                email, message))
    mail.send(msg)
    return render_template("contact.html", res=True)


@app.route("/quote", methods=["GET"])
def quote():
    return render_template("quote.html")


@app.route("/quote", methods=["POST"])
def quote_post():
    bname = request.form.get("bname")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    phone = request.form.get("phone")
    email = request.form.get("email")
    address = request.form.get("address")
    address2 = request.form.get("address2")
    city = request.form.get("city")
    postal = request.form.get("postal")
    types = request.form.get("type")
    size = request.form.get("size")
    washroom = request.form.get("washroom")
    cleaning = request.form.get("cleaning")
    time = request.form.get("time")
    info = request.form.get("info")

    msg = Message(
        subject=bname,
        sender=secret.username,
        recipients=[secret.rec],
        body="Business: {0} \nContact: {1} {2} \nPhone: {3} \nEmail: {4} \nAddress: {5} {6} {7} {8} \nType: {9} "
             "\nSize: {10} SqFt \nWashrooms: {11} \nFrequency: {12} \nTime: {13} \nMessage: {14}".format(bname, fname, lname,
                                                                                                    phone, email, address,
                                                                                                    address2, city, postal,
                                                                                                    types, size, washroom,
                                                                                                    cleaning, time, info)
    )
    mail.send(msg)
    return render_template("quote.html", res=True)


if __name__ == '__main__':
    app.run(debug=True)