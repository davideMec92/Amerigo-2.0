from __future__ import annotations

import copy
import time

from tinydb import where, TinyDB, Query
from typing import Dict

from project.hashgraph.services.database.TinyDB.TinyDBService import TinyDBService


class TinyDBModel:

    def __init__(self, tinyDBService: TinyDBService, primaryKey: str):
        self.db: TinyDB = tinyDBService.db
        self.primaryKey: str = primaryKey
        self.updatedTime: float | None = None

    def createFromDict(self, **entries: dict) -> TinyDBModel:
        self.toDict().update(entries)
        return self

    def getFromProperty(self, propertyName, propertyValue) -> TinyDBModel | None:
        result = self.db.search(where(propertyName) == propertyValue)
        if len(result) == 0:
            return None
        else:
            return self.createFromDict(result)

    def upsert(self) -> None:
        self.db.upsert(self.updateTime(), Query()[self.primaryKey] == getattr(self, self.primaryKey))

    def save(self) -> None:
        self.db.insert(self.updateTime())

    def remove(self) -> None:
        self.db.remove(Query()[self.primaryKey] == getattr(self, self.primaryKey))

    def updateTime(self) -> Dict:
        self.updatedTime = str(time.time())
        return self.toDict()

    def toDict(self) -> Dict:
        objectDict = copy.copy(self).__dict__
        objectDict.pop('db', None)
        return objectDict
