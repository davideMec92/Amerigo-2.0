import unittest

from project.hashgraph.helpers.CommunicationMessageDecrypter import CommunicationMessageDecrypter
from project.hashgraph.helpers.CommunicationMessageEncrypter import CommunicationMessageEncrypter
from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK


class CommunicationMessageEncryptionTest(unittest.TestCase):
    def testCommunicationMessageEncryptionDecryptionOK(self):
        communicationMessageACK = CommunicationMessageACK()
        encryptedMessage = CommunicationMessageEncrypter.encrypt(communicationMessageACK)
        decryptedMessage = CommunicationMessageDecrypter.decrypt(encryptedMessage)
        self.assertTrue(communicationMessageACK.toJson() == decryptedMessage)


if __name__ == '__main__':
    unittest.main()
