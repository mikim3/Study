
from flask import Flask, render_template, request, Response, session, flash, redirect, url_for

HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')  # 접속하는 url
def index():
    return render_template('index.html')

@app.route('/index2')  
def index2():
    return render_template('index2.html')
@app.route('/index3')  
def index3():
    return render_template('index3.html')
@app.route('/index4')  
def index4():
    return render_template('index4.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8080, debug=True)
