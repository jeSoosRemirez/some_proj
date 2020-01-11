import json


def contactadd():
    name = str(input('Type name of your friend: '))
    phonenum = int(input('Type phone number: '))
    contacts = {name: phonenum}
    with open('../proj/contacts.txt', 'a') as file:
        file.write(json.dumps(contacts))


def wordadd():
    word = str(input('Type word that you want to learn: '))
    translate = str(input('Type translate of this word: '))
    vocabulary = {word: translate}
    with open('../proj/vocabulary.txt', 'a+') as file:
        file.write(json.dumps(vocabulary))


def recipeadd():
    name = str(input('Type name of cook: '))
    recipe = []
    a = ''
    while a != 'N':
        goods = str(input('Type food that need for cook: '))
        recipe.append(goods)
        a = str(input('Do you wanna continue?(Y or N) ')).upper
        if a == 'Y':
            continue
        else:
            break
    print(f'{name}: {recipe}')


recipeadd()
