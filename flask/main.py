from flask import Flask, render_template
from searchLetters import search4letters, search4vowels

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def mainPage():
    return render_template('entry.html', title='Welcome!!!')

@app.route('/search', methods=['POST'])
def searchLettersIntoPhrase():
    phrase='prueba de concepto'
    letters='aeiou'
#    res=search4letters(phrase, letters)
    res=search4letters(phrase, letters)
#    return render_template('result.html', title='Results!!!', phrase=phrase, letters=letters, result=res)
    return res

app.run()
