from path import Path
from tinydb import TinyDB


class TinyDBService:

    # TODO INSTALL UNIQUE CONSTRAINT CHECKS TinyDB-CONSTRAINT
    # DB default settings
    DB_DEFAULT_NAME = 'default_db.json'

    def __init__(self, databaseName=None):
        self.DB_DEFAULT_PATH = None
        p = Path(__file__)

        for part in p.parts():
            if self.DB_DEFAULT_PATH is None:
                self.DB_DEFAULT_PATH = part
            elif self.DB_DEFAULT_PATH == '/':
                self.DB_DEFAULT_PATH = self.DB_DEFAULT_PATH + part
            else:
                self.DB_DEFAULT_PATH = self.DB_DEFAULT_PATH + '/' + part

            if part == 'hashgraph':
                self.DB_DEFAULT_PATH = self.DB_DEFAULT_PATH + '/data/'
                break

        TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}

        if databaseName is not None:
            self.DB_DEFAULT_NAME = databaseName + '.json'

        print(('Initializing ' + str(self.DB_DEFAULT_NAME) + ' DB..'))
        self.db: TinyDB = TinyDB(self.DB_DEFAULT_PATH + self.DB_DEFAULT_NAME)
