from multiprocessing.sharedctypes import synchronized

from project.hashgraph.helpers.Hash import Hash


class Store:
    events = {}
    rounds = {}
    lastMissingEvents = []
    storeCallback = None

    ROUND_DELETE_MARGIN = 1

    # TODO ADD CALLBACK FOR storeCallback
    def __init__(self, storeCallback):
        self.storeCallback = storeCallback

    # TODO ADD STORE CLONE FUNCTION

    def getEvents(self):
        return self.events

    def getRounds(self):
        return self.rounds

    def getLastMissingEvents(self):
        return self.getLastMissingEvents

    def clearLastMissingEvents(self):
        self.lastMissingEvents = []

    def setEvents(self, events):
        self.events = events

    def setRounds(self, rounds):
        self.rounds = rounds

    # TODO ADD putRound METHOD
    """public void putRound(Round round){

        //Check if round exists in order to add a single missing event
        if( this.rounds.containsKey(round.getRoundCreated()) == true ){

            for(String eventKey: ListHelper.getListDiff(this.rounds.get(round.getRoundCreated()).getEvents(), round.getEvents())){
                this.rounds.get(round.getRoundCreated()).getEvents().add(eventKey);
            }

            for(String witnessEventKey: ListHelper.getListDiff(this.rounds.get(round.getRoundCreated()).getWitnesses(), round.getWitnesses())){
                this.rounds.get(round.getRoundCreated()).getWitnesses().add(witnessEventKey);
            }

        } else {
            this.rounds.put(round.getRoundCreated(), round);
        }
    }"""

    def deleteEventFromKey(self, eventKey):
        self.events.pop(eventKey, None)

    @synchronized
    def deleteRoundFromRoundCreatedIndex(self, roundCreated):
        self.rounds.pop(roundCreated, None)

    def storeEvent(self, event):
        self.events[event.getEventBody().getCreatorAssociation().getKey()] = event
        self.storeCallback.eventStoredCallback(self.events.get((event.getEventBody().getCreatorAssociation().getKey())))

    def updateEvent(self, event):
        self.events[event.getEventBody().getCreatorAssociation().getKey()] = event

    def addEventInRound(self, event):
        self.rounds.get(event.getRoundCreated()).addEvent(event.getEventBody().getCreatorAssociation().getKey())

    # TODO IMPLEMENT storeMissingEvents METHOD
    """public void storeMissingEvents(Store otherHashgraph, String peerDeviceId, Integer firstMissingEventCreatorIndex) {
        int missingCreatorEventIndex = firstMissingEventCreatorIndex;
        Event missingEvent = otherHashgraph.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex);

        while(missingEvent != null){
            this.storeEvent(missingEvent);
            missingCreatorEventIndex++;
            missingEvent = otherHashgraph.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex);

            if(missingEvent == null){
                this.lastMissingEvents.add(this.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex - 1));
            }
        }
    }"""

    def getEventFromPeerAndCreatorIndex(self, peerDeviceId, peerCreatorIndex):
        hashKey = Hash.stringToHash(peerDeviceId + peerCreatorIndex)
        return self.getEventFromEventPeerAssociationKey(hashKey)

    def getEventFromEventPeerAssociationKey(self, eventPeerAssociationKey):
        return self.events.get(eventPeerAssociationKey) if eventPeerAssociationKey in self.events else None

    def getRoundFromRoundCreated(self, roundCreated):
        return self.rounds.get(roundCreated) if roundCreated in self.rounds else None

    def removeRoundsBeforeRoundCreatedIndex(self, roundCreatedIndex):
        toRemoveRoundCreatedIndex = (roundCreatedIndex - self.ROUND_DELETE_MARGIN)

        # Check if difference is negative
        if toRemoveRoundCreatedIndex < 0:
            return

        # TODO TO TEST!
        for k, v in self.rounds:
            if k < toRemoveRoundCreatedIndex:
                # Remove all events in round
                for eventKey in v.getEvents():
                    self.deleteEventFromKey(eventKey)

        # TODO TO TEST!
        for i in range(toRemoveRoundCreatedIndex - 1, 0, -1):
            if self.rounds.get(i) is None:
                break

            # Delete round
            self.deleteRoundFromRoundCreatedIndex(i)
