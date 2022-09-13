import unittest

from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK
from project.hashgraph.validators.communicationMessage.CommunicationMessageSchemaValidator import \
    CommunicationMessageSchemaValidator


class CommunicationMessageSchemaValidatorTest(unittest.TestCase):

    communicationMessageHashgraphOK = """{
   "peer":{
      "address":"B4:86:55:59:A2:E9",
      "deviceId":"5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2",
      "status":"CONNECTED",
      "updatedTime":"1663105787.8421385"
   },
   "store":{
      "events":{
         "2e44d0c334081823f8a6bbe14183d4589ecceb3e0ed9f522f98ff7daa7417138":{
            "bodySignature":"cf8a13eb2e6c86bf8241af1b585e6130dc2caba4aafcba6c129932f4411fcee3",
            "consensusTimestamp":0,
            "eventBody":{
               "creatorAssociation":{
                  "eventCreatorIndex":0,
                  "key":"2e44d0c334081823f8a6bbe14183d4589ecceb3e0ed9f522f98ff7daa7417138",
                  "peerDeviceId":"5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2"
               },
               "timestamp":1663105787,
               "transactions":[
                  
               ]
            },
            "firstDiscendants":{
               "5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2":1
            },
            "isDecided":false,
            "isFamous":false,
            "isWitness":true,
            "lastAncestors":{
               "5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2":0
            },
            "roundCreated":0,
            "roundReceived":-1
         },
         "902ea4dd5daf6eaa8a17f51765b3c91af025c14b447b993e643b7b093a9ffa0f":{
            "bodySignature":"dedffb412fc3ac6a06ac9dac650a22f29e69c3a557c4b342b11f865eae612480",
            "consensusTimestamp":0,
            "eventBody":{
               "creatorAssociation":{
                  "eventCreatorIndex":1,
                  "key":"902ea4dd5daf6eaa8a17f51765b3c91af025c14b447b993e643b7b093a9ffa0f",
                  "peerDeviceId":"5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2"
               },
               "otherParent":{
                  "eventCreatorIndex":0,
                  "key":"02a58b028dac68926307996bebddcd39ac4cac41b13d844ce99a3b7babe1a5cc",
                  "peerDeviceId":"26f3762f-8fde-49ca-9838-a4b1eab9adf1"
               },
               "otherParentHash":"362c6d0dde5da4499a5a530a5aa57d713471d2ec2f2b43efb949b71d41a2d25e",
               "selfParent":{
                  "eventCreatorIndex":0,
                  "key":"2e44d0c334081823f8a6bbe14183d4589ecceb3e0ed9f522f98ff7daa7417138",
                  "peerDeviceId":"5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2"
               },
               "selfParentHash":"cf8a13eb2e6c86bf8241af1b585e6130dc2caba4aafcba6c129932f4411fcee3",
               "timestamp":1663105862,
               "transactions":[
                  
               ]
            },
            "firstDiscendants":{
               "5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2":1
            },
            "isDecided":false,
            "isFamous":false,
            "isWitness":false,
            "lastAncestors":{
               "5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2":1,
               "26f3762f-8fde-49ca-9838-a4b1eab9adf1":0
            },
            "roundCreated":0,
            "roundReceived":-1
         },
         "02a58b028dac68926307996bebddcd39ac4cac41b13d844ce99a3b7babe1a5cc":{
            "bodySignature":"362c6d0dde5da4499a5a530a5aa57d713471d2ec2f2b43efb949b71d41a2d25e",
            "consensusTimestamp":0,
            "eventBody":{
               "creatorAssociation":{
                  "eventCreatorIndex":0,
                  "key":"02a58b028dac68926307996bebddcd39ac4cac41b13d844ce99a3b7babe1a5cc",
                  "peerDeviceId":"26f3762f-8fde-49ca-9838-a4b1eab9adf1"
               },
               "timestamp":1663105856,
               "transactions":[
                  
               ]
            },
            "firstDiscendants":{
               "5f63bcfa-c8af-4feb-85fd-1b5f32ef41a2":1,
               "26f3762f-8fde-49ca-9838-a4b1eab9adf1":0
            },
            "isDecided":false,
            "isFamous":false,
            "isWitness":true,
            "lastAncestors":{
               "26f3762f-8fde-49ca-9838-a4b1eab9adf1":0
            },
            "roundCreated":0,
            "roundReceived":-1
         }
      },
      "rounds":{
         "0":{
            "committed":false,
            "decidedWitnesses":[
               
            ],
            "determinedEvents":[
               
            ],
            "events":[
               "2e44d0c334081823f8a6bbe14183d4589ecceb3e0ed9f522f98ff7daa7417138",
               "02a58b028dac68926307996bebddcd39ac4cac41b13d844ce99a3b7babe1a5cc",
               "902ea4dd5daf6eaa8a17f51765b3c91af025c14b447b993e643b7b093a9ffa0f"
            ],
            "inRoundDeterminedEvents":[
               
            ],
            "peersInRound":2,
            "roundCreated":0,
            "roundReceived":-1,
            "witnesses":[
               "2e44d0c334081823f8a6bbe14183d4589ecceb3e0ed9f522f98ff7daa7417138",
               "02a58b028dac68926307996bebddcd39ac4cac41b13d844ce99a3b7babe1a5cc"
            ]
         }
      }
   },
   "type":"HASHGRAPH"
}"""

    def testCommunicationMessageHashgraphValidationOk(self):
        self.assertTrue(CommunicationMessageSchemaValidator.validate(self.communicationMessageHashgraphOK))

    def testACKMessageValidationOK(self):
        communicationMessageACK = CommunicationMessageACK()
        self.assertTrue(CommunicationMessageSchemaValidator.validate(communicationMessageACK.toJson()))

    def testACKMessageValidationOK(self):
        wrongCommunicationMessageACK = '{"type": "ACK", "wrongProperty": "wrong property value"}'
        self.assertFalse(CommunicationMessageSchemaValidator.validate(wrongCommunicationMessageACK))


if __name__ == '__main__':
    unittest.main()
