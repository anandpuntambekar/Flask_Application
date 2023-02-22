# Loan Application Approval Prediction Flask API

Blog - https://medium.com/@anpuntam/deploying-a-loan-approval-machine-learning-system-api-using-flask-820679e6d2dc
https://medium.com/@anpuntam/streamlining-development-and-deployment-with-continuous-integration-and-continuous-delivery-be7883391b21

This is a Flask API that takes loan application information as input and returns the loan approval status using a machine learning model. The API is built using Python and uses the Flask web framework.

## Requirements
- Python 3.x
- Flask
- Pickle

## Installation
- Clone the repository to your local machine.
- Install the required packages using pip:

```
pip install Flask
pip install pickle

```
Navigate to the project directory in your terminal.
- Run the API by executing the following command:
 ```
 flask run
```
## Usage
The API has two endpoints:

- /ping: Returns a message confirming that the API is working.
- /predict: Accepts loan application information in JSON format and returns the loan approval status.  
The expected keys in the JSON payload are:

- Gender: Gender of the loan applicant (Male/Female).
- Married: Marital status of the loan applicant (Married/Unmarried).
- Credit_History: Credit history of the loan applicant (Clear Debts/Unclear Debts).
- ApplicantIncome: Income of the loan applicant.
- LoanAmount: Loan amount requested by the loan applicant.

Example
Here's an example of how you can use the API to make a prediction:

```
import requests

url = "http://localhost:5000/predict"

payload = {"Gender": "Male",
           "Married": "Married",
           "Credit_History": "Clear Debts",
           "ApplicantIncome": 5000,
           "LoanAmount": 100000}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

The response should be a JSON object with the loan approval status:

```

{
    "loan_approval_status": "Approved"
}
```


Here are Snapshots of results when we use Postman
![alt text](https://github.com/anandpuntambekar/Flask_Application/blob/main/image_approve_loan.png)


![alt text](https://github.com/anandpuntambekar/Flask_Application/blob/main/image_reject_loan.png)

