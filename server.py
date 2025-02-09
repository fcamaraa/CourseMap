from flask import Flask, render_template

app = Flask(__name__)

# Route for Queens College Page
@app.route('/queens_college')
def queens_college_page():
    return render_template('queens_college.html')

# Route for Columbia Page
@app.route('/columbia')
def history_page():
    return render_template('columbia.html')

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

