from __future__ import annotations

import copy
import time
from typing import Dict

from tinydb import TinyDB, Query

from project.hashgraph.helpers.DatetimeHelper import DatetimeHelper
from project.hashgraph.interfaces.JsonPrintable import JsonPrintable
from project.hashgraph.services.database.TinyDB.TinyDBService import TinyDBService


class TinyDBModel(JsonPrintable):

    def __init__(self, tinyDBService: TinyDBService, primaryKey: str):
        self.db: TinyDB = tinyDBService.db
        self.primaryKey: str = primaryKey
        self.updatedTime: int | None = None
        self.modelQuery = Query()

    def createFromDict(self, entries: dict) -> TinyDBModel:
        self.__dict__.update(entries)
        return self

    def getFromPrimaryKey(self, propertyValue) -> TinyDBModel | None:
        result = self.db.get(self.modelQuery[self.primaryKey] == propertyValue)
        return None if result is None else self.createFromDict(result)

    def upsert(self) -> None:
        self.updateTime()
        self.db.upsert(self.toDict(), Query()[self.primaryKey] == getattr(self, self.primaryKey))

    def save(self) -> None:
        self.updateTime()
        self.db.insert(self.toDict())

    def remove(self) -> None:
        self.db.remove(self.modelQuery[self.primaryKey] == getattr(self, self.primaryKey))

    def updateTime(self) -> None:
        self.updatedTime = DatetimeHelper.getNowTimestamp()

    def toDict(self) -> Dict:
        objectDict = copy.copy(self).__dict__
        objectDict.pop('db', None)
        objectDict.pop('modelQuery', None)
        return objectDict
