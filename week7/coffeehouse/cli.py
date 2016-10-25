import requests

json_result = requests.get("http://localhost:8000/specials").json()
print(json_result)

for special in json_result:
    print(special["name"])
    print(special["price"])
    print(special["description"])
    print("*" * 80)
