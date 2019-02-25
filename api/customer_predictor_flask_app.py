#create flask_app file
import json
import os
from flask import Flask,jsonify,request
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)
@app.route("/cuspredict/",methods=['GET','POST'])
def predict():
    creditscore = float(request.args.get('creditscore'))
    geography = request.args.get('geography')
    gender = request.args.get('gender')
    age = float(request.args.get('age'))
    tenure = float(request.args.get('tenure'))
    balance = float(request.args.get('balance'))
    hascrcard = float(request.args.get('hascrcard'))
    isactivemember = float(request.args.get('isactivemember'))
    estimatedsalary = float(request.args.get('estimatedsalary'))
    
    #return creditscore+" "+geography+" "+gender+" "+age+" "+tenure+" "+balance+" "+hascrcard+" "+isactivemember+" "+isactivemember
    

    
    if gender=='male':
        gender=1
    else:
        gender=0
        
    if geography=='Germany':
        geography_1=1
        geography_2=0
        geography_3=0
    elif geography=='Spain':
        geography_1=0
        geography_2=1
        geography_3=0
    else:
        geography_1=0
        geography_2=0
        geography_3=1
        
        
    with open('customer_predictor_model.pkl', 'rb') as handle:
        model = pickle.load(handle)
    
    status = model.predict(np.array([[creditscore, geography_1,geography_2,geography_3, gender,age,tenure,balance,hascrcard,isactivemember,estimatedsalary]]))
    
    return str(status[0])

@app.route("/",methods=['GET'])
def default():
    return "<h1> Welcome to customer predictor model <h1>"
 

if __name__ == "__main__":
    app.run() 
