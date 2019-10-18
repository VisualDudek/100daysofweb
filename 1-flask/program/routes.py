from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# def 100Days() <--- U can not create def name begins from number
@app.route('/100Days')
def p100Days():
    return render_template('100Days.html')