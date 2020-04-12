import json

phone = {'brand':'Xiaomi', 'model':'Note 10 Pro', 'capaciti':'5260'}



phone_json= json.dumps(phone)
print(type(phone_json), phone_json)

with open('phone_json.txt', 'w') as f:
    json.dump(phone, f)

# load, loads
with open('phone_json.txt') as f:
    data = json.load(f)

print(type(data), data)

