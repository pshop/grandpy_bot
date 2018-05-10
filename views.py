from flask import Flask, request, render_template
from my_classes import ClassParser

app = Flask(__name__)

@app.route('/')
def grandpy_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def grandpy_form_post():
    question = request.form['question']
    p = ClassParser.Parser(question)
    
    return p.parsed_string