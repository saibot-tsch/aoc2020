"""Day 21: Allergen Assessment"""

from operator import itemgetter
from itertools import permutations


def find_possible_ingredients(foods):
    """returns lookup {allergene: {ingredients}}"""
    candidates = {}
    for ingredients, allergenes in foods:
        for a in allergenes:
            if not candidates.get(a):
                candidates[a] = set(ingredients)
            candidates[a] = candidates[a] & set(ingredients)
    return candidates


def combine(sets):
    """returns the union of given sets"""
    return sets[0].union(*sets[1:])


def find_dangerous_ingredients(foods):
    """returns a set of ingredients that have allergenes"""
    candidates = find_possible_ingredients(foods)
    return combine(list(candidates.values()))


def count_ingredients_without_allergenes(foods):
    """returns number of ingredients that cannot contain known allergenes"""
    dangerous_ingredients = find_dangerous_ingredients(foods)
    return sum([ing not in dangerous_ingredients
                for ingredients, _ in foods for ing in ingredients])


def find_allergene_assignment(foods):
    """returns list of [(allergene, ingredient)]"""
    candidates = find_possible_ingredients(foods)
    ingredients = list(find_dangerous_ingredients(foods))

    for assignment in permutations(ingredients, r=len(ingredients)):
        if all(ing in candidates[a] for a, ing in zip(candidates, assignment)):
            return zip(candidates, assignment)


def get_dangerous_ingredients(foods):
    """returns list of ingredients"""
    assignment = find_allergene_assignment(foods)
    return ','.join([i for a, i in sorted(assignment, key=itemgetter(0))])


if __name__ == '__main__':
    with open('input.txt') as f:
        foods = [[part.replace(',', '').split(' ')
                  for part in line[:-2].split(' (contains ')] for line in f]

    print('part 1:', count_ingredients_without_allergenes(foods))
    print('part 2:', get_dangerous_ingredients(foods))
