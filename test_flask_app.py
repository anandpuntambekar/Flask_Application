import pytest
import json
from app import app
import json
# app = Flask(__name__)


@pytest.fixture
def client ():
    return app.test_client()

# using this client ww will abe to get and post request , etc and these will help us simulate all the end points

def test_ping(client):
    # ping end point acepts get request and sends message for you.
    resp =client.get('/ping')
    assert resp.status_code==200
    assert resp.json== {"message":"Hi there I am working"}



'''

def test_ping():
    
    ##We first need to run a server and get get the output
    ##falsk offers a test
    ##When we run flask app in terminal we dont have to run fasl every time we reun flask server
    ##In the test a
    
    client = app.test_client()
    url = '/ping'
    response = client.get(url)
    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'Hi there I am working'}

def test_prediction_approved():
    client = app.test_client()
    url = '/predict'
    data = {
        'Gender': 'Male',
        'Married': 'Yes',
        'Credit_History': 'Unclear Debts',
        'ApplicantIncome': 5000,
        'LoanAmount': 200
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'loan_approval_status': 'Rejected'}

def test_prediction_rejected():
    client = app.test_client()
    url = '/predict'
    data = {
        'Gender': 'Female',
        'Married': 'No',
        'Credit_History': 'Unclear Debts',
        'ApplicantIncome': 1000,
        'LoanAmount': 50
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'loan_approval_status': 'Rejected'}
'''