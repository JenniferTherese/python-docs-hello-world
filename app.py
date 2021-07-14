
from flask import Flask, request
from flask_restful import Resource, Api

import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub



details = {
    'PhoneNo': [9444415512,9176435819,9003282132],
    'Name' : ['Sam', 'Aishwarya', 'Jen'],
    'Age' : ['1993-10-12', '1993-09-02', '1992-01-01'],
    'City' : ['Chennai', 'Bangalore', 'Delhi']
}
  
# creating a Dataframe object 
df = pd.DataFrame(details, columns = ['PhoneNo','Name', 'Age', 'City'])


def get_info(nos):
    nos = int(nos)
    # name = df.loc[df['PhoneNo'] == nos, 'Name'].item()
    # age = df.loc[df['PhoneNo'] == nos, 'Age'].item()
    # city = df.loc[df['PhoneNo'] == nos, 'City'].item()
    if nos in df.values :
        name = df[df['PhoneNo']==nos]['Name'].values[0]
        age = df[df['PhoneNo']==nos]['Age'].values[0]
        city = df[df['PhoneNo']==nos]['City'].values[0]
        result = [name,age,city]
    else:
        result = "Validation failed"
    return result

app = Flask(__name__)

@app.route('/getinfo/<nos>', methods=['GET'])
def get(nos):
    return {'data': get_info(nos)}


@app.route('/home')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
     app.run()



