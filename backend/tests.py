import requests


def test_predict():
    '''Testing the predict api with random data'''
    url = "http://127.0.0.1:5000/predict"
    headers = {"Content-Type": "application/json"}
    payload = [5.1, 3.5, 1.4, 0.2]

    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    test_predict()