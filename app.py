from flask import Flask, request, render_template

from Utility.translator_utility import translator
from database.db_operation import get_BegineerLevelInfo
from model.BeginnerList import BeginnerList


app = Flask(__name__)


@app.route('/')
def showchatbot():  # put application's code here
    return render_template('chatbot.html')

@app.route('/translate', methods=['POST'])
def translate():
    body = request.get_json()
    sentence = body.get('sentence')
    language = body.get('language')
    t = translator(language, sentence)
    response = t.translate()
    return response

@app.route('/signUp', methods=['POST'])
def addUser():
    pass

@app.route('/beginnerlevel', methods=['Get'])
def getBegginerLevelDetails():
    lst = BeginnerList(get_BegineerLevelInfo());
    return  lst.toJSON()


if __name__ == '__main__':
    app.run()
