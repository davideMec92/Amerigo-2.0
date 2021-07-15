from database_manager import DatabaseManager
from creatorAssociation import CreatorAssociation

class Event:

    consensusTimestamp = None,
    transactions = [],
    creatorAssociation = None;

    def __init__( self, dict ):
      self.consensusTimestamp = dict["consensusTimestamp"]
      self.transactions = dict["transactions"]
      self.creatorAssociation = CreatorAssociation(dict["creatorAssociation"])

    def toDict(self):
        return {'consensusTimestamp': self.consensusTimestamp, 'transactions': self.transactions, 'creatorAssociation': self.creatorAssociation.toDict()}
