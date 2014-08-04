turtle-graphics-map
===================

Uses data from a csv to draw a map with python's turtle graphics.

The csv file contains information about cities, and roads which can connect one city to another.
The first element of each row in the file must begin with either a 'c' (for 'city') or an 'r' (for 'road'). 
If it's a row containing city information, it follows the following format:

  c, City Name, x coordinate, y coordinate, population

If it's a row containing road information, it follows this format:

  r, City Name 1, City Name2

Examples: 

  c,San Diego,-30.333,40.25,1300000
  c,Los Angeles,-33.8,60.29,3858000
  r,San Diego,Los Angeles

  See also testmap.csv
  
If the population of a city is between 1 and 90000, it is considered a town and is drawn on the map as a
small unfilled circle. If the population is greater than 90000, it is drawn as a larger, filled circle. 
A city with population 0 is not drawn on the map, but is saved as a location that roads can connect to. 

