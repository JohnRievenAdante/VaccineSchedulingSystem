from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main_homepage():
    return render_template("home.html")

@app.route('/otherpage', methods = ['POST'])
def otherpage():
    return render_template("otherpage.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)