from flask import Flask, render_template, request
import wordmatics as wm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Call the C++ executable with 'entry' as input
    # Process the result and return it
    letters = request.form.get('a')
    letters += request.form.get('b')
    letters += request.form.get('c')
    letters += request.form.get('d')
    letters += request.form.get('e')
    letters += request.form.get('f')
    center = request.form.get('i')
    s_words_list = ''
    f_words_list = ''
    #SLOW SLOW SLOW
    all =  wm.all_words_list()
    val = wm.valid_words_list()
    for word in all:
        f = wm.filter(word, letters, center)
        if f:
            s_words_list += f'<li>{word}</li>'
    for word in val:
        if wm.pangram(word, letters, center) and wm.filter(word, letters, center):
            f_words_list +=  f'<li style="font-weight: 650;">{word}</li>'
        else:    
            if wm.filter(word, letters, center):
                f_words_list +=  f'<li>{word}</li>'
    #result is good

    return render_template("index.html", letters="Letters: " + letters, center="Center: " + center, valid_english_list=f_words_list, all_words_list=s_words_list)

if __name__ == '__main__':
    app.run(port=4174, debug=True)