from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('Homepage1.html')


@app.route('/login')
def login():
    return render_template('Login.html')


if __name__ == '__main__':
    app.run()
