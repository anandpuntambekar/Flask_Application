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

def test_predict(client):
    test_data = {"Gender":"Male", "Married":"Unmarried",
    'Credit_History' : "Unclear Debts",
    'ApplicantIncome':100000,'LoanAmount':2000000}
    response =client.post("/predict",json = test_data)
    assert response.status_code==200
    assert response.json=={
        'loan_approval_status': 'Rejected'
            }


