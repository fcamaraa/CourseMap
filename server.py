
import time


import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/queens_college')
def index():
    return render_template('queens_college.html')
@app.route('/columbia')
def history_page():
    return render_template('columbia.html')
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()