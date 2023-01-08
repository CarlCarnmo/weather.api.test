import pickle
from get_weather import get_weather



#Towns class for list
class Town:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Name: {self.name} (x:{self.x}, y:{self.y})"


# Save a list of objects of MyClass to a file
def save_object_list(town_list):
    with open('save\Towns.pk1', 'wb') as f:
        pickle.dump(town_list, f)


# Load a list of objects of MyClass from a file
def load_object_town():
    with open('save\Towns.pk1', 'rb') as f:
        return pickle.load(f)


# Remove a object from town.pk1
def remove_object_town():
    town_list = load_object_town()
    for town in town_list:
        print(repr(town))
    name = input("Enter name of a town to remove: ")
    town_list = load_object_town()
    town_list = [town for town in town_list if town.name != name]
    save_object_list(town_list)


def add_object_town():
    name = input('Enter the name of the town: ')
    x = input('Enter the x coordinate of the town: ')
    y = input('Enter the y coordinate of the town: ')
    
    # Load towns
    town_list = load_object_town()

    # Create a new Town object
    new_town = Town(name, x, y)

    # Append the new town to the list
    town_list.append(new_town)

    save_object_list(town_list)


def get_weather_from_list():

    # Load Towns
    town_list = load_object_town()

    # Print Towns
    for town in town_list:
        print(repr(town))
    name = input("Enter the name of the town you want data from: ")

    #Find the correct town
    s_town = next(town for town in town_list if town.name == name)

    #get_weather
    get_weather(s_town.x,s_town.y)


"""
town_list = [Town("Stockholm", 2.123123, 32.12345), Town("Mjölby", 52.5567567, 62.45674534)]
save_object_list(town_list, 'Towns.lis')
town_list = load_object_town()
for town in town_list:
    print(repr(town))
"""