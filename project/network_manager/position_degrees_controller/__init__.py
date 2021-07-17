from position_degrees import PositionDegrees

class PositionDegreesController:

    database_manager = PositionDegrees.database_manager

    @staticmethod
    def getPositionsDegrees():
        return PositionDegreesController.database_manager.getAll()
