import requests


url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()

#print(data)

for i in data:
    print(f"ID:{i['id']}")
    print(f"Product Name:{i['title']}")
    print(f"Product Price:{i['price']}")