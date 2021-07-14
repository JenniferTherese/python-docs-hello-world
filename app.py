
from flask import Flask, request
from flask_restful import Resource, Api



app = Flask(__name__)

@app.route('/home')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
     app.run()



