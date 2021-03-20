from database_manager import DatabaseManager

class CreatorAssociation:

    peerDeviceId = None
    eventCreatorIndex = None

    def __init__( self, dict ):
      self.peerDeviceId = dict["peerDeviceId"]
      self.eventCreatorIndex = dict["eventCreatorIndex"]

    def toDict(self):
        return {'peerDeviceId':self.peerDeviceId, 'eventCreatorIndex':self.eventCreatorIndex}
