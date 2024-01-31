from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
import pandas as pd
import re
import os 
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

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    if file:
        #Guardamos el archivo en una carpeta local
        filename = file.filename
        file_path = os.path.join('uploads',filename)
        file.save(file_path)

        #Leemos el archivo .dat con pandas
        df = pd.read_csv(file_path, sep='\t')

        #Convertimos el DataFrame a un archivo .xls
        xls_filename = filename.replace('.dat', '.xls')
        xls_file_path = os.path.join('downloads', xls_filename)
        df.to_excel(xls_file_path, index=False)

        #Eliminamos el archivo .dat
        os.remove(file_path)

        #Devolvemos la descarga del archivo xls
        return redirect(url_for('download', filename=xls_filename))
    
@app.route('/download/<filename>')
def download(filename):
    downloads_folder = 'downloads'
    return redirect(url_for('static', filename=os.path.join(downloads_folder, filename)),code=301)

if __name__ == '__main__':

    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    app.run(host='0.0.0.0', port = 4000, debug = True)