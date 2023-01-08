import re
from list_module import *
from get_weather import get_weather



#town_list = load_object_town()
#Menu code
def print_menu():
  print("1. weather by link")
  print("2. weather from list")
  print("3. add town to list")
  print("4. remove town from list")
  print("5. weather by coordinates")
  print("6. Quit")

def menu():
  while True:
    #Print the menu
    print_menu()
    
    # Get the user's choice
    choice = input("Enter your choice: ")
    # Run the chosen function
    if choice == "1":
        get_weather_from_link()
    elif choice == "2":
        get_weather_from_list()
    elif choice == "3":
        add_object_town()
    elif choice == "4":
        remove_object_town()
    elif choice == "5":
        get_weather_from_coords()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Try again.")



#Get weather from a google maps link with cordinates
def get_weather_from_link():
    # Retrieve the webpage
    url = input("Enter a link: ")
    match = re.search(r"@(-?\d+\.\d+),(-?\d+\.\d+)", url)
    
    # Extract the x and y values from the match
    x = match.group(1)
    y = match.group(2)
    
    
    #send request to get_weather(x,y).py
    get_weather(x,y)



#Get weather from entering cords (x, y)
def get_weather_from_coords():
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    get_weather(x,y)