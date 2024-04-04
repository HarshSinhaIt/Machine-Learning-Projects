from flask import Flask , render_template, request
import pickle

app= Flask(__name__)

#load the model

model = pickle.load(open('model_KN.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods= ['POST', 'GET'])
def predict():
    SepalLengthCm = float(request.form['SepalLengthCm'])
    SepalWidthCm = float(request.form['SepalWidthCm'])
    PetalLengthCm = float(request.form['PetalLengthCm'])
    PetalWidthCm = float(request.form['PetalWidthCm'])
    result = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug= True)