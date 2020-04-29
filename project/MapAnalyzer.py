
#import numpy as np
from numpy import *
from circular_list import circularList
import matplotlib.pyplot as plt

orientation_list = circularList()

orientation_list.push('W')
orientation_list.push('S')
orientation_list.push('E')
actual_orientation = orientation_list.push('N')

left_proximity_actual_x = 0
left_proximity_actual_y = 0

front_proximity_actual_x = 0
front_proximity_actual_y = 0

right_proximity_actual_x = 0
right_proximity_actual_y = 0

#                           W                       N                       S                   E
robot_matrix = array([[{ 'x' : 3, 'y' : 15}, {'x' : 15, 'y' : 13 }, {'x' : 0, 'y' : 3 }, {'x' : 13, 'y' : 0}], #DX
					[{ 'x' : 0, 'y' : 8}, {'x' : 8, 'y' : 15 }, {'x' : 8, 'y' : 0 }, {'x' : 15, 'y' : 8}], #FRONT
					[{ 'x' : 3, 'y' : 0}, {'x' : 0, 'y' : 13 }, {'x' : 15, 'y' : 3 }, {'x' : 13, 'y' : 15}] #LX
					])

points_list = []

robot_movements_x = [ robot_matrix[0][2].get('x'), robot_matrix[0][2].get('x'), robot_matrix[0][1].get('x'), robot_matrix[0][1].get('x')]
robot_movements_y = [ robot_matrix[0][3].get('y'), robot_matrix[0][0].get('y'), robot_matrix[0][0].get('y'), robot_matrix[0][3].get('y')]

# Using readlines()
file = open('data', 'r')
Lines = file.readlines()

def updateActualProximityValues():

    global left_proximity_actual_x
    global left_proximity_actual_y

    global front_proximity_actual_x
    global front_proximity_actual_y

    global right_proximity_actual_x
    global right_proximity_actual_y

    global actual_orientation

    col_index = None

    if actual_orientation.data == 'W':
        col_index = 0
    elif actual_orientation.data == 'N':
        col_index = 1
    elif actual_orientation.data == 'S':
        col_index = 2
    elif actual_orientation.data == 'E':
        col_index = 3

    left_proximity_actual_x = robot_matrix[2][col_index].get('x') #0
    left_proximity_actual_y = robot_matrix[2][col_index].get('y') #13

    front_proximity_actual_x = robot_matrix[1][col_index].get('x') #8
    front_proximity_actual_y = robot_matrix[1][col_index].get('y') #15

    right_proximity_actual_x = robot_matrix[0][col_index].get('x') #15
    right_proximity_actual_y = robot_matrix[0][col_index].get('y') #13

updateActualProximityValues()

def roundToLowerMultiple(x, base=5):
    #return int(base * round(float(x)/base))
	x = float(x)
	return int(x - (x%base))

def generateObstacleSquarePointsA(x,y):

	global points_list

	#print('A Values x: ' + str(x)+', y: ' + str(y))

	points_list.append({'x' : x,'y' : y})
	points_list.append({'x' : x + 5,'y' : y})
	points_list.append({'x' : x + 5,'y' : y + 5})
	points_list.append({'x' : x ,'y' : y + 5})

	#print('A list: ' + str(points_list))

def generateObstacleSquarePointsB(x,y):

	global points_list

	#print('B Values x: ' + str(x)+', y: ' + str(y))

	points_list.append({'x' : x,'y' : y})
	points_list.append({'x' : x - 5,'y' : y})
	points_list.append({'x' : x - 5,'y' : y + 5})
	points_list.append({'x' : x ,'y' : y + 5})

	#print('B list: ' + str(points_list))

def generateObstacleSquarePointsC(x,y):

	global points_list

	#print('C Values x: ' + str(x)+', y: ' + str(y))

	points_list.append({'x' : x,'y' : y})
	points_list.append({'x' : x + 5,'y' : y})
	points_list.append({'x' : x + 5,'y' : y - 5})
	points_list.append({'x' : x ,'y' : y - 5})

	#print('C list: ' + str(points_list))

def updateRobotMatrixValues(coordinateType, value):

    global robot_matrix

    for row in robot_matrix: #Colonne
        for item in row: #Righe

            #print('update value: ' + str(item.get( coordinateType )))

            if coordinateType == 'y':
                item.update( y = item.get( coordinateType ) + value )
            else:
                item.update( x = item.get( coordinateType ) + value )


	robot_movements_x.append(robot_matrix[0][2].get('x'))
	robot_movements_y.append(robot_matrix[0][3].get('y'))

	robot_movements_x.append(robot_matrix[0][2].get('x'))
	robot_movements_y.append(robot_matrix[0][0].get('y'))

	robot_movements_x.append(robot_matrix[0][1].get('x'))
	robot_movements_y.append(robot_matrix[0][0].get('y'))

	robot_movements_x.append(robot_matrix[0][1].get('x'))
	robot_movements_y.append(robot_matrix[0][3].get('y'))

    print(str(robot_matrix))

for line in Lines:

    strip_values = line.strip().split(',')
    temp_left_proximity = roundToLowerMultiple(strip_values[0].strip())
    temp_front_proximity = roundToLowerMultiple(strip_values[1].strip())
    temp_right_proximity = roundToLowerMultiple(strip_values[2].strip())
    temp_bug_mode_last_move = strip_values[3].strip()

    print(str(temp_bug_mode_last_move))

    if temp_bug_mode_last_move is not None:

        if temp_bug_mode_last_move == 'C':
            actual_orientation = actual_orientation.next
        elif temp_bug_mode_last_move == 'CC':
            actual_orientation = actual_orientation.prev
        elif temp_bug_mode_last_move == '2C':
            actual_orientation = actual_orientation.next
            actual_orientation = actual_orientation.next
        elif temp_bug_mode_last_move == '2CC':
            actual_orientation = actual_orientation.prev
            actual_orientation = actual_orientation.prev
        elif temp_bug_mode_last_move == 'F':

            if actual_orientation.data == 'N':
                updateRobotMatrixValues('y', 10)
            elif actual_orientation.data == 'S':
                updateRobotMatrixValues('y', -10)
            elif actual_orientation.data == 'W':
                updateRobotMatrixValues('x', -10)
            elif actual_orientation.data == 'E':
                updateRobotMatrixValues('x', 10)

    updateActualProximityValues()

    if actual_orientation.data == 'N':
        generateObstacleSquarePointsB( roundToLowerMultiple(left_proximity_actual_x) - temp_left_proximity, roundToLowerMultiple( left_proximity_actual_y )  )
        generateObstacleSquarePointsA( roundToLowerMultiple(front_proximity_actual_x), temp_front_proximity + front_proximity_actual_y )
        generateObstacleSquarePointsA( roundToLowerMultiple(right_proximity_actual_x) + temp_right_proximity, roundToLowerMultiple( right_proximity_actual_y ) )
    elif actual_orientation.data == 'S':
        generateObstacleSquarePointsA( roundToLowerMultiple(left_proximity_actual_x) + temp_left_proximity, roundToLowerMultiple( left_proximity_actual_y )  )
        generateObstacleSquarePointsC( roundToLowerMultiple(front_proximity_actual_x), front_proximity_actual_y - temp_front_proximity )
        generateObstacleSquarePointsB( roundToLowerMultiple(right_proximity_actual_x) - temp_right_proximity, roundToLowerMultiple( right_proximity_actual_y ) )
    elif actual_orientation.data == 'W':
        generateObstacleSquarePointsC( roundToLowerMultiple( left_proximity_actual_x ), roundToLowerMultiple( left_proximity_actual_y ) - temp_left_proximity )
        generateObstacleSquarePointsB( roundToLowerMultiple(front_proximity_actual_x) - temp_front_proximity, roundToLowerMultiple( front_proximity_actual_y ) )
        generateObstacleSquarePointsA( roundToLowerMultiple(right_proximity_actual_x), temp_right_proximity + roundToLowerMultiple( right_proximity_actual_y ) )
    elif actual_orientation.data == 'E':
        generateObstacleSquarePointsA( left_proximity_actual_x, temp_left_proximity + roundToLowerMultiple( left_proximity_actual_y ) )
        generateObstacleSquarePointsA( roundToLowerMultiple(front_proximity_actual_x) + temp_front_proximity, roundToLowerMultiple( front_proximity_actual_y ) )
        generateObstacleSquarePointsC( roundToLowerMultiple(right_proximity_actual_x), roundToLowerMultiple( right_proximity_actual_y ) - temp_right_proximity )

    print(str(temp_left_proximity) + ' ' + str(temp_front_proximity) + ' ' + str(temp_right_proximity) + ' ' + str(temp_bug_mode_last_move))

x = []
y = []

for point in points_list:
	x.append(point.get('x'))
	y.append(point.get('y'))

plt.scatter(x, y, color='red')
plt.scatter(robot_movements_x, robot_movements_y)
plt.xlim(-200,200)
plt.ylim(-200,200)
plt.show()
