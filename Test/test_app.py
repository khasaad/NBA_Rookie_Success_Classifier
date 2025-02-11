import pytest
import json
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

# Test case for the /predict endpoint with valid input
def test_predict_valid_input(client):
    valid_input = [0.5] * 19
    response = client.post('/predict', json=valid_input)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'prediction' in data

# Test case for the /predict endpoint with invalid input (wrong number of features)
def test_predict_invalid_input(client):
    # Invalid input with less than 19 features
    invalid_input = [0.5] * 18
    response = client.post('/predict', json=invalid_input)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

