import json


def contactadd(self):
    name = str(input('Type name of your friend: '))
    phonenum = int(input('Type phone number: '))
    contacts = {name: phonenum}
    with open('../proj/contacts.txt', 'w') as file:
        file.write(json.dumps(contacts))


contactadd(self=1)
