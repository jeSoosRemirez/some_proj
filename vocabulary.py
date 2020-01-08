import json


def wordadd():
    word = str(input('Type word that you want to learn: '))
    translate = str(input('Type translate of this word: '))
    vocabulary = {word: translate}
    with open('../proj/vocabulary.txt', 'w') as file:
        file.write(json.dumps(vocabulary))


wordadd()
