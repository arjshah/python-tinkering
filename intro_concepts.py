# Playing with lists
cars = ['bmw', 'audi', 'mercedes']

# Simple if else statements
for car in cars:
    if car == 'bmw': 
        print(car.upper())
    else:
        print(car.title())

# Looping through list values
available_toppings = ['extra cheese', 'onion', 'mushrooms', 'olives', 'green peppers', 'pepperoni']
requested_toppings = ['extra cheese', 'pepperoni', 'garlic']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we are out of {requested_topping}")

print("\nFinish making your pizza!")

# Playing with dictionaries
alien = {'color': 'green', 'points': 5}
print(alien)

# Adding new key value pairs to a dictionary
alien['x_position'] = 0
alien['y_position'] = 25

print(alien)

# Using get method when looking up unconfirmed keys in a dictionary
favorite_languages = {
        'arjun': 'python',
        'annie': 'elk',
        'frankie': 'lisp',
        'sheru': 'c',
        'kari': 'lisp'
}

frankie_favorite = favorite_languages.get('YOE', 'No YOE data available')
print(frankie_favorite)

# Looping through a dictionary, printing values and using set method to eliminate repetitions
for value in set(favorite_languages.values()):
    print(value.title())

# Nesting dictionaries inside a list
alien_list = []

for alien_number in range(20):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_list.append(new_alien)

for alien in alien_list[:5]:
    print(alien)
print("...")

print(f"Total alien count: {len(alien_list)}")