from __future__ import annotations

import copy
import time
from typing import Dict

from tinydb import TinyDB, Query

from project.hashgraph.interfaces.JsonPrintable import JsonPrintable
from project.hashgraph.services.database.TinyDB.TinyDBService import TinyDBService


class TinyDBModel(JsonPrintable):

    def __init__(self, tinyDBService: TinyDBService, primaryKey: str):
        self.db: TinyDB = tinyDBService.db
        self.primaryKey: str = primaryKey
        self.updatedTime: float | None = None
        self.modelQuery = Query()

    def createFromDict(self, entries: dict) -> TinyDBModel:
        self.__dict__.update(entries)
        return self

    def getFromPrimaryKey(self, propertyValue) -> TinyDBModel | None:
        result = self.db.get(self.modelQuery[self.primaryKey] == propertyValue)
        return None if result is None else self.createFromDict(result)

    def upsert(self) -> None:
        self.db.upsert(self.updateTime(), Query()[self.primaryKey] == getattr(self, self.primaryKey))

    def save(self) -> None:
        self.db.insert(self.updateTime())

    def remove(self) -> None:
        self.db.remove(self.modelQuery[self.primaryKey] == getattr(self, self.primaryKey))

    def updateTime(self) -> Dict:
        self.updatedTime = str(int(time.time()))
        return self.toDict()

    def toDict(self) -> Dict:
        objectDict = copy.copy(self).__dict__
        objectDict.pop('db', None)
        objectDict.pop('modelQuery', None)
        return objectDict
