import os
import sys
import subprocess
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Call the C++ executable with 'entry' as input
    # Process the result and return it
    data = []
    letters = request.form.get('a')
    letters += request.form.get('b')
    letters += request.form.get('c')
    letters += request.form.get('d')
    letters += request.form.get('e')
    letters += request.form.get('f')
    data.append(letters)
    center = request.form.get('i')
    data.append(center)

    cmd=f'./main.out {letters} {center} 1'
    cpp_output = subprocess.check_output(cmd, shell=True)[:-2]
    #result is good
    words_list = cpp_output.decode('utf-8').split(', ')
    s_words_list = ''
    for word in words_list:
        s_words_list += f'<li>{word}</li>'
    f_words_list = ''
    for word in words_list:
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        response = requests.request("GET", url)
        if response.status_code == 200:
            f_words_list +=  f'<li>{word}</li>'

    
    return render_template("index.html", letters=letters, center=center, valid_english_list=f_words_list, all_words_list=s_words_list)

if __name__ == '__main__':
    app.run(debug=True)