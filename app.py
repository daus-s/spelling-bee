import os
import sys
import subprocess
import requests
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print('hello form')
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

    print(f'{letters} {center}')
    cmd=f'./main.out {letters} {center} 1'
    cpp_output = subprocess.check_output(cmd, shell=True)[:-2]
    #result is good
    words_list = cpp_output.decode('utf-8').split(', ')
    f_words_list = []
    for word in words_list:
        print(f'word: {word}')            
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        print(url)
        response = requests.request("GET", url)
        print(response)
           

    print(words_list)
    print(f_words_list)


    return render_template_string("output.html", letters=letters, center=center, words=words_list, f_words=words_list)

if __name__ == '__main__':
    app.run(debug=True)