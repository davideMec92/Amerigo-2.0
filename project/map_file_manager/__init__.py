import os
from custom_exceptions import *
from datetime import date

class MapFileManager:

    map_files_dir = 'map_files'

    filename_prefix = 'map_data_'

    file_exstension = '.txt'

    file_counter = 0

    file_object = None

    today_date = None

    def __init__(self):

        try:

            if not os.path.exists(self.map_files_dir):
                print('Creation of ' + str(self.map_files_dir) + ' folder..')
                os.makedirs(self.map_files_dir)

            self.today_date = str(date.today().strftime("%d_%m_%Y"))

            self.initFile()

        except OSError as e:
            print('MapFileManager Exception: ' + str(e))

    def getFileName(self):
        return self.filename_prefix + self.today_date + '_' + str(self.file_counter) + self.file_exstension

    def initFile(self):

        if self.file_object is not None:
            return

        self.file_counter = self.file_counter + 1

        print('Opening map file..')
        self.file_object = open(self.map_files_dir + '/' + self.getFileName(), 'a')

    def append(self, data):

        try:

            if self.file_object is None:
                print('Init File..')
                self.initFile()

            print('Append data: ' + str(data))
            self.file_object.write(data + "\n")
        except Exception, e:
            print('MapFileManager Exception: ' + str(e))
            self.close()


    def close(self):

        if self.file_object is not None:
            print('Closing file..')
            self.file_object.close()
            self.file_object = None
