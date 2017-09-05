'''Distance Between Two Cities - Calculates the distance between two cities and allows 
the user to specify a unit of distance. This program may require finding coordinates 
for the cities like latitude and longitude.'''

import math

x1 = input("give input of X1: ")
y1 = input("give input of Y1: ")
x2 = input("give input of X2: ")
y2 = input("give input of Y2: ")


DistanceX = float(x2) - float(x1)
DistanceY = float(y1) - float(y2)  

DistanceX = float(DistanceX ** 2)
DistanceY = float(DistanceY ** 2)

Main = float(DistanceX + DistanceY)
Main = float(Main**(1.0/2))

print(Main)