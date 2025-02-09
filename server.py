from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import time 

app = Flask(__name__)

@app.route('/queens_college')
def queens_college():
    return render_template('queens_college.html')
@app.route('/columbia')
def columbia():
    return render_template('columbia.html')
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    