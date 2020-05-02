
from numpy import *
from circular_list import circularList
import matplotlib.pyplot as plt
import glob,os
from custom_exceptions import *

class MapAnalyzer:

	orientation_list = circularList()

	actual_orientation = None

	left_proximity_actual_x = None
	left_proximity_actual_y = None

	front_proximity_actual_x = None
	front_proximity_actual_y = None

	right_proximity_actual_x = None
	right_proximity_actual_y = None

	robot_matrix = None

	points_list = []

	robot_movements_x = None
	robot_movements_y = None

	input_files = []

	file_extension_in = '.map'
	file_extension_out = '.png'

	map_files_dir_in = 'map_files'
	map_files_dir_out = 'map_files/map'

	def __init__(self):

		try:

			print('MapAnalyzer init..')

			if not os.path.exists(self.map_files_dir_out):
				print('Creation of ' + str(self.map_files_dir_out) + ' folder..')
				os.makedirs(self.map_files_dir_out)

			for file in glob.glob('./' + self.map_files_dir_in + '/*' + self.file_extension_in):
				print('file: ' + str(file))
				self.input_files.append(file)

		except OSError as e:
			print('MapAnalyzer Exception: ' + str(e))
			raise mapAnalyzerInitializationsException( 'MapAnalyzer Exception: ' + str(e) )

	def initValues(self):

		self.orientation_list = circularList()
		self.orientation_list.push('W')
		self.orientation_list.push('S')
		self.orientation_list.push('E')
		self.actual_orientation = self.orientation_list.push('N')

		self.left_proximity_actual_x = 0
		self.left_proximity_actual_y = 0

		self.front_proximity_actual_x = 0
		self.front_proximity_actual_y = 0

		self.right_proximity_actual_x = 0
		self.right_proximity_actual_y = 0

		#                               W                       N                       S                   E
		self.robot_matrix = array([[{ 'x' : 3, 'y' : 15}, {'x' : 15, 'y' : 13 }, {'x' : 0, 'y' : 3 }, {'x' : 13, 'y' : 0}], #DX
							[{ 'x' : 0, 'y' : 8}, {'x' : 8, 'y' : 15 }, {'x' : 8, 'y' : 0 }, {'x' : 15, 'y' : 8}], #FRONT
							[{ 'x' : 3, 'y' : 0}, {'x' : 0, 'y' : 13 }, {'x' : 15, 'y' : 3 }, {'x' : 13, 'y' : 15}] #LX
							])

		self.robot_movements_x = [ self.robot_matrix[0][2].get('x'), self.robot_matrix[0][2].get('x'), self.robot_matrix[0][1].get('x'), self.robot_matrix[0][1].get('x')]
		self.robot_movements_y = [ self.robot_matrix[0][3].get('y'), self.robot_matrix[0][0].get('y'), self.robot_matrix[0][0].get('y'), self.robot_matrix[0][3].get('y')]

		self.points_list = []

		self.updateActualProximityValues()

	def plotMaps(self):

		if len(self.input_files) > 0:

			for file in self.input_files:
				self.buildMap(file)

	def updateActualProximityValues(self):

	    col_index = None

	    if self.actual_orientation.data == 'W':
	        col_index = 0
	    elif self.actual_orientation.data == 'N':
	        col_index = 1
	    elif self.actual_orientation.data == 'S':
	        col_index = 2
	    elif self.actual_orientation.data == 'E':
	        col_index = 3

	    self.left_proximity_actual_x = self.robot_matrix[2][col_index].get('x')
	    self.left_proximity_actual_y = self.robot_matrix[2][col_index].get('y')

	    self.front_proximity_actual_x = self.robot_matrix[1][col_index].get('x')
	    self.front_proximity_actual_y = self.robot_matrix[1][col_index].get('y')

	    self.right_proximity_actual_x = self.robot_matrix[0][col_index].get('x')
	    self.right_proximity_actual_y = self.robot_matrix[0][col_index].get('y')

	def roundToLowerMultiple(self, x, base=5):
	    #return int(base * round(float(x)/base))
		x = float(x)
		return int(x - (x%base))

	def generateObstacleSquarePointsA(self, x, y):

		#print('A Values x: ' + str(x)+', y: ' + str(y))

		self.points_list.append({'x' : x,'y' : y})
		self.points_list.append({'x' : x + 5,'y' : y})
		self.points_list.append({'x' : x + 5,'y' : y + 5})
		self.points_list.append({'x' : x ,'y' : y + 5})

		#print('A list: ' + str(points_list))

	def generateObstacleSquarePointsB(self, x, y):

		#print('B Values x: ' + str(x)+', y: ' + str(y))

		self.points_list.append({'x' : x,'y' : y})
		self.points_list.append({'x' : x - 5,'y' : y})
		self.points_list.append({'x' : x - 5,'y' : y + 5})
		self.points_list.append({'x' : x ,'y' : y + 5})

		#print('B list: ' + str(points_list))

	def generateObstacleSquarePointsC(self, x, y):

		#print('C Values x: ' + str(x)+', y: ' + str(y))

		self.points_list.append({'x' : x,'y' : y})
		self.points_list.append({'x' : x + 5,'y' : y})
		self.points_list.append({'x' : x + 5,'y' : y - 5})
		self.points_list.append({'x' : x ,'y' : y - 5})

		#print('C list: ' + str(points_list))

	def updateRobotMatrixValues(self, coordinateType, value):

	    for row in self.robot_matrix: #Colonne
	        for item in row: #Righe

	            #print('update value: ' + str(item.get( coordinateType )))

	            if coordinateType == 'y':
	                item.update( y = item.get( coordinateType ) + value )
	            else:
	                item.update( x = item.get( coordinateType ) + value )


		self.robot_movements_x.append(self.robot_matrix[0][2].get('x'))
		self.robot_movements_y.append(self.robot_matrix[0][3].get('y'))

		self.robot_movements_x.append(self.robot_matrix[0][2].get('x'))
		self.robot_movements_y.append(self.robot_matrix[0][0].get('y'))

		self.robot_movements_x.append(self.robot_matrix[0][1].get('x'))
		self.robot_movements_y.append(self.robot_matrix[0][0].get('y'))

		self.robot_movements_x.append(self.robot_matrix[0][1].get('x'))
		self.robot_movements_y.append(self.robot_matrix[0][3].get('y'))

	    #print(str(robot_matrix))

	def buildMap(self, filename):

		try:

			file = open(filename, 'r')

			Lines = file.readlines()

			self.initValues()

			for line in Lines:

			    strip_values = line.strip().split(',')
			    temp_left_proximity = self.roundToLowerMultiple(strip_values[0].strip())
			    temp_front_proximity = self.roundToLowerMultiple(strip_values[1].strip())
			    temp_right_proximity = self.roundToLowerMultiple(strip_values[2].strip())
			    temp_bug_mode_last_move = strip_values[3].strip()

			    #print(str(temp_bug_mode_last_move))

			    if temp_bug_mode_last_move is not None:

			        if temp_bug_mode_last_move == 'C':
			            self.actual_orientation = self.actual_orientation.next
			        elif temp_bug_mode_last_move == 'CC':
			            self.actual_orientation = self.actual_orientation.prev
			        elif temp_bug_mode_last_move == '2C':
			            self.actual_orientation = self.actual_orientation.next
			            self.actual_orientation = self.actual_orientation.next
			        elif temp_bug_mode_last_move == '2CC':
			            self.actual_orientation = self.actual_orientation.prev
			            self.actual_orientation = self.actual_orientation.prev
			        elif temp_bug_mode_last_move == 'F':

			            if self.actual_orientation.data == 'N':
			                self.updateRobotMatrixValues('y', 10)
			            elif self.actual_orientation.data == 'S':
			                self.updateRobotMatrixValues('y', -10)
			            elif self.actual_orientation.data == 'W':
			                self.updateRobotMatrixValues('x', -10)
			            elif self.actual_orientation.data == 'E':
			                self.updateRobotMatrixValues('x', 10)

			    self.updateActualProximityValues()

			    if self.actual_orientation.data == 'N':
			        self.generateObstacleSquarePointsB( self.roundToLowerMultiple(self.left_proximity_actual_x) - temp_left_proximity, self.roundToLowerMultiple( self.left_proximity_actual_y )  )
			        self.generateObstacleSquarePointsA( self.roundToLowerMultiple(self.front_proximity_actual_x), temp_front_proximity + self.front_proximity_actual_y )
			        self.generateObstacleSquarePointsA( self.roundToLowerMultiple(self.right_proximity_actual_x) + temp_right_proximity, self.roundToLowerMultiple( self.right_proximity_actual_y ) )
			    elif self.actual_orientation.data == 'S':
			        self.generateObstacleSquarePointsA( self.roundToLowerMultiple(self.left_proximity_actual_x) + temp_left_proximity, self.roundToLowerMultiple( self.left_proximity_actual_y )  )
			        self.generateObstacleSquarePointsC( self.roundToLowerMultiple(self.front_proximity_actual_x), self.front_proximity_actual_y - temp_front_proximity )
			        self.generateObstacleSquarePointsB( self.roundToLowerMultiple(self.right_proximity_actual_x) - temp_right_proximity, self.roundToLowerMultiple( self.right_proximity_actual_y ) )
			    elif self.actual_orientation.data == 'W':
			        self.generateObstacleSquarePointsC( self.roundToLowerMultiple( self.left_proximity_actual_x ), self.roundToLowerMultiple( self.left_proximity_actual_y ) - temp_left_proximity )
			        self.generateObstacleSquarePointsB( self.roundToLowerMultiple(self.front_proximity_actual_x) - temp_front_proximity, self.roundToLowerMultiple( self.front_proximity_actual_y ) )
			        self.generateObstacleSquarePointsA( self.roundToLowerMultiple(self.right_proximity_actual_x), temp_right_proximity + self.roundToLowerMultiple( self.right_proximity_actual_y ) )
			    elif self.actual_orientation.data == 'E':
			        self.generateObstacleSquarePointsA( self.roundToLowerMultiple(self.left_proximity_actual_x), temp_left_proximity + self.roundToLowerMultiple( self.left_proximity_actual_y ) )
			        self.generateObstacleSquarePointsA( self.roundToLowerMultiple(self.front_proximity_actual_x) + temp_front_proximity, self.roundToLowerMultiple( self.front_proximity_actual_y ) )
			        self.generateObstacleSquarePointsC( self.roundToLowerMultiple(self.right_proximity_actual_x), self.roundToLowerMultiple( self.right_proximity_actual_y ) - temp_right_proximity )

			    #print(str(temp_left_proximity) + ' ' + str(temp_front_proximity) + ' ' + str(temp_right_proximity) + ' ' + str(temp_bug_mode_last_move))

			x = []
			y = []

			for point in self.points_list:
				x.append(point.get('x'))
				y.append(point.get('y'))

			plt.scatter(x, y, color='red')
			plt.scatter(self.robot_movements_x, self.robot_movements_y)
			plt.savefig(self.map_files_dir_out + '/' + os.path.basename(filename).split('.')[0] + self.file_extension_out, dpi=200, bbox_inches='tight')
			plt.clf()

		except Exception, e:
			raise mapAnalyzerPlotBuildException('MapAnalyzer: ' + str(e))
