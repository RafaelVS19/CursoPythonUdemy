import json

with open('abc.json', 'r') as file2:
    d1_json = file2.read()
    d1_json = json.loads(d1_json) # transforma de json em dicionário

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)