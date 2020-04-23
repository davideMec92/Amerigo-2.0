
#Python custom exceptions

class Error(Exception):
   """Base class for other exceptions"""
   pass


#Proximity Exceptions

class proximityMeasurementErrorException( Error ):
    pass


#Compass Exceptions

class compassGetRotationDegreeCostsException( Error ):
    pass

#Configurator Exceptions

class configuratorLoadConfException( Error ):
    pass

class configuratorGpioInitializationException( Error ):
    pass

#Motors Exceptions
class motorsInitializationException( Error ):
    pass

#Proximity Exception
class proximityInitializationException( Error ):
    pass

class proximityGetDistanceException( Error ):
    pass
