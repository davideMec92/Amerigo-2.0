from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationCallback:
    def clientResponseCallback(self, message: CommunicationMessage) -> None:
        raise Exception('Method not implemented')
