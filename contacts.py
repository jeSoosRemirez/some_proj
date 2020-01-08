import json


number = {'Andrew': 38063}

with open('../proj/contacts.txt', 'w') as file:
    file.write(json.dumps(number))
