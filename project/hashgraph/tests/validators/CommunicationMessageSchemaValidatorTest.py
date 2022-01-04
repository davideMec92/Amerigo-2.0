import unittest

from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK
from project.hashgraph.validators.communicationMessage.CommunicationMessageSchemaValidator import \
    CommunicationMessageSchemaValidator


class CommunicationMessageSchemaValidatorTest(unittest.TestCase):

    def testACKMessageValidationOK(self):
        communicationMessageACK = CommunicationMessageACK()
        self.assertTrue(CommunicationMessageSchemaValidator.validate(communicationMessageACK.toJson()))


if __name__ == '__main__':
    unittest.main()
