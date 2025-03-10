spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # foods = []
    # for spicy_food in spicy_foods:
    #     foods.append(spicy_foods['name'])
    # return foods
    return [food['name'] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]>5]
    

def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {'🌶'*foods['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods['cuisine'] == cuisine:
            return foods
    

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    if (len(spicy_foods)>0):
        return (sum([avg_spice['heat_level']for avg_spice in spicy_foods])/len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
