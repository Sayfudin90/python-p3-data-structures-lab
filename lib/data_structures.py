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

# Function to get names of all spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# Function to get spiciest foods (heat level > 5)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# Function to print spicy foods with their heat level as 🌶 emojis
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# Function to get a spicy food by its cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

# Function to print only the spiciest foods (heat level > 5)
def print_spiciest_foods(spicy_foods):
    spicy_foods_above_5 = get_spiciest_foods(spicy_foods)
    for food in spicy_foods_above_5:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# Function to calculate the average heat level of all foods
def average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

# Function to add a new spicy food to the list
def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods
