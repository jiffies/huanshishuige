#-*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return u'这里是还施水阁'

if __name__ == '__main__':
    app.run()
