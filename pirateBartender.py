import random

def bartender():
    questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
    }

    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }

    names = {
        "adjectives": ["Wild", "Cool", "Sizzlin", "Smooth", "Tangy"],
        "nouns": ["Snake", "Orange", "Ringer", "Moose", "Cat"],
    }

    answers = []
    for question in questions:
        user_answer = input(questions[question])
        if user_answer == "yes" or user_answer == "y":
            answers.append(random.choice(ingredients[question]))
    print("Here ya go! This is called the {} {}".format(random.choice(names["adjectives"]), random.choice(names["nouns"])))
    print("These are the ingredients {}".format(answers))

    repeat = input("Do you want another?")
    if repeat == "yes" or repeat == "y":
        bartender()


if __name__ == '__main__':
    bartender()