import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model_pickle = open ("./artefacts/classifier.pkl","rb")
clf = pickle.load(model_pickle)
# mapping the URL to the function is done via a decorator
# decorators are a python concept they allow you to build on the type of functin you have
# https://yourwebsite.com/ping

@app.route("/ping",methods=['GET'])
def ping():
  return {"message":"Hi there I am working"}


## define the end point which will make the prediction
## The URL and fuction need not be same

## request give us function which is called Get Json
## gender , married credit history, will come from Json

@app.route("/predict",methods=["POST"])
def prediction():
  """
  Returns loan application status using ML model
  """

  loan_req = request.get_json()
  print(loan_req) 

  if loan_req['Gender'] == "Male":
        Gender = 0
  else:
        Gender = 1
 
  if loan_req['Married'] == "Unmarried":
        Married = 0
  else:
        Married = 1
 
  if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
  else:
        Credit_History = 1  
    
  ApplicantIncome = loan_req['ApplicantIncome']
  LoanAmount = loan_req['LoanAmount'] / 1000
 
    # Making predictions 
  prediction = clf.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
  if prediction == 0:
        pred = 'Rejected'
  else:
        pred = 'Approved'

  result = {
        'loan_approval_status': pred
    }

  return jsonify(result)
  
