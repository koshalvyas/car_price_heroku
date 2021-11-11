import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':2, 'kms':9, 'test_score':6})

print(r.json())