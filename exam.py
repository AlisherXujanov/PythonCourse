import random

exercises = [
    "---Class---",
    '---Files---',
    "---String ms---",
    "---Bool  &  Data-types---",
    "---Functions in depth---",
    "---Set types---",
    "---Sequence types---",
    "---For loop / while---",
    "---Built-in functions---",
    "---Mapping---",
]

names = [
    "Diana", "Manzura", "Shaxrizoda",
    "Artem", "Xayot", "Asli",
    "Zarruh", "Aziz", "Shaxruz", "Istam"
]

already_included = []
result = {}


def get_random_choice(exs):
    if len(already_included) == len(exs):
        return

    choice = random.choice(exs)
    if choice in already_included:
        return get_random_choice(exs)
    else:
        already_included.append(choice)
        return choice


for i in range(len(names)):
    unique_choice = get_random_choice(exercises)
    result[names[i]] = unique_choice


for key, val in result.items():
    print(f'\n {key} - {val}')
