#!/usr/bin/env python


def scores(after):
    recipes = [3, 7]
    current = [0, 1]
    while len(recipes) < after + 10:
        recipes_sum = sum(recipes[c] for c in current)
        newrecipes = [int(i) for i in str(recipes_sum)]
        recipes.extend(newrecipes)
        current = tuple(
            map(lambda c: (c + recipes[c]+1) % len(recipes), current))
    return ''.join(map(str, recipes[after:after + 10]))


assert scores(9) == '5158916779'
assert scores(5) == '0124515891'
assert scores(18) == '9251071085'
assert scores(2018) == '5941429882'
print(scores(30121))
