
from flask import Flask, render_template, request,redirect
from werkzeug.utils import secure_filename
from wtforms import FileField
import pandas
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, RNN, Dense, LSTM, Bidirectional, SimpleRNN
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
import os
from flask_wtf.csrf import CSRFProtect
import csv
import requests

path = os.getcwd()

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config['SECRET_KEY'] = "secretkey"
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def upload_file():
    return render_template('index.html')


@app.route("/display",methods=['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        print(filename)

        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        print("hhh",app.config['UPLOAD_FOLDER']+"/"+filename)
        # file = open(os.path.join(app.config['UPLOAD_FOLDER'],filename),"r")
        content = pandas.read_csv(app.config['UPLOAD_FOLDER']+"/"+filename, encoding = "ISO-8859-1", engine='c')


        with requests.Session() as s:
            s.get(app.config['UPLOAD_FOLDER']+"/"+filename)

    return render_template('content.html')



    

if __name__ == "__main__":
    app.run(debug=True)