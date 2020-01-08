import json


def contactadd():
    name = str(input('Type name of your friend: '))
    phonenum = int(input('Type phone number: '))
    contacts = {name: phonenum}
    with open('../proj/contacts.txt', 'w') as file:
        file.write(json.dumps(contacts))


def wordadd():
    word = str(input('Type word that you want to learn: '))
    translate = str(input('Type translate of this word: '))
    vocabulary = {word: translate}
    with open('../proj/vocabulary.txt', 'w+') as file:
        file.write(json.dumps(vocabulary))
