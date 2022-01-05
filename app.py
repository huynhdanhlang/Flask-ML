
from flask import Flask, render_template, request,send_file
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
import pandas
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os
from flask_wtf.csrf import CSRFProtect
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

@app.route('/api/downloadfile/<filename>', methods=['GET',"POST"])
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'],filename),as_attachment=True,download_name=filename)

@app.route("/display",methods=['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        print("hhh",app.config['UPLOAD_FOLDER']+"\\"+filename)
        # file = open(os.path.join(app.config['UPLOAD_FOLDER'],filename),"r")
        # content = pandas.read_csv(app.config['UPLOAD_FOLDER']+"\\"+filename, encoding = "ISO-8859-1", engine='c')
        
        # with requests.Session() as s:
        #     s.get('https://112b-8-21-11-129.ngrok.io/api/downloadfile'+'/'+filename)
    # return redirect('https://112b-8-21-11-129.ngrok.io/api/downloadfile'+'/'+'uploads'+'/'+filename)
        
    return render_template('content.html',filename=filename)
        





if __name__ == "__main__":
    app.run(debug=True)