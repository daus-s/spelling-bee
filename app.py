import os
import sys
import subprocess
import requests
from flask import Flask, render_template, request
import wordmatics as wm
from logger import Logger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    log = Logger()
    # Call the C++ executable with 'entry' as input
    # Process the result and return it
    letters = request.form.get('a')
    letters += request.form.get('b')
    letters += request.form.get('c')
    letters += request.form.get('d')
    letters += request.form.get('e')
    letters += request.form.get('f')
    center = request.form.get('i')
    words_list = []
    #SLOW SLOW SLOW
    for word in wm.word_list:
        f = wm.filter(word, letters, center)
        print(word, end=', ')
        if f:
            words_list += word
    #result is good
    s_words_list = ''
    for word in words_list:
        s_words_list += f'<li>{word}</li>'
    f_words_list = ''
    for word in words_list:
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        response = requests.request("GET", url)
        if response.status_code == 200:
            if wm.pangram(word, letters, center):
                f_words_list +=  f'<li style="font-weight: 650;">{word}</li>'
            else:    
                f_words_list +=  f'<li>{word}</li>'
            log.write(word)
            log.write(", ")
    log.write('\n')
    #print(f_words_list)
    return render_template("index.html", letters="Letters: " + letters, center="Center: " + center, valid_english_list=f_words_list, all_words_list=s_words_list)

if __name__ == '__main__':
    app.run(port=4174, debug=True)