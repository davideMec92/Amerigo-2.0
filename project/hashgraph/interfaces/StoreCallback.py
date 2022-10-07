import abc

from project.hashgraph.models.Event import Event

class StoreCallback(abc.ABC):
    @abc.abstractmethod
    def eventStoredCallback(self, event: Event):
        pass
