from threading import Thread

from project.Logger.Logger import Logger, LogLevels
from project.bluetooth_client import BluetoothClient
from project.bluetooth_settings import BluetoothSettings
from project.hashgraph.helpers.FifoQueue import FifoQueue  # type: ignore
from project.hashgraph.models.Block import Block
from project.hashgraph.models.communication.CommunicationMessageBlock import CommunicationMessageBlock


class BlockManager(Thread):
    toCommitBlocks: FifoQueue[Block] = []
    isSendEnabled: bool = True

    def stopSending(self) -> None:
        self.isSendEnabled = False

    def sendBlock(self, block: Block) -> None:
        self.toCommitBlocks.push(block)

    def run(self) -> None:
        isBlockSent: bool = False

        while self.isSendEnabled is True:
            if self.toCommitBlocks.isEmpty() is False:
                isBlockSent = True
                try:
                    bluetoothClient: BluetoothClient = BluetoothClient(BluetoothSettings.BluetoothServerBluetoothMAC, BluetoothSettings.BluetoothServerUUID)
                    bluetoothClient.sendMessage(CommunicationMessageBlock(self.toCommitBlocks.peek().build()))
                except Exception as e:
                    Logger.createLog(LogLevels.ERROR, __file__, 'Error during building and sending block: ' + str(e))
                    isBlockSent = False
                finally:
                    if isBlockSent is True:
                        self.toCommitBlocks.peek().store.removeRoundsBeforeRoundCreatedIndex(self.toCommitBlocks.peek().roundCreated)
                        self.toCommitBlocks.remove()






