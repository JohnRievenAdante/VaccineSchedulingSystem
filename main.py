from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route ("/")

def Home():
    return render_template("Home.html", content="Test")

@app.route ("/ScheduleAppointment")

def ScheduleAppointment():
    return render_template("ScheduleAppointment.html", content="Test")

@app.route ("/ViewAppointment")

def ViewAppointment():
    return render_template("ViewAppointment.html", content="Test")

@app.route ("/Login")

def Login():
    return render_template("Login.html", content="Test")

@app.route ("/Register")

def Register():
    return render_template("Register.html", content="Test")

if __name__ == "__main__":
    app.run(debug=True)