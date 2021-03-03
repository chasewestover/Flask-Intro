from flask import Flask
app = Flask(__name__)


def html_template(filler):
    return f"<html><body><h1>{filler}</h1></body></html>"


@app.route('/welcome')
def welcome():
    return html_template("welcome")


@app.route('/welcome/<wel_var>')
def welcome_home(wel_var):
    return html_template(f"welcome {wel_var}")

