# Copyright 2014 Andrew Cleland
# Map drawing using turtle graphics

# Import necessary packages
import sys
import csv
from turtle import *

# City class - contains name, location, and populatin
class City():
    # Constructor
    def __init__(self, data):
        # data is in form [c, name, x position, y position, population]
        self.name = data[1]
        self.x = float(data[2])
        self.y = float(data[3])
        self.loc = (self.x, self.y)
        self.pop = int(data[4])

# Road class - contains names of connecting cities
class Road():
    # Constructor
    def __init__(self, data):
        # data has form [r, cityname1, cityname2]
        self.city1 = data[1]
        self.city2 = data[2]

# Map class - contains dictionary of cities, list of roads
class Map():
    # Constructor - generates map from a valid csv file
    def __init__(self, mapfile):
        # Read the file
        map_data = csv.reader(open(mapfile))
        # Initialize city dictionary
        self.city = {}
        # Initialize road list
        self.road = []
        # Collect and store data to dictionary and list
        for entry in map_data:
            if entry[0] == 'c':
                newCity = City(entry)
                self.city[newCity.name] = newCity
            elif entry[0] == 'r':
                newRoad = Road(entry)
                self.road.append(newRoad)
            else:
                print('This shouldn\'t print')

    # Method for drawing the map
    


# Allow for command line usage
if __name__ == '__main__':
    main(sys.argv[1])
    



