from flask import Flask, render_template, request, escape
from searchLetters import search4letters, search4vowels

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def mainPage():
    return render_template('entry.html', title='Welcome!!!')

@app.route('/search', methods=['POST'])
def search_letters_into_phrase():
    phrase=request.form['phrase']
    letters=request.form['letters']
    res=search4letters(phrase, letters)
    log_request(request, res)        
    return render_template('result.html', title='Results!!!', phrase=phrase, letters=letters, result=res)

@app.route('/log')
def get_log():
    with open('log.txt') as log:
        res=log.read()

    return escape(res)
    
def log_request(req, res):
    with open('log.txt', 'a') as log:
        log.write(str(req.form))
        log.write(str(req.remote_addr))
        log.write(str(req.user_agent))
        log.write(str(res))
        log.write('\n')

if __name__=='__main__':
    app.run(debug=True)


