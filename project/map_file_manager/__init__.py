import os
from custom_exceptions import *

class MapFileManager:

    map_files_dir = 'map_files'

    filename = 'test_map.txt'

    file_object = None

    def __init__(self):

        try:

            if not os.path.exists(self.map_files_dir):
                print('Creation of ' + str(self.map_files_dir) + ' folder..')
                os.makedirs(self.map_files_dir)

            print('Opening map file..')
            self.file_object = open(self.map_files_dir + '/' + self.filename, 'a')
        except OSError as e:
            print('MapFileManager Exception: ' + str(e))



    def append(self, data):

        try:
            print('Append data: ' + str(data))
            self.file_object.write(data + "\n")
        except Exception, e:
            print('MapFileManager Exception: ' + str(e))
            self.close()


    def close(self):

        if self.file_object is not None:
            print('Closing file..')
            self.file_object.close()
