import requests

data = {'nombre':'Rubén','edad':20,'salario':1000}

res = requests.post('http://localhost:8000/persona',json=data)
print(res)