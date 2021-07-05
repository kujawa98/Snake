from random import choice


def generate_food(free_spots):
    filtered = filter(lambda x: x[2] == True, free_spots)
    return choice(list(filtered))
