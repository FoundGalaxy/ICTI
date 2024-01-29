from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
import pandas as pd

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/conversor.html')
def conversor():
    return render_template('conversor.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug = True)
