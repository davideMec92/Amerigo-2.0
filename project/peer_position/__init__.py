class PeerPosition:

    deviceId = None
    degrees = None

    def __init__( self, dict ):
      self.deviceId = dict["deviceId"]
      self.degrees = dict["degrees"]

    def toDict(self):
        return {'deviceId': self.deviceId, 'degrees':self.degrees}
