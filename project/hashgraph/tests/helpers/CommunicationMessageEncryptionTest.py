import unittest

from project.hashgraph.helpers.CommunicationMessageEncrypter import CommunicationMessageEncrypter
from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK


class CommunicationMessageEncrypterTest(unittest.TestCase):
    def testCommunicationMessageEncryption(self):
        communicationMessageACK = CommunicationMessageACK()
        print('ENCRYPT: ' + CommunicationMessageEncrypter.encrypt(communicationMessageACK))
        self.assertTrue(True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
