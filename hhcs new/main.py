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
    # if (gender == 'male'):
    #     gender=0
    # else:
    #     gender=1
    age = request.form['age']
    sbp = request.form['sbp']
    hbp = request.form['hbp']
    spo2 = request.form['spo2']
    temp = request.form['temp']
    h_rate = request.form['h_rate']
    glc = request.form['glc']
    res = predict(gender,age, sbp, hbp, h_rate, glc, spo2, temp)
    # print(gender)
    # print(spo2)
    # print(sbp)
    # print(hbp)
    # print(h_rate)
    # print(glc)
    if (res[0] == 1):
        res = "healthy"
    elif(res[0] == 2):
        res = "High BP"
    elif(res[0] == 3):
        res = "LOW BP"
    elif(res[0] == 4):
        res = "High Sugar"
    elif(res[0] == 5):
        res = "Low Sugar"
    elif(res[0] == 6):
        res = "Low Oxygen"
    elif(res[0] == 7):
        res = "High Temperature"
    elif(res[0] == 8):
        res = "Heartbeat is High"
    elif(res[0] == 9):
        res = "Risk"
    

    return render_template('forms.html', res = res)

@app.route('/forms', methods=['POST', 'GET'])
def form():
    return render_template('forms.html')

@app.route('/tips', methods=['POST', 'GET'])
def tips():
    return render_template('tips.html')

@app.route('/posts', methods=['POST', 'GET'])
def posts():
    return render_template('post.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

@app.route('/recommendations', methods=['POST', 'GET'])
def recommend():
    return render_template('recommendations.html')

@app.route('/faqs', methods=['POST', 'GET'])
def faqs():
    return render_template('faq.html')

@app.route('/login', methods=['POST', 'GET'])
def logi():
    return render_template('login.html')

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