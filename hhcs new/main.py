from flask import Flask, render_template, request
import requests
import pickle
from sklearn.preprocessing import StandardScaler

import pandas as pd

app = Flask(__name__)


mdl = pickle.load(open('model_svc.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def forms():
    gender = request.form['gender']
    age = request.form['age']
    sbp = request.form['SBP']
    hbp = request.form['HBP']
    spo2 = request.form['spo2']
    temp = request.form['temp']
    h_rate = request.form['h_rate']
    glc = request.form['glc']
    res = predict(gender,age, sbp, hbp, h_rate, glc, spo2, temp)
    print(res)
    return render_template('forms.html')

@app.route('/forms', methods=['POST', 'GET'])
def form():
    return render_template('forms.html')


def predict(g,a,s,h,hr,gl,sp,temp):
    p = [[g,a,s,h,hr,gl,sp,temp],
        [g,a,s,h,hr,gl,sp,temp]]
    pickled_model = pickle.load(open('model_svc.pkl', 'rb'))
        # pickled_model.predict(model.sen())

    scaler = StandardScaler()

    p = pd.DataFrame(scaler.fit_transform(p))

    return(pickled_model.predict(p))

if __name__ == '__main__':
    app.run(debug=True)