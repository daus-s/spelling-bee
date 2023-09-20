import os
import sys
import subprocess
from os.path import exists
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Call the C++ executable with 'entry' as input
    # Process the result and return it
    letters = request.form['a']
    letters += request.form['b']
    letters += request.form['c']
    letters = request.form['d']
    letters += request.form['e']
    letters += request.form['f']

    center = request.form['i']
    cmd=f'./main.out {letters} {center} 1'
    result = subprocess.check_output(cmd, shell=True)
    print(result)
    return "Result from C++: ..."

if __name__ == '__main__':
    app.run(debug=True)