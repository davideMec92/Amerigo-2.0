import abc


class StoreCallback(abc.ABC):
    @abc.abstractmethod
    def eventStoredCallback(self):
        pass
