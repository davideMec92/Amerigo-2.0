
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt

left_proximity_actual_x = 0
left_proximity_actual_y = 13

front_proximity_actual_x = 8
front_proximity_actual_y = 15

right_proximity_actual_x = 15
right_proximity_actual_y = 13

robot_matrix = array([[{ 'x' : 3, 'y' : 15}, {'x' : 15, 'y' : 13 }, {'x' : 0, 'y' : 3 }, {'x' : 13, 'y' : 0}],
					[{ 'x' : 0, 'y' : 8}, {'x' : 8, 'y' : 15 }, {'x' : 8, 'y' : 0 }, {'x' : 15, 'y' : 8}],
					[{ 'x' : 3, 'y' : 0}, {'x' : 0, 'y' : 13 }, {'x' : 15, 'y' : 3 }, {'x' : 13, 'y' : 15}]
					])

print(robot_matrix)

orientation_index = 'N'

points_list = []

# Using readlines()
file = open('data', 'r')
Lines = file.readlines()

def roundToLowerMultiple(x, base=5):
    #return int(base * round(float(x)/base))
	x = float(x)
	return int(x - (x%base))

def generateObstacleSquarePointsLeft(x,y):

	#print('Values x: ' + str(x)+', y: ' + str(y))

	points_list.append({'x' : x,'y' : y})
	points_list.append({'x' : x - 5,'y' : y})
	points_list.append({'x' : x - 5,'y' : y + 5})
	points_list.append({'x' : x ,'y' : y + 5})

	#print('list: ' + str(points_list))

def generateObstacleSquarePointsFront(x,y):

	#print('Values x: ' + str(x)+', y: ' + str(y))

	points_list.append({'x' : x,'y' : y})
	points_list.append({'x' : x + 5,'y' : y})
	points_list.append({'x' : x + 5,'y' : y + 5})
	points_list.append({'x' : x ,'y' : y + 5})

	#print('list: ' + str(points_list))

def generateObstacleSquarePointsRight(x,y):

	print('Values x: ' + str(x)+', y: ' + str(y))

	points_list.append({'x' : x,'y' : y})
	points_list.append({'x' : x + 5,'y' : y})
	points_list.append({'x' : x + 5,'y' : y + 5})
	points_list.append({'x' : x ,'y' : y + 5})

	print('list: ' + str(points_list))

for line in Lines:
	strip_values = line.strip().split(',')
	temp_left_proximity = roundToLowerMultiple(strip_values[0])
	temp_front_proximity = roundToLowerMultiple(strip_values[1])
	temp_right_proximity = roundToLowerMultiple(strip_values[2])
	temp_bug_mode_last_move = strip_values[3]

	"""if temp_bug_mode_last_move is not None:

		if temp_bug_mode_last_move == 'C':

		elif temp_bug_mode_last_move == 'CC':
		elif temp_bug_mode_last_move == '2C':
			orientation_index = 'W'
		elif temp_bug_mode_last_move == '2CC':
			pass
		elif temp_bug_mode_last_move == 'F':"""



	generateObstacleSquarePointsLeft( left_proximity_actual_x - temp_left_proximity, roundToLowerMultiple( left_proximity_actual_y )  )
	generateObstacleSquarePointsFront( temp_front_proximity, temp_front_proximity + front_proximity_actual_y )
	generateObstacleSquarePointsRight( right_proximity_actual_x + temp_right_proximity, roundToLowerMultiple( right_proximity_actual_y ) )

	print(str(temp_left_proximity) + ' ' + str(temp_front_proximity) + ' ' + str(temp_right_proximity) + ' ' + str(temp_bug_mode_last_move))

x = [0,0,15,15]
y = [0,15,15,0]

for point in points_list:
	x.append(point.get('x'))
	y.append(point.get('y'))



plt.scatter(x, y)
plt.xlim(-150,150)
plt.ylim(-150,150)
plt.show()
