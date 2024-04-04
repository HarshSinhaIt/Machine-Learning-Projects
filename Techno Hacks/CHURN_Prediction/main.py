
from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
import pickle
import numpy as np

app= Flask(__name__)

@app.route("/")
def LoadPage():
    return render_template('home.html', query= "")