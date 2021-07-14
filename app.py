import getinfo
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)




class Information(Resource):
    def get(self, nos):
        return {'data': getinfo.get_info(nos)}

api.add_resource(Information, '/getinfo/<nos>')

if __name__ == '__main__':
     app.run()
