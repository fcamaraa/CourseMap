import time


import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/queens_college')
@app.route('/queens_college')
def queens_college_page():
    # Load the JSON data
    with open('Data/courses.json', 'r') as file:
        courses = json.load(file)

    # Pass the courses to the template
    return render_template('queens_college.html', courses=courses)
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