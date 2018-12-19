#!/usr/bin/env python3


def scores(target):
    target = list(map(int, target))
    recipes = [3, 7]
    current = (0,1)

    while True:
        recipes_sum = sum(recipes[c] for c in current)
        new_recipes = list(map(int, str(recipes_sum)))
        for new_recipet in new_recipes:
            recipes.append(new_recipet)
            if target == recipes[-len(target):]:
                return len(recipes) - len(target)
        current  = tuple((c + recipes[c]+1) % len(recipes) for c in current)

        

assert scores('01245') == 5
assert scores('51589') == 9
assert scores('92510') == 18
assert scores('59414') == 2018
print('Tests passed')
print(scores('030121'))
