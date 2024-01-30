from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
import pandas as pd
import re
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/conversor.html')
def conversor():
    return render_template('conversor.html')

@app.route('/asistencias.html')
def asistencias():
    return render_template('asistencias.html')

@app.route('/registros.html')
def registros():
    return render_template('registros.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug = True)