import unittest

from project.hashgraph.helpers.models.JSONDecoders.StoreJSONDecoder import StoreJSONDecoder
from project.hashgraph.models.Store import Store


class HashgraphStoreDeserializerTest(unittest.TestCase):

    jsonStore = """{
  "events": {
    "5ba2c833c5d65e649e4b4fa4d426223f3300650f874e32c4451d9346ce6469e2": {
      "bodySignature": "562a91837c9922cf666b2e29b7653a909aa801688c332b528d1ed4ce28aa0af6",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 5,
          "key": "5ba2c833c5d65e649e4b4fa4d426223f3300650f874e32c4451d9346ce6469e2",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
          "peerDeviceId": "A"
        },
        "otherParentHash": "63bbfdc2be6d2992df8ec9e7eacac60875071890aa9fd8ebea7a8f7ddf29dc0e",
        "selfParent": {
          "eventCreatorIndex": 4,
          "key": "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
          "peerDeviceId": "B"
        },
        "selfParentHash": "694e403297c502c36c6bbcf3249589a226e3469cc161445121644e31a44adf73",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 6
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 4,
        "B": 5,
        "C": 1,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece": {
      "bodySignature": "296dc1e26e8020381d9c4db50630b39eca9f75a6a802a6ba419c947ef81819f0",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 25,
          "key": "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 18,
          "key": "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
          "peerDeviceId": "D"
        },
        "otherParentHash": "534f0480f75ad211c373a7ab291bf528a6bc893b503c1e79c446c351dbc6993d",
        "selfParent": {
          "eventCreatorIndex": 24,
          "key": "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b",
          "peerDeviceId": "B"
        },
        "selfParentHash": "c65458629bd0aed13340bf9870fe9d5b6992dcb1d496c6bdb3c809b3325ad59e",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 16,
        "B": 26,
        "C": 9,
        "D": 19
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 15,
        "B": 25,
        "C": 7,
        "D": 18
      },
      "roundCreated": 7,
      "roundReceived": 8
    },
    "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4": {
      "bodySignature": "18d68dfa4cb0e082ef772a5bfbde7bbdfdebe2dfc7a1b226b6f1e44431b1e061",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 6,
          "key": "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
          "peerDeviceId": "A"
        },
        "otherParentHash": "63bbfdc2be6d2992df8ec9e7eacac60875071890aa9fd8ebea7a8f7ddf29dc0e",
        "selfParent": {
          "eventCreatorIndex": 5,
          "key": "12a750139ca2e4c14287bb6ed9ece9ee75b556a911f19f91c2f0d59ef40e7597",
          "peerDeviceId": "D"
        },
        "selfParentHash": "f1cb1707110eb15e02b7178a0f86d7dd8db1b5ec90cc0b1dc4d58546bd84d393",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 6,
        "D": 7
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 4,
        "B": 4,
        "C": 1,
        "D": 6
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca": {
      "bodySignature": "c0b1600027320bddc1ef90f1549ed399d84da0f9dd749b19fa1d9e04b233c16c",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 3,
          "key": "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 8,
          "key": "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb",
          "peerDeviceId": "D"
        },
        "otherParentHash": "bbf42bc814810e0c113add9cdf71ea96bbcfb727f481f59b8b73914bfc597c07",
        "selfParent": {
          "eventCreatorIndex": 2,
          "key": "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
          "peerDeviceId": "C"
        },
        "selfParentHash": "22f19b46c7c817e5ff0003c321eaf7350b9740289b1ccff9e568b43736f5e7a6",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "B": 12,
        "C": 4,
        "D": 10
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 4,
        "B": 6,
        "C": 3,
        "D": 8
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57": {
      "bodySignature": "694e403297c502c36c6bbcf3249589a226e3469cc161445121644e31a44adf73",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 4,
          "key": "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
          "peerDeviceId": "D"
        },
        "otherParentHash": "c0dea7a627c4e4f449a200e8e7e24fb65c1983825de9860fe849283c833f9f35",
        "selfParent": {
          "eventCreatorIndex": 3,
          "key": "0cd20d37dbaa799d1d2f6f04adbab0b9e958b083f38e06512cdefadd20863f98",
          "peerDeviceId": "B"
        },
        "selfParentHash": "a28524fcd4b22424ed7f46c58cba876e3f794f3c136faeb463472db1351cdd01",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 4,
        "B": 4,
        "D": 6
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 1,
        "B": 4,
        "C": 0,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677": {
      "bodySignature": "8d02e5067cb6d45c5046efd177cf805e76a7d64450e0a30b4a4bb5f1f2f74d63",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 21,
          "key": "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 13,
          "key": "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
          "peerDeviceId": "A"
        },
        "otherParentHash": "49e76ca4db45b2d6a9815038bcc8fb51887f000ac57c64ea18006d9800709cea",
        "selfParent": {
          "eventCreatorIndex": 20,
          "key": "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e",
          "peerDeviceId": "B"
        },
        "selfParentHash": "7c07a4f40b931b398ac7dcdc2ed24be2221c25bf080ad3fd1bd97f8baf18ade5",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 18
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 13,
        "B": 21,
        "C": 6,
        "D": 15
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524": {
      "bodySignature": "a034d1aca11febf230c76446a18aa6ef8800c62dd8faf38924423bea850c34c6",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 9,
          "key": "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 26,
          "key": "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85",
          "peerDeviceId": "B"
        },
        "otherParentHash": "22c0e532a8783d107fc60d749985ab667d7bf293769d33c9ac62b82644ad2d5c",
        "selfParent": {
          "eventCreatorIndex": 8,
          "key": "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
          "peerDeviceId": "C"
        },
        "selfParentHash": "ac065284c027a7421f80702c3c0c998c8d2b1b48d148cb0d529d85962b0f1613",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 16,
        "B": 28,
        "C": 10,
        "D": 19
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 15,
        "B": 26,
        "C": 9,
        "D": 18
      },
      "roundCreated": 7,
      "roundReceived": 8
    },
    "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14": {
      "bodySignature": "a78884ab937e09055e931c3aec6249e8193c7c30b3d6a716971b98e2053c9f3d",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 0,
          "key": "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14",
          "peerDeviceId": "A"
        },
        "timestamp": 1641661514,
        "transactions": []
      },
      "firstDiscendants": {
        "A": 2,
        "D": 4
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 0
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97": {
      "bodySignature": "cca20bb93dda7cbe0407d7ddef39d853be213e4bfa5d980c154dfc792a358c23",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 7,
          "key": "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 9,
          "key": "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359",
          "peerDeviceId": "B"
        },
        "otherParentHash": "2f3d19ba9c370890af844c580b94b9196acdad9d8a9ce758e2a6d31d11c8f27c",
        "selfParent": {
          "eventCreatorIndex": 6,
          "key": "d94791a85f88d5f49c3cc06d5557316cf743d60149820c594f389a1b301ff021",
          "peerDeviceId": "A"
        },
        "selfParentHash": "e94c54c6e016be7de03582659a4ea469f3e65913bd28c88bb111fde371c17152",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "B": 12,
        "C": 5,
        "D": 12
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 7,
        "B": 9,
        "C": 3,
        "D": 8
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1": {
      "bodySignature": "edfab87ae5bd096d6184db50c2324aff5068b87249f330d2e109dc53ec5b0c88",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 6,
          "key": "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 15,
          "key": "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23",
          "peerDeviceId": "D"
        },
        "otherParentHash": "527cf5e61b2a32a5782f1485a91788d3648e6f98becd25db3293deca23ebaf49",
        "selfParent": {
          "eventCreatorIndex": 5,
          "key": "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
          "peerDeviceId": "C"
        },
        "selfParentHash": "a137eb02f7b5a27cfeb6f2665028a70bf77abc92da0cdc1b0cf907aae3a5ecb2",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 24,
        "C": 7,
        "D": 16
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 10,
        "B": 17,
        "C": 6,
        "D": 15
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "00ceeab4df7002aad9c625c69e81c47d07f71027ad3600787a73c7e91fdf8d61": {
      "bodySignature": "68dd820ec128de7f4ee6e02c079eef69db7257c27c193e2f3fe0d1d309ae849a",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 18,
          "key": "00ceeab4df7002aad9c625c69e81c47d07f71027ad3600787a73c7e91fdf8d61",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 11,
          "key": "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
          "peerDeviceId": "A"
        },
        "otherParentHash": "ceac2b2e3545b1bd388e4982c603eed3b023dace8d698484acf5a0b3c378159f",
        "selfParent": {
          "eventCreatorIndex": 17,
          "key": "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
          "peerDeviceId": "B"
        },
        "selfParentHash": "edd2f8d2b43a0928ed840c328760627dfa501a1c4021567d33b51432efd8da28",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 21,
        "D": 16
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 11,
        "B": 18,
        "C": 5,
        "D": 13
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af": {
      "bodySignature": "83079dc796ad1a9290b00557a2ffc701980b0b4d637849091a7c691788cb5bad",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 16,
          "key": "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 20,
          "key": "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e",
          "peerDeviceId": "B"
        },
        "otherParentHash": "7c07a4f40b931b398ac7dcdc2ed24be2221c25bf080ad3fd1bd97f8baf18ade5",
        "selfParent": {
          "eventCreatorIndex": 15,
          "key": "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23",
          "peerDeviceId": "D"
        },
        "selfParentHash": "527cf5e61b2a32a5782f1485a91788d3648e6f98becd25db3293deca23ebaf49",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 16
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 11,
        "B": 20,
        "C": 6,
        "D": 16
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "a7dc9aa658db149b641d28252d72e0b081504170be70b919c22bcefc43e5b33c": {
      "bodySignature": "e6601072723a554da4dcb8481855fd91315f8875f4701aa6cbf3712d7fb71b54",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 11,
          "key": "a7dc9aa658db149b641d28252d72e0b081504170be70b919c22bcefc43e5b33c",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 12,
          "key": "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
          "peerDeviceId": "B"
        },
        "otherParentHash": "10f1f621f8d9ad99a7a317f9bcd757315f23fb15d019f8e48ee0b1f3032b1141",
        "selfParent": {
          "eventCreatorIndex": 10,
          "key": "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
          "peerDeviceId": "D"
        },
        "selfParentHash": "04484a7899836ba785c3af28676a5459044836a57d5f2a500ed182f54b5e9273",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "D": 12
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 7,
        "B": 12,
        "C": 3,
        "D": 11
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "91bec90d2f59a91f2e7c08d17b5334af65f58b47672600b8bdb4a44a8b0d81c8": {
      "bodySignature": "f39c5c8ae64becdf9e490201e88cc053b45fc8d206b36fed91c33c7e6f2f07e5",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 12,
          "key": "91bec90d2f59a91f2e7c08d17b5334af65f58b47672600b8bdb4a44a8b0d81c8",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 19,
          "key": "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024",
          "peerDeviceId": "B"
        },
        "otherParentHash": "d5e840b39b4b6a80099d689911c6223716f5c4d813b5922a481c5ad270552bd4",
        "selfParent": {
          "eventCreatorIndex": 11,
          "key": "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
          "peerDeviceId": "A"
        },
        "selfParentHash": "ceac2b2e3545b1bd388e4982c603eed3b023dace8d698484acf5a0b3c378159f",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 13
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 12,
        "B": 19,
        "C": 5,
        "D": 13
      },
      "roundCreated": 5,
      "roundReceived": 7
    },
    "2265f5336d7b6037b5b75ace727a6c482c37ae963dad3bd8eff402314e8548ab": {
      "bodySignature": "cf5e521ec88c69bfd758eb7a8f5037faa3b6f18c3b41c7773922809d52342dc4",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 2,
          "key": "2265f5336d7b6037b5b75ace727a6c482c37ae963dad3bd8eff402314e8548ab",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 1,
          "key": "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
          "peerDeviceId": "B"
        },
        "otherParentHash": "d2b8b2ac46bcb1a0cc23a863ee4f13902270d8b58ef128cfc74508ac1bc49684",
        "selfParent": {
          "eventCreatorIndex": 1,
          "key": "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681",
          "peerDeviceId": "D"
        },
        "selfParentHash": "8b4b39f1992af5a79a876eb67dc71c198791f038604b2aa3bdcf01419e2b3bf8",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "D": 4
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "B": 1,
        "D": 2
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c": {
      "bodySignature": "677ffb4fac601c6b4c21a07ca9ea72532b30e353c4cfbee6ec0036e4770e6ae8",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 14,
          "key": "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 8,
          "key": "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
          "peerDeviceId": "A"
        },
        "otherParentHash": "64e4994b05364f5393515305175dd2c29b3fdd7d8cfc66bc37b87331ac1093bd",
        "selfParent": {
          "eventCreatorIndex": 13,
          "key": "7f4ad165faba63f8891890e1704cf042727c76dfb8812ffaff566517cb8be642",
          "peerDeviceId": "B"
        },
        "selfParentHash": "7d9cbfd4290ca10f936cd7b769a42ca515fb9f8cc22ee290e3aab61c76f6b33d",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 15
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 8,
        "B": 14,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 5
    },
    "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd": {
      "bodySignature": "de432dfe38ebe55085fa4858c5a92998e4498dc2110a2d617c05a0984459ebcc",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 15,
          "key": "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 5,
          "key": "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
          "peerDeviceId": "C"
        },
        "otherParentHash": "a137eb02f7b5a27cfeb6f2665028a70bf77abc92da0cdc1b0cf907aae3a5ecb2",
        "selfParent": {
          "eventCreatorIndex": 14,
          "key": "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c",
          "peerDeviceId": "B"
        },
        "selfParentHash": "677ffb4fac601c6b4c21a07ca9ea72532b30e353c4cfbee6ec0036e4770e6ae8",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 10,
        "B": 15,
        "D": 13
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 8,
        "B": 15,
        "C": 5,
        "D": 12
      },
      "roundCreated": 4,
      "roundReceived": 5
    },
    "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e": {
      "bodySignature": "7c07a4f40b931b398ac7dcdc2ed24be2221c25bf080ad3fd1bd97f8baf18ade5",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 20,
          "key": "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 6,
          "key": "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
          "peerDeviceId": "C"
        },
        "otherParentHash": "edfab87ae5bd096d6184db50c2324aff5068b87249f330d2e109dc53ec5b0c88",
        "selfParent": {
          "eventCreatorIndex": 19,
          "key": "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024",
          "peerDeviceId": "B"
        },
        "selfParentHash": "d5e840b39b4b6a80099d689911c6223716f5c4d813b5922a481c5ad270552bd4",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 21,
        "D": 16
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 11,
        "B": 20,
        "C": 6,
        "D": 15
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "5985f6f8353e299ba80dec0a569d2757f733a25567a6a4f38f5f102770495ae6": {
      "bodySignature": "376a3e732eb3839637acefedf2c73d2475abe32fb9d7dd6e808312b12e6518db",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 18,
          "key": "5985f6f8353e299ba80dec0a569d2757f733a25567a6a4f38f5f102770495ae6",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 13,
          "key": "6645ca87da6316d5bb2b8e48f6d382c9ffff5a74966c81debc183dc6bb84130d",
          "peerDeviceId": "C"
        },
        "otherParentHash": "5faffed1433fbed44fd20361994c4d5209056a8f8aa5f146f82bb921b3d6d256",
        "selfParent": {
          "eventCreatorIndex": 17,
          "key": "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc",
          "peerDeviceId": "A"
        },
        "selfParentHash": "c621ca66d1528315b1571404a6692d2719d80efb4c48797f81a64605fbef1e27",
        "timestamp": 1641661517,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 18,
        "B": 31,
        "C": 14,
        "D": 21
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 18,
        "B": 30,
        "C": 13,
        "D": 20
      },
      "roundCreated": 10,
      "roundReceived": -1
    },
    "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648": {
      "bodySignature": "bcbe4df273080c34fba91a209ad69c1f5964dfd441bd2bfced0972fe3b4539e8",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 1,
          "key": "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 1,
          "key": "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
          "peerDeviceId": "B"
        },
        "otherParentHash": "d2b8b2ac46bcb1a0cc23a863ee4f13902270d8b58ef128cfc74508ac1bc49684",
        "selfParent": {
          "eventCreatorIndex": 0,
          "key": "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14",
          "peerDeviceId": "A"
        },
        "selfParentHash": "a78884ab937e09055e931c3aec6249e8193c7c30b3d6a716971b98e2053c9f3d",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 2,
        "D": 4
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 1,
        "B": 1,
        "D": 1
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6": {
      "bodySignature": "b7584dbb2705edcac4aa9c45450b4bcf26dd8f6f37f735cf7274f731f14a1cd7",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 3,
          "key": "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 1,
          "key": "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6",
          "peerDeviceId": "C"
        },
        "otherParentHash": "bd61fa665f408a791f804f48db4679deb540e5e070bff57fe42debcddd4cb3ea",
        "selfParent": {
          "eventCreatorIndex": 2,
          "key": "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
          "peerDeviceId": "A"
        },
        "selfParentHash": "86a6459bb9f2373a5fb397627fe5131ad68749597ca9a01985933f0e51c7a17b",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 4,
        "B": 6,
        "C": 3,
        "D": 8
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 3,
        "B": 2,
        "C": 1,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8": {
      "bodySignature": "04484a7899836ba785c3af28676a5459044836a57d5f2a500ed182f54b5e9273",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 10,
          "key": "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 3,
          "key": "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
          "peerDeviceId": "C"
        },
        "otherParentHash": "c0b1600027320bddc1ef90f1549ed399d84da0f9dd749b19fa1d9e04b233c16c",
        "selfParent": {
          "eventCreatorIndex": 9,
          "key": "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
          "peerDeviceId": "D"
        },
        "selfParentHash": "b6c603442f0c24d8c246ec39a9bde4b137c4d4201b8dbc2d8fc0bc731b00b4ed",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 12,
        "C": 4,
        "D": 10
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 5,
        "B": 9,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "1d3a071aecf272a7b72d68659ffd251c94a39817614912fc97fc969725000774": {
      "bodySignature": "9a2773916b5775ccc30b711e93d8e5c2ba3ab01f594508c588493e57d7afaf24",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 17,
          "key": "1d3a071aecf272a7b72d68659ffd251c94a39817614912fc97fc969725000774",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 22,
          "key": "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855",
          "peerDeviceId": "B"
        },
        "otherParentHash": "abf5607a72e83fd106c57524a473c22b48a9d6e39b094c9fa3f0e52617b1f315",
        "selfParent": {
          "eventCreatorIndex": 16,
          "key": "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
          "peerDeviceId": "D"
        },
        "selfParentHash": "83079dc796ad1a9290b00557a2ffc701980b0b4d637849091a7c691788cb5bad",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "D": 18
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 13,
        "B": 22,
        "C": 6,
        "D": 17
      },
      "roundCreated": 6,
      "roundReceived": 8
    },
    "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0": {
      "bodySignature": "ac065284c027a7421f80702c3c0c998c8d2b1b48d148cb0d529d85962b0f1613",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 8,
          "key": "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 25,
          "key": "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
          "peerDeviceId": "B"
        },
        "otherParentHash": "296dc1e26e8020381d9c4db50630b39eca9f75a6a802a6ba419c947ef81819f0",
        "selfParent": {
          "eventCreatorIndex": 7,
          "key": "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
          "peerDeviceId": "C"
        },
        "selfParentHash": "0054fc82c8eb14c2896f3baf1de62591565d33971036976692d49bc763ab9cd5",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 16,
        "B": 28,
        "C": 10,
        "D": 19
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 15,
        "B": 25,
        "C": 8,
        "D": 18
      },
      "roundCreated": 7,
      "roundReceived": 8
    },
    "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63": {
      "bodySignature": "63bbfdc2be6d2992df8ec9e7eacac60875071890aa9fd8ebea7a8f7ddf29dc0e",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 4,
          "key": "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
          "peerDeviceId": "B"
        },
        "otherParentHash": "694e403297c502c36c6bbcf3249589a226e3469cc161445121644e31a44adf73",
        "selfParent": {
          "eventCreatorIndex": 3,
          "key": "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6",
          "peerDeviceId": "A"
        },
        "selfParentHash": "b7584dbb2705edcac4aa9c45450b4bcf26dd8f6f37f735cf7274f731f14a1cd7",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 4,
        "B": 6,
        "C": 3,
        "D": 8
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 4,
        "B": 4,
        "C": 1,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681": {
      "bodySignature": "8b4b39f1992af5a79a876eb67dc71c198791f038604b2aa3bdcf01419e2b3bf8",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 1,
          "key": "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 0,
          "key": "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
          "peerDeviceId": "B"
        },
        "otherParentHash": "b8395a581b9fa2dcd939c1cec7c30c4516b4c0de52d0e5aedc3aa1a9d1b9ed37",
        "selfParent": {
          "eventCreatorIndex": 0,
          "key": "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
          "peerDeviceId": "D"
        },
        "selfParentHash": "27445e0eec10e9e0e4454b8d08c13104a3de8d9de3a47fd9675d022eb9425bfc",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 2,
        "C": 1,
        "D": 1
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "B": 0,
        "D": 1
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6": {
      "bodySignature": "bd61fa665f408a791f804f48db4679deb540e5e070bff57fe42debcddd4cb3ea",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 1,
          "key": "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 2,
          "key": "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
          "peerDeviceId": "B"
        },
        "otherParentHash": "a281c0ea01b6fbeb5647ecf2e1ee250b671848634045e9d8858902b6c6bb45d4",
        "selfParent": {
          "eventCreatorIndex": 0,
          "key": "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
          "peerDeviceId": "C"
        },
        "selfParentHash": "2f2e0ba194f992405e81bd3cf39a6617c40d1d50a034dace1bd8dfa7900399ac",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 4,
        "B": 6,
        "C": 2
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "D": 1,
        "B": 2,
        "C": 1
      },
      "roundCreated": 0,
      "roundReceived": 2
    },
    "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56": {
      "bodySignature": "86a6459bb9f2373a5fb397627fe5131ad68749597ca9a01985933f0e51c7a17b",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 2,
          "key": "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
          "peerDeviceId": "D"
        },
        "otherParentHash": "c0dea7a627c4e4f449a200e8e7e24fb65c1983825de9860fe849283c833f9f35",
        "selfParent": {
          "eventCreatorIndex": 1,
          "key": "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648",
          "peerDeviceId": "A"
        },
        "selfParentHash": "bcbe4df273080c34fba91a209ad69c1f5964dfd441bd2bfced0972fe3b4539e8",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 4,
        "B": 6,
        "C": 3,
        "D": 8
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 2,
        "B": 2,
        "C": 0,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e": {
      "bodySignature": "b6c603442f0c24d8c246ec39a9bde4b137c4d4201b8dbc2d8fc0bc731b00b4ed",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 9,
          "key": "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 9,
          "key": "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359",
          "peerDeviceId": "B"
        },
        "otherParentHash": "2f3d19ba9c370890af844c580b94b9196acdad9d8a9ce758e2a6d31d11c8f27c",
        "selfParent": {
          "eventCreatorIndex": 8,
          "key": "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb",
          "peerDeviceId": "D"
        },
        "selfParentHash": "bbf42bc814810e0c113add9cdf71ea96bbcfb727f481f59b8b73914bfc597c07",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 12,
        "C": 4,
        "D": 10
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 5,
        "B": 9,
        "C": 3,
        "D": 9
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215": {
      "bodySignature": "b3cf41994946d6d9240c5c83b200f39bc8de1005e4f588f5c0f9836e3b090c81",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 16,
          "key": "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 9,
          "key": "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524",
          "peerDeviceId": "C"
        },
        "otherParentHash": "a034d1aca11febf230c76446a18aa6ef8800c62dd8faf38924423bea850c34c6",
        "selfParent": {
          "eventCreatorIndex": 15,
          "key": "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
          "peerDeviceId": "A"
        },
        "selfParentHash": "a74395946313557e2029a3503bbe1a93898541de07bde9ed45698e45109d8480",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 16,
        "B": 28,
        "C": 11,
        "D": 19
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 16,
        "B": 26,
        "C": 9,
        "D": 18
      },
      "roundCreated": 8,
      "roundReceived": -1
    },
    "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a": {
      "bodySignature": "a60246ec59373726664084ca42180fa8ac3cac39367f632659ca9346926ad0c4",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 10,
          "key": "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 27,
          "key": "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
          "peerDeviceId": "B"
        },
        "otherParentHash": "21cea27665c844f8a6adcd727d1fb481691b5eb3dbd79d33c82ce52070ec84b5",
        "selfParent": {
          "eventCreatorIndex": 9,
          "key": "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524",
          "peerDeviceId": "C"
        },
        "selfParentHash": "a034d1aca11febf230c76446a18aa6ef8800c62dd8faf38924423bea850c34c6",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 17,
        "B": 30,
        "C": 12,
        "D": 20
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 16,
        "B": 27,
        "C": 10,
        "D": 19
      },
      "roundCreated": 8,
      "roundReceived": -1
    },
    "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea": {
      "bodySignature": "426efc066ec89ef8cac6e16ed7a49661553bcda24c154f4f71ca33f1b74c446b",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 5,
          "key": "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 6,
          "key": "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
          "peerDeviceId": "B"
        },
        "otherParentHash": "8fcfbe194c60e8d75606b178a82f8b862480798ef650599a2dcd98997fb8319d",
        "selfParent": {
          "eventCreatorIndex": 4,
          "key": "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
          "peerDeviceId": "A"
        },
        "selfParentHash": "63bbfdc2be6d2992df8ec9e7eacac60875071890aa9fd8ebea7a8f7ddf29dc0e",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 5,
        "B": 9,
        "D": 10
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 5,
        "B": 6,
        "C": 1,
        "D": 6
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79": {
      "bodySignature": "ee5e0bb175ae6c9698f62aaca02a2bcf50df7db68b3e0576584c27acab4118f8",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 10,
          "key": "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 7,
          "key": "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
          "peerDeviceId": "A"
        },
        "otherParentHash": "cca20bb93dda7cbe0407d7ddef39d853be213e4bfa5d980c154dfc792a358c23",
        "selfParent": {
          "eventCreatorIndex": 9,
          "key": "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359",
          "peerDeviceId": "B"
        },
        "selfParentHash": "2f3d19ba9c370890af844c580b94b9196acdad9d8a9ce758e2a6d31d11c8f27c",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 12,
        "C": 5,
        "D": 12
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 7,
        "B": 10,
        "C": 3,
        "D": 8
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308": {
      "bodySignature": "49e76ca4db45b2d6a9815038bcc8fb51887f000ac57c64ea18006d9800709cea",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 13,
          "key": "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 20,
          "key": "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e",
          "peerDeviceId": "B"
        },
        "otherParentHash": "7c07a4f40b931b398ac7dcdc2ed24be2221c25bf080ad3fd1bd97f8baf18ade5",
        "selfParent": {
          "eventCreatorIndex": 12,
          "key": "91bec90d2f59a91f2e7c08d17b5334af65f58b47672600b8bdb4a44a8b0d81c8",
          "peerDeviceId": "A"
        },
        "selfParentHash": "f39c5c8ae64becdf9e490201e88cc053b45fc8d206b36fed91c33c7e6f2f07e5",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 24,
        "C": 7
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 13,
        "B": 20,
        "C": 6,
        "D": 15
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855": {
      "bodySignature": "abf5607a72e83fd106c57524a473c22b48a9d6e39b094c9fa3f0e52617b1f315",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 22,
          "key": "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 16,
          "key": "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
          "peerDeviceId": "D"
        },
        "otherParentHash": "83079dc796ad1a9290b00557a2ffc701980b0b4d637849091a7c691788cb5bad",
        "selfParent": {
          "eventCreatorIndex": 21,
          "key": "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
          "peerDeviceId": "B"
        },
        "selfParentHash": "8d02e5067cb6d45c5046efd177cf805e76a7d64450e0a30b4a4bb5f1f2f74d63",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 18
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 13,
        "B": 22,
        "C": 6,
        "D": 16
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934": {
      "bodySignature": "60e0bfc3b7e595ed128bd6c00705b665f815c96ecf97df1ab3a42da4566713c1",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 3,
          "key": "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 2,
          "key": "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
          "peerDeviceId": "B"
        },
        "otherParentHash": "a281c0ea01b6fbeb5647ecf2e1ee250b671848634045e9d8858902b6c6bb45d4",
        "selfParent": {
          "eventCreatorIndex": 2,
          "key": "2265f5336d7b6037b5b75ace727a6c482c37ae963dad3bd8eff402314e8548ab",
          "peerDeviceId": "D"
        },
        "selfParentHash": "cf5e521ec88c69bfd758eb7a8f5037faa3b6f18c3b41c7773922809d52342dc4",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "D": 4
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "B": 2,
        "C": 0,
        "D": 3
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b": {
      "bodySignature": "c65458629bd0aed13340bf9870fe9d5b6992dcb1d496c6bdb3c809b3325ad59e",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 24,
          "key": "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 14,
          "key": "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
          "peerDeviceId": "A"
        },
        "otherParentHash": "6253e2cdb748f08d7fac7166e36576a608486f6b117c7bc898b79ba9058e18fa",
        "selfParent": {
          "eventCreatorIndex": 23,
          "key": "04ee0df547e7f6a0c65d15af049d47420008eafb8df8e37452d934c8e2499f14",
          "peerDeviceId": "B"
        },
        "selfParentHash": "797e1f392d1d665b34fd4133b47b38d31d5c3482c6469fdb39e1f8b2d69e1a71",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 18
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 14,
        "B": 24,
        "C": 6,
        "D": 16
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024": {
      "bodySignature": "d5e840b39b4b6a80099d689911c6223716f5c4d813b5922a481c5ad270552bd4",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 19,
          "key": "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 11,
          "key": "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
          "peerDeviceId": "A"
        },
        "otherParentHash": "ceac2b2e3545b1bd388e4982c603eed3b023dace8d698484acf5a0b3c378159f",
        "selfParent": {
          "eventCreatorIndex": 18,
          "key": "00ceeab4df7002aad9c625c69e81c47d07f71027ad3600787a73c7e91fdf8d61",
          "peerDeviceId": "B"
        },
        "selfParentHash": "68dd820ec128de7f4ee6e02c079eef69db7257c27c193e2f3fe0d1d309ae849a",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 21,
        "D": 16
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 11,
        "B": 19,
        "C": 5,
        "D": 13
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd": {
      "bodySignature": "6f9679e69ed1a8438f61047c46f6f1b8d94ea270e92411203ced43bb4c25a196",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 12,
          "key": "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6",
          "peerDeviceId": "C"
        },
        "otherParentHash": "4f5ed15fc344de48998fed78cb3dec182bd067cbc163ba7549556bdbed66fdad",
        "selfParent": {
          "eventCreatorIndex": 11,
          "key": "a7dc9aa658db149b641d28252d72e0b081504170be70b919c22bcefc43e5b33c",
          "peerDeviceId": "D"
        },
        "selfParentHash": "e6601072723a554da4dcb8481855fd91315f8875f4701aa6cbf3712d7fb71b54",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 10,
        "B": 17,
        "C": 5,
        "D": 12
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 7,
        "B": 12,
        "C": 4,
        "D": 12
      },
      "roundCreated": 4,
      "roundReceived": 5
    },
    "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14": {
      "bodySignature": "6253e2cdb748f08d7fac7166e36576a608486f6b117c7bc898b79ba9058e18fa",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 14,
          "key": "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 6,
          "key": "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
          "peerDeviceId": "C"
        },
        "otherParentHash": "edfab87ae5bd096d6184db50c2324aff5068b87249f330d2e109dc53ec5b0c88",
        "selfParent": {
          "eventCreatorIndex": 13,
          "key": "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
          "peerDeviceId": "A"
        },
        "selfParentHash": "49e76ca4db45b2d6a9815038bcc8fb51887f000ac57c64ea18006d9800709cea",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 24,
        "C": 7
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 14,
        "B": 20,
        "C": 6,
        "D": 15
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "04ee0df547e7f6a0c65d15af049d47420008eafb8df8e37452d934c8e2499f14": {
      "bodySignature": "797e1f392d1d665b34fd4133b47b38d31d5c3482c6469fdb39e1f8b2d69e1a71",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 23,
          "key": "04ee0df547e7f6a0c65d15af049d47420008eafb8df8e37452d934c8e2499f14",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 14,
          "key": "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
          "peerDeviceId": "A"
        },
        "otherParentHash": "6253e2cdb748f08d7fac7166e36576a608486f6b117c7bc898b79ba9058e18fa",
        "selfParent": {
          "eventCreatorIndex": 22,
          "key": "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855",
          "peerDeviceId": "B"
        },
        "selfParentHash": "abf5607a72e83fd106c57524a473c22b48a9d6e39b094c9fa3f0e52617b1f315",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 18
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 14,
        "B": 23,
        "C": 6,
        "D": 16
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44": {
      "bodySignature": "5693488ac47298983fb5f84436169df0c78a7452256e39466f6bb50d5adb6afb",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 19,
          "key": "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 16,
          "key": "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
          "peerDeviceId": "A"
        },
        "otherParentHash": "b3cf41994946d6d9240c5c83b200f39bc8de1005e4f588f5c0f9836e3b090c81",
        "selfParent": {
          "eventCreatorIndex": 18,
          "key": "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
          "peerDeviceId": "D"
        },
        "selfParentHash": "534f0480f75ad211c373a7ab291bf528a6bc893b503c1e79c446c351dbc6993d",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 17,
        "B": 28,
        "C": 11,
        "D": 19
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 16,
        "B": 26,
        "C": 9,
        "D": 19
      },
      "roundCreated": 8,
      "roundReceived": -1
    },
    "fafc221218d3b700c520f88d2d25775cd5135fa3964607b547671c197e990465": {
      "bodySignature": "eba5a09204d969ea7ad0fc7c4ec7a83b1b8291b43af228867a6151fd5f4efaa4",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 14,
          "key": "fafc221218d3b700c520f88d2d25775cd5135fa3964607b547671c197e990465",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 31,
          "key": "5eb00cfd65e6c6c1ae30f9a19426b50a9f3a89bddd63d7e0cc662c15c12c6ebf",
          "peerDeviceId": "B"
        },
        "otherParentHash": "28683b6582cbd835f126ae2186e0075701003c52597cd84c0a0268f6657cf33a",
        "selfParent": {
          "eventCreatorIndex": 13,
          "key": "6645ca87da6316d5bb2b8e48f6d382c9ffff5a74966c81debc183dc6bb84130d",
          "peerDeviceId": "C"
        },
        "selfParentHash": "5faffed1433fbed44fd20361994c4d5209056a8f8aa5f146f82bb921b3d6d256",
        "timestamp": 1641661517,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "C": 14
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 18,
        "B": 31,
        "C": 14,
        "D": 21
      },
      "roundCreated": 10,
      "roundReceived": -1
    },
    "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561": {
      "bodySignature": "a281c0ea01b6fbeb5647ecf2e1ee250b671848634045e9d8858902b6c6bb45d4",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 2,
          "key": "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 0,
          "key": "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
          "peerDeviceId": "C"
        },
        "otherParentHash": "2f2e0ba194f992405e81bd3cf39a6617c40d1d50a034dace1bd8dfa7900399ac",
        "selfParent": {
          "eventCreatorIndex": 1,
          "key": "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
          "peerDeviceId": "B"
        },
        "selfParentHash": "d2b8b2ac46bcb1a0cc23a863ee4f13902270d8b58ef128cfc74508ac1bc49684",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 3,
        "B": 2,
        "C": 2,
        "D": 4
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "B": 2,
        "C": 0,
        "D": 1
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5": {
      "bodySignature": "90e25b4f320d2fc657330bda5348795d9fce3bfb0b9a5d8afdfb5999a25da714",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 10,
          "key": "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 15,
          "key": "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
          "peerDeviceId": "B"
        },
        "otherParentHash": "de432dfe38ebe55085fa4858c5a92998e4498dc2110a2d617c05a0984459ebcc",
        "selfParent": {
          "eventCreatorIndex": 9,
          "key": "06663975f75f189f1d70bd14d8f22df264cd6a5c7575d6875183d0ec76432fbb",
          "peerDeviceId": "A"
        },
        "selfParentHash": "2b0149b06c55ddca32750342dc164df9624df4bd1ab7c848b95e322f1a62983d",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 10,
        "B": 17,
        "C": 6,
        "D": 15
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 10,
        "B": 15,
        "C": 5,
        "D": 12
      },
      "roundCreated": 4,
      "roundReceived": 5
    },
    "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23": {
      "bodySignature": "a137eb02f7b5a27cfeb6f2665028a70bf77abc92da0cdc1b0cf907aae3a5ecb2",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 5,
          "key": "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 12,
          "key": "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
          "peerDeviceId": "D"
        },
        "otherParentHash": "6f9679e69ed1a8438f61047c46f6f1b8d94ea270e92411203ced43bb4c25a196",
        "selfParent": {
          "eventCreatorIndex": 4,
          "key": "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6",
          "peerDeviceId": "C"
        },
        "selfParentHash": "4f5ed15fc344de48998fed78cb3dec182bd067cbc163ba7549556bdbed66fdad",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 10,
        "B": 17,
        "C": 6,
        "D": 15
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 7,
        "B": 12,
        "C": 5,
        "D": 12
      },
      "roundCreated": 4,
      "roundReceived": 5
    },
    "22b5894e02a73bb5dee8ae7db1fc6f2502052c6da5c20d77612682022bd4bdae": {
      "bodySignature": "5a884e182fd47d290ac6b056a18370495a54859b16d1c4d333ef252c4c0517eb",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 11,
          "key": "22b5894e02a73bb5dee8ae7db1fc6f2502052c6da5c20d77612682022bd4bdae",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 28,
          "key": "8abdf1580603d91a8e255690a4b7381a36aff7b0c4c0c6589831ddf165aca75c",
          "peerDeviceId": "B"
        },
        "otherParentHash": "6d77750ce95e1648e99febabf90e793cc5c7a033f968fdfcf14483cdd1b1ff63",
        "selfParent": {
          "eventCreatorIndex": 10,
          "key": "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a",
          "peerDeviceId": "C"
        },
        "selfParentHash": "a60246ec59373726664084ca42180fa8ac3cac39367f632659ca9346926ad0c4",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 17,
        "B": 30,
        "C": 12,
        "D": 20
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 16,
        "B": 28,
        "C": 11,
        "D": 19
      },
      "roundCreated": 8,
      "roundReceived": -1
    },
    "8abdf1580603d91a8e255690a4b7381a36aff7b0c4c0c6589831ddf165aca75c": {
      "bodySignature": "6d77750ce95e1648e99febabf90e793cc5c7a033f968fdfcf14483cdd1b1ff63",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 28,
          "key": "8abdf1580603d91a8e255690a4b7381a36aff7b0c4c0c6589831ddf165aca75c",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 16,
          "key": "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
          "peerDeviceId": "A"
        },
        "otherParentHash": "b3cf41994946d6d9240c5c83b200f39bc8de1005e4f588f5c0f9836e3b090c81",
        "selfParent": {
          "eventCreatorIndex": 27,
          "key": "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
          "peerDeviceId": "B"
        },
        "selfParentHash": "21cea27665c844f8a6adcd727d1fb481691b5eb3dbd79d33c82ce52070ec84b5",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 17,
        "B": 28,
        "C": 11,
        "D": 20
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 16,
        "B": 28,
        "C": 9,
        "D": 19
      },
      "roundCreated": 8,
      "roundReceived": -1
    },
    "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb": {
      "bodySignature": "bbf42bc814810e0c113add9cdf71ea96bbcfb727f481f59b8b73914bfc597c07",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 8,
          "key": "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 2,
          "key": "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
          "peerDeviceId": "C"
        },
        "otherParentHash": "22f19b46c7c817e5ff0003c321eaf7350b9740289b1ccff9e568b43736f5e7a6",
        "selfParent": {
          "eventCreatorIndex": 7,
          "key": "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
          "peerDeviceId": "D"
        },
        "selfParentHash": "78f8c90478cfbd0376c00746abe248ba5e28d7714a4a9175e249c07f5a7e952b",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "C": 3,
        "D": 8
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 4,
        "B": 6,
        "C": 2,
        "D": 8
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21": {
      "bodySignature": "b8395a581b9fa2dcd939c1cec7c30c4516b4c0de52d0e5aedc3aa1a9d1b9ed37",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 0,
          "key": "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
          "peerDeviceId": "B"
        },
        "timestamp": 1641661514,
        "transactions": []
      },
      "firstDiscendants": {
        "A": 3,
        "B": 2,
        "C": 2,
        "D": 4
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "B": 0
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019": {
      "bodySignature": "10f1f621f8d9ad99a7a317f9bcd757315f23fb15d019f8e48ee0b1f3032b1141",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 12,
          "key": "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 10,
          "key": "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
          "peerDeviceId": "D"
        },
        "otherParentHash": "04484a7899836ba785c3af28676a5459044836a57d5f2a500ed182f54b5e9273",
        "selfParent": {
          "eventCreatorIndex": 11,
          "key": "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a",
          "peerDeviceId": "B"
        },
        "selfParentHash": "b06ddb9f90707e396f43d7171179e77e7f6b11300d24434106644038151d6789",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 12,
        "C": 5,
        "D": 12
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 7,
        "B": 12,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e": {
      "bodySignature": "21cea27665c844f8a6adcd727d1fb481691b5eb3dbd79d33c82ce52070ec84b5",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 27,
          "key": "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 19,
          "key": "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
          "peerDeviceId": "D"
        },
        "otherParentHash": "5693488ac47298983fb5f84436169df0c78a7452256e39466f6bb50d5adb6afb",
        "selfParent": {
          "eventCreatorIndex": 26,
          "key": "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85",
          "peerDeviceId": "B"
        },
        "selfParentHash": "22c0e532a8783d107fc60d749985ab667d7bf293769d33c9ac62b82644ad2d5c",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 17,
        "B": 28,
        "C": 11,
        "D": 20
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 16,
        "B": 27,
        "C": 9,
        "D": 19
      },
      "roundCreated": 8,
      "roundReceived": -1
    },
    "0cd20d37dbaa799d1d2f6f04adbab0b9e958b083f38e06512cdefadd20863f98": {
      "bodySignature": "a28524fcd4b22424ed7f46c58cba876e3f794f3c136faeb463472db1351cdd01",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 3,
          "key": "0cd20d37dbaa799d1d2f6f04adbab0b9e958b083f38e06512cdefadd20863f98",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 3,
          "key": "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934",
          "peerDeviceId": "D"
        },
        "otherParentHash": "60e0bfc3b7e595ed128bd6c00705b665f815c96ecf97df1ab3a42da4566713c1",
        "selfParent": {
          "eventCreatorIndex": 2,
          "key": "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
          "peerDeviceId": "B"
        },
        "selfParentHash": "a281c0ea01b6fbeb5647ecf2e1ee250b671848634045e9d8858902b6c6bb45d4",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 4
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "B": 3,
        "C": 0,
        "D": 3
      },
      "roundCreated": 0,
      "roundReceived": 2
    },
    "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5": {
      "bodySignature": "ceac2b2e3545b1bd388e4982c603eed3b023dace8d698484acf5a0b3c378159f",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 11,
          "key": "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 17,
          "key": "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
          "peerDeviceId": "B"
        },
        "otherParentHash": "edd2f8d2b43a0928ed840c328760627dfa501a1c4021567d33b51432efd8da28",
        "selfParent": {
          "eventCreatorIndex": 10,
          "key": "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5",
          "peerDeviceId": "A"
        },
        "selfParentHash": "90e25b4f320d2fc657330bda5348795d9fce3bfb0b9a5d8afdfb5999a25da714",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 11,
        "B": 20,
        "D": 16
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 11,
        "B": 17,
        "C": 5,
        "D": 13
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "6645ca87da6316d5bb2b8e48f6d382c9ffff5a74966c81debc183dc6bb84130d": {
      "bodySignature": "5faffed1433fbed44fd20361994c4d5209056a8f8aa5f146f82bb921b3d6d256",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 13,
          "key": "6645ca87da6316d5bb2b8e48f6d382c9ffff5a74966c81debc183dc6bb84130d",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 30,
          "key": "726a2749e243fa32b5dbbbcde1ff60642830a8a6f7afba55458ac681a6908461",
          "peerDeviceId": "B"
        },
        "otherParentHash": "5bc8b3fc7893f4c7dd6b027ebdd40dcc9aabc0d58acad70b6d6f0fb75c0f2b01",
        "selfParent": {
          "eventCreatorIndex": 12,
          "key": "fa70213c8aaf9d8fdd6d9377a388260efb452ec9f6afadb591d7ca6782cb9a57",
          "peerDeviceId": "C"
        },
        "selfParentHash": "51723dc5c24f027a7b139fc1f7d6fe0de64f8a41f20aac259bc0045d2d55d462",
        "timestamp": 1641661517,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 18,
        "B": 31,
        "C": 14,
        "D": 21
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 17,
        "B": 30,
        "C": 13,
        "D": 20
      },
      "roundCreated": 9,
      "roundReceived": -1
    },
    "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2": {
      "bodySignature": "0054fc82c8eb14c2896f3baf1de62591565d33971036976692d49bc763ab9cd5",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 7,
          "key": "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 24,
          "key": "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b",
          "peerDeviceId": "B"
        },
        "otherParentHash": "c65458629bd0aed13340bf9870fe9d5b6992dcb1d496c6bdb3c809b3325ad59e",
        "selfParent": {
          "eventCreatorIndex": 6,
          "key": "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
          "peerDeviceId": "C"
        },
        "selfParentHash": "edfab87ae5bd096d6184db50c2324aff5068b87249f330d2e109dc53ec5b0c88",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 26,
        "C": 8,
        "D": 18
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 14,
        "B": 24,
        "C": 7,
        "D": 16
      },
      "roundCreated": 6,
      "roundReceived": 7
    },
    "d210ba50f39c0d38f61379d30c99f31cc7b3af39b7aa19320394f504fb3a40a5": {
      "bodySignature": "18b8c58db4ac08d8679fa3546a5d7fa8ee9d16407ed40f5e47a2762236cbc8c8",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 29,
          "key": "d210ba50f39c0d38f61379d30c99f31cc7b3af39b7aa19320394f504fb3a40a5",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 20,
          "key": "422446d7512f61f772230f96c25069087be68c6ec57af8e1f18be7a9fad55375",
          "peerDeviceId": "D"
        },
        "otherParentHash": "5439f97f725f1370a2cb1d8fe19ec825f9b2ec0dd9aa016e5bcefcc374522640",
        "selfParent": {
          "eventCreatorIndex": 28,
          "key": "8abdf1580603d91a8e255690a4b7381a36aff7b0c4c0c6589831ddf165aca75c",
          "peerDeviceId": "B"
        },
        "selfParentHash": "6d77750ce95e1648e99febabf90e793cc5c7a033f968fdfcf14483cdd1b1ff63",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 18,
        "B": 30,
        "C": 13,
        "D": 21
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 17,
        "B": 29,
        "C": 11,
        "D": 20
      },
      "roundCreated": 9,
      "roundReceived": -1
    },
    "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1": {
      "bodySignature": "edd2f8d2b43a0928ed840c328760627dfa501a1c4021567d33b51432efd8da28",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 17,
          "key": "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 13,
          "key": "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f",
          "peerDeviceId": "D"
        },
        "otherParentHash": "2b3713a0f6209a1d14b8ec8356e8c7a67be588488dec2dd13dffb8c5cee8f1b7",
        "selfParent": {
          "eventCreatorIndex": 16,
          "key": "bc215963d1a424a5f9707d565f07a5bcf79e19cde17372a9a6a914cd986f7fc9",
          "peerDeviceId": "B"
        },
        "selfParentHash": "95593643a9d4ab78098772143d8c035d004cfeb8cc08488efe2e8b77650796dc",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "B": 17,
        "C": 6,
        "D": 16
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 10,
        "B": 17,
        "C": 5,
        "D": 13
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38": {
      "bodySignature": "8fcfbe194c60e8d75606b178a82f8b862480798ef650599a2dcd98997fb8319d",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 6,
          "key": "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 6,
          "key": "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4",
          "peerDeviceId": "D"
        },
        "otherParentHash": "18d68dfa4cb0e082ef772a5bfbde7bbdfdebe2dfc7a1b226b6f1e44431b1e061",
        "selfParent": {
          "eventCreatorIndex": 5,
          "key": "5ba2c833c5d65e649e4b4fa4d426223f3300650f874e32c4451d9346ce6469e2",
          "peerDeviceId": "B"
        },
        "selfParentHash": "562a91837c9922cf666b2e29b7653a909aa801688c332b528d1ed4ce28aa0af6",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "B": 6,
        "C": 3,
        "D": 10
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 4,
        "B": 6,
        "C": 1,
        "D": 6
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc": {
      "bodySignature": "c621ca66d1528315b1571404a6692d2719d80efb4c48797f81a64605fbef1e27",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 17,
          "key": "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 11,
          "key": "22b5894e02a73bb5dee8ae7db1fc6f2502052c6da5c20d77612682022bd4bdae",
          "peerDeviceId": "C"
        },
        "otherParentHash": "5a884e182fd47d290ac6b056a18370495a54859b16d1c4d333ef252c4c0517eb",
        "selfParent": {
          "eventCreatorIndex": 16,
          "key": "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
          "peerDeviceId": "A"
        },
        "selfParentHash": "b3cf41994946d6d9240c5c83b200f39bc8de1005e4f588f5c0f9836e3b090c81",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 17,
        "B": 30,
        "C": 13,
        "D": 20
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 17,
        "B": 28,
        "C": 11,
        "D": 19
      },
      "roundCreated": 9,
      "roundReceived": -1
    },
    "f86ae46d947e2215ce53b1ae840af949b5f686e69ea2f6b7eaf3725619d4303e": {
      "bodySignature": "8bb60580f4f40f89959cd66bfe2da75c4db1a677163d8f329f6b8b3e4733b377",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 7,
          "key": "f86ae46d947e2215ce53b1ae840af949b5f686e69ea2f6b7eaf3725619d4303e",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 5,
          "key": "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
          "peerDeviceId": "A"
        },
        "otherParentHash": "426efc066ec89ef8cac6e16ed7a49661553bcda24c154f4f71ca33f1b74c446b",
        "selfParent": {
          "eventCreatorIndex": 6,
          "key": "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
          "peerDeviceId": "B"
        },
        "selfParentHash": "8fcfbe194c60e8d75606b178a82f8b862480798ef650599a2dcd98997fb8319d",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "B": 10,
        "D": 10
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 5,
        "B": 7,
        "C": 1,
        "D": 6
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "fa267bb037d77a0599298151783319ce7a4ff032983503ee466717e814e43207": {
      "bodySignature": "65dda2c8f64c6e84df64e56f6d5aced75fc11a5620e46cc6bd94d22dc63e5742",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 21,
          "key": "fa267bb037d77a0599298151783319ce7a4ff032983503ee466717e814e43207",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 18,
          "key": "5985f6f8353e299ba80dec0a569d2757f733a25567a6a4f38f5f102770495ae6",
          "peerDeviceId": "A"
        },
        "otherParentHash": "376a3e732eb3839637acefedf2c73d2475abe32fb9d7dd6e808312b12e6518db",
        "selfParent": {
          "eventCreatorIndex": 20,
          "key": "422446d7512f61f772230f96c25069087be68c6ec57af8e1f18be7a9fad55375",
          "peerDeviceId": "D"
        },
        "selfParentHash": "5439f97f725f1370a2cb1d8fe19ec825f9b2ec0dd9aa016e5bcefcc374522640",
        "timestamp": 1641661517,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 31,
        "C": 14,
        "D": 21
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 18,
        "B": 30,
        "C": 13,
        "D": 21
      },
      "roundCreated": 10,
      "roundReceived": -1
    },
    "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f": {
      "bodySignature": "64e4994b05364f5393515305175dd2c29b3fdd7d8cfc66bc37b87331ac1093bd",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 8,
          "key": "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 12,
          "key": "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
          "peerDeviceId": "B"
        },
        "otherParentHash": "10f1f621f8d9ad99a7a317f9bcd757315f23fb15d019f8e48ee0b1f3032b1141",
        "selfParent": {
          "eventCreatorIndex": 7,
          "key": "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
          "peerDeviceId": "A"
        },
        "selfParentHash": "cca20bb93dda7cbe0407d7ddef39d853be213e4bfa5d980c154dfc792a358c23",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 8,
        "B": 15,
        "D": 13
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 8,
        "B": 12,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 5
    },
    "726a2749e243fa32b5dbbbcde1ff60642830a8a6f7afba55458ac681a6908461": {
      "bodySignature": "5bc8b3fc7893f4c7dd6b027ebdd40dcc9aabc0d58acad70b6d6f0fb75c0f2b01",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 30,
          "key": "726a2749e243fa32b5dbbbcde1ff60642830a8a6f7afba55458ac681a6908461",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 17,
          "key": "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc",
          "peerDeviceId": "A"
        },
        "otherParentHash": "c621ca66d1528315b1571404a6692d2719d80efb4c48797f81a64605fbef1e27",
        "selfParent": {
          "eventCreatorIndex": 29,
          "key": "d210ba50f39c0d38f61379d30c99f31cc7b3af39b7aa19320394f504fb3a40a5",
          "peerDeviceId": "B"
        },
        "selfParentHash": "18b8c58db4ac08d8679fa3546a5d7fa8ee9d16407ed40f5e47a2762236cbc8c8",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 18,
        "B": 30,
        "C": 13,
        "D": 21
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 17,
        "B": 30,
        "C": 11,
        "D": 20
      },
      "roundCreated": 9,
      "roundReceived": -1
    },
    "12a750139ca2e4c14287bb6ed9ece9ee75b556a911f19f91c2f0d59ef40e7597": {
      "bodySignature": "f1cb1707110eb15e02b7178a0f86d7dd8db1b5ec90cc0b1dc4d58546bd84d393",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 5,
          "key": "12a750139ca2e4c14287bb6ed9ece9ee75b556a911f19f91c2f0d59ef40e7597",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 4,
          "key": "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
          "peerDeviceId": "B"
        },
        "otherParentHash": "694e403297c502c36c6bbcf3249589a226e3469cc161445121644e31a44adf73",
        "selfParent": {
          "eventCreatorIndex": 4,
          "key": "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
          "peerDeviceId": "D"
        },
        "selfParentHash": "c0dea7a627c4e4f449a200e8e7e24fb65c1983825de9860fe849283c833f9f35",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 6,
        "D": 7
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 1,
        "B": 4,
        "C": 0,
        "D": 5
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359": {
      "bodySignature": "2f3d19ba9c370890af844c580b94b9196acdad9d8a9ce758e2a6d31d11c8f27c",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 9,
          "key": "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 3,
          "key": "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
          "peerDeviceId": "C"
        },
        "otherParentHash": "c0b1600027320bddc1ef90f1549ed399d84da0f9dd749b19fa1d9e04b233c16c",
        "selfParent": {
          "eventCreatorIndex": 8,
          "key": "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75",
          "peerDeviceId": "B"
        },
        "selfParentHash": "bb60ed2e8e5bc0e77be860bc4cbcded8535107d8e3834951f8e276f74045952b",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "B": 10,
        "D": 10
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 5,
        "B": 9,
        "C": 3,
        "D": 8
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb": {
      "bodySignature": "22f19b46c7c817e5ff0003c321eaf7350b9740289b1ccff9e568b43736f5e7a6",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 2,
          "key": "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 3,
          "key": "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6",
          "peerDeviceId": "A"
        },
        "otherParentHash": "b7584dbb2705edcac4aa9c45450b4bcf26dd8f6f37f735cf7274f731f14a1cd7",
        "selfParent": {
          "eventCreatorIndex": 1,
          "key": "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6",
          "peerDeviceId": "C"
        },
        "selfParentHash": "bd61fa665f408a791f804f48db4679deb540e5e070bff57fe42debcddd4cb3ea",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "C": 3,
        "D": 8
      },
      "isDecided": true,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 3,
        "B": 2,
        "C": 2,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 3
    },
    "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293": {
      "bodySignature": "a74395946313557e2029a3503bbe1a93898541de07bde9ed45698e45109d8480",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 15,
          "key": "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 7,
          "key": "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
          "peerDeviceId": "C"
        },
        "otherParentHash": "0054fc82c8eb14c2896f3baf1de62591565d33971036976692d49bc763ab9cd5",
        "selfParent": {
          "eventCreatorIndex": 14,
          "key": "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
          "peerDeviceId": "A"
        },
        "selfParentHash": "6253e2cdb748f08d7fac7166e36576a608486f6b117c7bc898b79ba9058e18fa",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 15,
        "B": 26,
        "C": 9,
        "D": 18
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 16
      },
      "roundCreated": 7,
      "roundReceived": 8
    },
    "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e": {
      "bodySignature": "78f8c90478cfbd0376c00746abe248ba5e28d7714a4a9175e249c07f5a7e952b",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 7,
          "key": "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 6,
          "key": "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
          "peerDeviceId": "B"
        },
        "otherParentHash": "8fcfbe194c60e8d75606b178a82f8b862480798ef650599a2dcd98997fb8319d",
        "selfParent": {
          "eventCreatorIndex": 6,
          "key": "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4",
          "peerDeviceId": "D"
        },
        "selfParentHash": "18d68dfa4cb0e082ef772a5bfbde7bbdfdebe2dfc7a1b226b6f1e44431b1e061",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "C": 3,
        "D": 8
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 4,
        "B": 6,
        "C": 1,
        "D": 7
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "bc215963d1a424a5f9707d565f07a5bcf79e19cde17372a9a6a914cd986f7fc9": {
      "bodySignature": "95593643a9d4ab78098772143d8c035d004cfeb8cc08488efe2e8b77650796dc",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 16,
          "key": "bc215963d1a424a5f9707d565f07a5bcf79e19cde17372a9a6a914cd986f7fc9",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 10,
          "key": "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5",
          "peerDeviceId": "A"
        },
        "otherParentHash": "90e25b4f320d2fc657330bda5348795d9fce3bfb0b9a5d8afdfb5999a25da714",
        "selfParent": {
          "eventCreatorIndex": 15,
          "key": "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
          "peerDeviceId": "B"
        },
        "selfParentHash": "de432dfe38ebe55085fa4858c5a92998e4498dc2110a2d617c05a0984459ebcc",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 17
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 10,
        "B": 16,
        "C": 5,
        "D": 12
      },
      "roundCreated": 4,
      "roundReceived": 5
    },
    "06663975f75f189f1d70bd14d8f22df264cd6a5c7575d6875183d0ec76432fbb": {
      "bodySignature": "2b0149b06c55ddca32750342dc164df9624df4bd1ab7c848b95e322f1a62983d",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 9,
          "key": "06663975f75f189f1d70bd14d8f22df264cd6a5c7575d6875183d0ec76432fbb",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 14,
          "key": "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c",
          "peerDeviceId": "B"
        },
        "otherParentHash": "677ffb4fac601c6b4c21a07ca9ea72532b30e353c4cfbee6ec0036e4770e6ae8",
        "selfParent": {
          "eventCreatorIndex": 8,
          "key": "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
          "peerDeviceId": "A"
        },
        "selfParentHash": "64e4994b05364f5393515305175dd2c29b3fdd7d8cfc66bc37b87331ac1093bd",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 10
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 9,
        "B": 14,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 5
    },
    "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b": {
      "bodySignature": "2f2e0ba194f992405e81bd3cf39a6617c40d1d50a034dace1bd8dfa7900399ac",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 0,
          "key": "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
          "peerDeviceId": "C"
        },
        "timestamp": 1641661514,
        "transactions": []
      },
      "firstDiscendants": {
        "A": 4,
        "B": 6,
        "C": 2,
        "D": 4
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "C": 0
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75": {
      "bodySignature": "bb60ed2e8e5bc0e77be860bc4cbcded8535107d8e3834951f8e276f74045952b",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 8,
          "key": "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 5,
          "key": "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
          "peerDeviceId": "A"
        },
        "otherParentHash": "426efc066ec89ef8cac6e16ed7a49661553bcda24c154f4f71ca33f1b74c446b",
        "selfParent": {
          "eventCreatorIndex": 7,
          "key": "f86ae46d947e2215ce53b1ae840af949b5f686e69ea2f6b7eaf3725619d4303e",
          "peerDeviceId": "B"
        },
        "selfParentHash": "8bb60580f4f40f89959cd66bfe2da75c4db1a677163d8f329f6b8b3e4733b377",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7,
        "B": 10,
        "D": 10
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 5,
        "B": 8,
        "C": 1,
        "D": 6
      },
      "roundCreated": 2,
      "roundReceived": 3
    },
    "5eb00cfd65e6c6c1ae30f9a19426b50a9f3a89bddd63d7e0cc662c15c12c6ebf": {
      "bodySignature": "28683b6582cbd835f126ae2186e0075701003c52597cd84c0a0268f6657cf33a",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 31,
          "key": "5eb00cfd65e6c6c1ae30f9a19426b50a9f3a89bddd63d7e0cc662c15c12c6ebf",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 21,
          "key": "fa267bb037d77a0599298151783319ce7a4ff032983503ee466717e814e43207",
          "peerDeviceId": "D"
        },
        "otherParentHash": "65dda2c8f64c6e84df64e56f6d5aced75fc11a5620e46cc6bd94d22dc63e5742",
        "selfParent": {
          "eventCreatorIndex": 30,
          "key": "726a2749e243fa32b5dbbbcde1ff60642830a8a6f7afba55458ac681a6908461",
          "peerDeviceId": "B"
        },
        "selfParentHash": "5bc8b3fc7893f4c7dd6b027ebdd40dcc9aabc0d58acad70b6d6f0fb75c0f2b01",
        "timestamp": 1641661517,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 31,
        "C": 14
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 18,
        "B": 31,
        "C": 13,
        "D": 21
      },
      "roundCreated": 10,
      "roundReceived": -1
    },
    "422446d7512f61f772230f96c25069087be68c6ec57af8e1f18be7a9fad55375": {
      "bodySignature": "5439f97f725f1370a2cb1d8fe19ec825f9b2ec0dd9aa016e5bcefcc374522640",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 20,
          "key": "422446d7512f61f772230f96c25069087be68c6ec57af8e1f18be7a9fad55375",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 17,
          "key": "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc",
          "peerDeviceId": "A"
        },
        "otherParentHash": "c621ca66d1528315b1571404a6692d2719d80efb4c48797f81a64605fbef1e27",
        "selfParent": {
          "eventCreatorIndex": 19,
          "key": "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
          "peerDeviceId": "D"
        },
        "selfParentHash": "5693488ac47298983fb5f84436169df0c78a7452256e39466f6bb50d5adb6afb",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 18,
        "B": 30,
        "C": 13,
        "D": 20
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 17,
        "B": 28,
        "C": 11,
        "D": 20
      },
      "roundCreated": 9,
      "roundReceived": -1
    },
    "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85": {
      "bodySignature": "22c0e532a8783d107fc60d749985ab667d7bf293769d33c9ac62b82644ad2d5c",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 26,
          "key": "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 15,
          "key": "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
          "peerDeviceId": "A"
        },
        "otherParentHash": "a74395946313557e2029a3503bbe1a93898541de07bde9ed45698e45109d8480",
        "selfParent": {
          "eventCreatorIndex": 25,
          "key": "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
          "peerDeviceId": "B"
        },
        "selfParentHash": "296dc1e26e8020381d9c4db50630b39eca9f75a6a802a6ba419c947ef81819f0",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 16,
        "B": 26,
        "C": 9,
        "D": 19
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 15,
        "B": 26,
        "C": 7,
        "D": 18
      },
      "roundCreated": 7,
      "roundReceived": 8
    },
    "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9": {
      "bodySignature": "534f0480f75ad211c373a7ab291bf528a6bc893b503c1e79c446c351dbc6993d",
      "consensusTimestamp": 1641661516,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 18,
          "key": "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 15,
          "key": "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
          "peerDeviceId": "A"
        },
        "otherParentHash": "a74395946313557e2029a3503bbe1a93898541de07bde9ed45698e45109d8480",
        "selfParent": {
          "eventCreatorIndex": 17,
          "key": "1d3a071aecf272a7b72d68659ffd251c94a39817614912fc97fc969725000774",
          "peerDeviceId": "D"
        },
        "selfParentHash": "9a2773916b5775ccc30b711e93d8e5c2ba3ab01f594508c588493e57d7afaf24",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 16,
        "B": 26,
        "C": 9,
        "D": 18
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 15,
        "B": 24,
        "C": 7,
        "D": 18
      },
      "roundCreated": 7,
      "roundReceived": 8
    },
    "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32": {
      "bodySignature": "27445e0eec10e9e0e4454b8d08c13104a3de8d9de3a47fd9675d022eb9425bfc",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 0,
          "key": "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
          "peerDeviceId": "D"
        },
        "timestamp": 1641661514,
        "transactions": []
      },
      "firstDiscendants": {
        "B": 2,
        "C": 1,
        "D": 1
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "D": 0
      },
      "roundCreated": 0,
      "roundReceived": 1
    },
    "d94791a85f88d5f49c3cc06d5557316cf743d60149820c594f389a1b301ff021": {
      "bodySignature": "e94c54c6e016be7de03582659a4ea469f3e65913bd28c88bb111fde371c17152",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 6,
          "key": "d94791a85f88d5f49c3cc06d5557316cf743d60149820c594f389a1b301ff021",
          "peerDeviceId": "A"
        },
        "otherParent": {
          "eventCreatorIndex": 8,
          "key": "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75",
          "peerDeviceId": "B"
        },
        "otherParentHash": "bb60ed2e8e5bc0e77be860bc4cbcded8535107d8e3834951f8e276f74045952b",
        "selfParent": {
          "eventCreatorIndex": 5,
          "key": "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
          "peerDeviceId": "A"
        },
        "selfParentHash": "426efc066ec89ef8cac6e16ed7a49661553bcda24c154f4f71ca33f1b74c446b",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 7
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 6,
        "B": 8,
        "C": 1,
        "D": 6
      },
      "roundCreated": 2,
      "roundReceived": 4
    },
    "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad": {
      "bodySignature": "e0626203b0ab0077ae6b8e1c51c62ec2278640006095a0a1091c81771b05f9f0",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 14,
          "key": "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 17,
          "key": "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
          "peerDeviceId": "B"
        },
        "otherParentHash": "edd2f8d2b43a0928ed840c328760627dfa501a1c4021567d33b51432efd8da28",
        "selfParent": {
          "eventCreatorIndex": 13,
          "key": "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f",
          "peerDeviceId": "D"
        },
        "selfParentHash": "2b3713a0f6209a1d14b8ec8356e8c7a67be588488dec2dd13dffb8c5cee8f1b7",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "C": 6,
        "D": 15
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 10,
        "B": 17,
        "C": 5,
        "D": 14
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "fa70213c8aaf9d8fdd6d9377a388260efb452ec9f6afadb591d7ca6782cb9a57": {
      "bodySignature": "51723dc5c24f027a7b139fc1f7d6fe0de64f8a41f20aac259bc0045d2d55d462",
      "consensusTimestamp": 0,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 12,
          "key": "fa70213c8aaf9d8fdd6d9377a388260efb452ec9f6afadb591d7ca6782cb9a57",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 29,
          "key": "d210ba50f39c0d38f61379d30c99f31cc7b3af39b7aa19320394f504fb3a40a5",
          "peerDeviceId": "B"
        },
        "otherParentHash": "18b8c58db4ac08d8679fa3546a5d7fa8ee9d16407ed40f5e47a2762236cbc8c8",
        "selfParent": {
          "eventCreatorIndex": 11,
          "key": "22b5894e02a73bb5dee8ae7db1fc6f2502052c6da5c20d77612682022bd4bdae",
          "peerDeviceId": "C"
        },
        "selfParentHash": "5a884e182fd47d290ac6b056a18370495a54859b16d1c4d333ef252c4c0517eb",
        "timestamp": 1641661516,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 18,
        "B": 31,
        "C": 14,
        "D": 21
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": true,
      "lastAncestors": {
        "A": 17,
        "B": 29,
        "C": 12,
        "D": 20
      },
      "roundCreated": 9,
      "roundReceived": -1
    },
    "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a": {
      "bodySignature": "b06ddb9f90707e396f43d7171179e77e7f6b11300d24434106644038151d6789",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 11,
          "key": "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 10,
          "key": "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
          "peerDeviceId": "D"
        },
        "otherParentHash": "04484a7899836ba785c3af28676a5459044836a57d5f2a500ed182f54b5e9273",
        "selfParent": {
          "eventCreatorIndex": 10,
          "key": "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
          "peerDeviceId": "B"
        },
        "selfParentHash": "ee5e0bb175ae6c9698f62aaca02a2bcf50df7db68b3e0576584c27acab4118f8",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 12,
        "C": 5,
        "D": 12
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 7,
        "B": 11,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6": {
      "bodySignature": "4f5ed15fc344de48998fed78cb3dec182bd067cbc163ba7549556bdbed66fdad",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 4,
          "key": "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6",
          "peerDeviceId": "C"
        },
        "otherParent": {
          "eventCreatorIndex": 11,
          "key": "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a",
          "peerDeviceId": "B"
        },
        "otherParentHash": "b06ddb9f90707e396f43d7171179e77e7f6b11300d24434106644038151d6789",
        "selfParent": {
          "eventCreatorIndex": 3,
          "key": "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
          "peerDeviceId": "C"
        },
        "selfParentHash": "c0b1600027320bddc1ef90f1549ed399d84da0f9dd749b19fa1d9e04b233c16c",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "C": 5,
        "D": 12
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 7,
        "B": 11,
        "C": 4,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 4
    },
    "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f": {
      "bodySignature": "2b3713a0f6209a1d14b8ec8356e8c7a67be588488dec2dd13dffb8c5cee8f1b7",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 13,
          "key": "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 15,
          "key": "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
          "peerDeviceId": "B"
        },
        "otherParentHash": "de432dfe38ebe55085fa4858c5a92998e4498dc2110a2d617c05a0984459ebcc",
        "selfParent": {
          "eventCreatorIndex": 12,
          "key": "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
          "peerDeviceId": "D"
        },
        "selfParentHash": "6f9679e69ed1a8438f61047c46f6f1b8d94ea270e92411203ced43bb4c25a196",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 17,
        "D": 14
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 8,
        "B": 15,
        "C": 5,
        "D": 13
      },
      "roundCreated": 4,
      "roundReceived": 5
    },
    "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23": {
      "bodySignature": "527cf5e61b2a32a5782f1485a91788d3648e6f98becd25db3293deca23ebaf49",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 15,
          "key": "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 5,
          "key": "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
          "peerDeviceId": "C"
        },
        "otherParentHash": "a137eb02f7b5a27cfeb6f2665028a70bf77abc92da0cdc1b0cf907aae3a5ecb2",
        "selfParent": {
          "eventCreatorIndex": 14,
          "key": "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
          "peerDeviceId": "D"
        },
        "selfParentHash": "e0626203b0ab0077ae6b8e1c51c62ec2278640006095a0a1091c81771b05f9f0",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 14,
        "C": 6,
        "D": 15
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 10,
        "B": 17,
        "C": 5,
        "D": 15
      },
      "roundCreated": 5,
      "roundReceived": 6
    },
    "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c": {
      "bodySignature": "c0dea7a627c4e4f449a200e8e7e24fb65c1983825de9860fe849283c833f9f35",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 4,
          "key": "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
          "peerDeviceId": "D"
        },
        "otherParent": {
          "eventCreatorIndex": 1,
          "key": "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648",
          "peerDeviceId": "A"
        },
        "otherParentHash": "bcbe4df273080c34fba91a209ad69c1f5964dfd441bd2bfced0972fe3b4539e8",
        "selfParent": {
          "eventCreatorIndex": 3,
          "key": "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934",
          "peerDeviceId": "D"
        },
        "selfParentHash": "60e0bfc3b7e595ed128bd6c00705b665f815c96ecf97df1ab3a42da4566713c1",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 4,
        "B": 6,
        "C": 2,
        "D": 4
      },
      "isDecided": true,
      "isFamous": true,
      "isWitness": true,
      "lastAncestors": {
        "A": 1,
        "B": 2,
        "C": 0,
        "D": 4
      },
      "roundCreated": 1,
      "roundReceived": 2
    },
    "7f4ad165faba63f8891890e1704cf042727c76dfb8812ffaff566517cb8be642": {
      "bodySignature": "7d9cbfd4290ca10f936cd7b769a42ca515fb9f8cc22ee290e3aab61c76f6b33d",
      "consensusTimestamp": 1641661515,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 13,
          "key": "7f4ad165faba63f8891890e1704cf042727c76dfb8812ffaff566517cb8be642",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 8,
          "key": "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
          "peerDeviceId": "A"
        },
        "otherParentHash": "64e4994b05364f5393515305175dd2c29b3fdd7d8cfc66bc37b87331ac1093bd",
        "selfParent": {
          "eventCreatorIndex": 12,
          "key": "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
          "peerDeviceId": "B"
        },
        "selfParentHash": "10f1f621f8d9ad99a7a317f9bcd757315f23fb15d019f8e48ee0b1f3032b1141",
        "timestamp": 1641661515,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "B": 15
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "A": 8,
        "B": 13,
        "C": 3,
        "D": 10
      },
      "roundCreated": 3,
      "roundReceived": 5
    },
    "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a": {
      "bodySignature": "d2b8b2ac46bcb1a0cc23a863ee4f13902270d8b58ef128cfc74508ac1bc49684",
      "consensusTimestamp": 1641661514,
      "eventBody": {
        "creatorAssociation": {
          "eventCreatorIndex": 1,
          "key": "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
          "peerDeviceId": "B"
        },
        "otherParent": {
          "eventCreatorIndex": 1,
          "key": "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681",
          "peerDeviceId": "D"
        },
        "otherParentHash": "8b4b39f1992af5a79a876eb67dc71c198791f038604b2aa3bdcf01419e2b3bf8",
        "selfParent": {
          "eventCreatorIndex": 0,
          "key": "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
          "peerDeviceId": "B"
        },
        "selfParentHash": "b8395a581b9fa2dcd939c1cec7c30c4516b4c0de52d0e5aedc3aa1a9d1b9ed37",
        "timestamp": 1641661514,
        "transactions": [
          {
            "creationTime": 0,
            "goalPeerDeviceId": "A"
          }
        ]
      },
      "firstDiscendants": {
        "A": 3,
        "B": 2,
        "C": 2,
        "D": 4
      },
      "isDecided": false,
      "isFamous": false,
      "isWitness": false,
      "lastAncestors": {
        "B": 1,
        "D": 1
      },
      "roundCreated": 0,
      "roundReceived": 1
    }
  },
  "rounds": {
    "0": {
      "committed": true,
      "decidedWitnesses": [
        "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
        "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
        "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
        "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14"
      ],
      "determinedEvents": [
        "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
        "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
        "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
        "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681",
        "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
        "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
        "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14",
        "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648",
        "2265f5336d7b6037b5b75ace727a6c482c37ae963dad3bd8eff402314e8548ab",
        "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934",
        "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6",
        "0cd20d37dbaa799d1d2f6f04adbab0b9e958b083f38e06512cdefadd20863f98"
      ],
      "events": [
        "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
        "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
        "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
        "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681",
        "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
        "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
        "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6",
        "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14",
        "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648",
        "2265f5336d7b6037b5b75ace727a6c482c37ae963dad3bd8eff402314e8548ab",
        "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934",
        "0cd20d37dbaa799d1d2f6f04adbab0b9e958b083f38e06512cdefadd20863f98"
      ],
      "inRoundDeterminedEvents": [],
      "peersInRound": 4,
      "roundCreated": 0,
      "roundReceived": -1,
      "witnesses": [
        "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
        "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
        "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
        "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14"
      ]
    },
    "1": {
      "committed": true,
      "decidedWitnesses": [
        "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
        "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
        "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
        "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57"
      ],
      "determinedEvents": [
        "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
        "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
        "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6",
        "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
        "12a750139ca2e4c14287bb6ed9ece9ee75b556a911f19f91c2f0d59ef40e7597",
        "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
        "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4",
        "5ba2c833c5d65e649e4b4fa4d426223f3300650f874e32c4451d9346ce6469e2",
        "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb"
      ],
      "events": [
        "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
        "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
        "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6",
        "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
        "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
        "12a750139ca2e4c14287bb6ed9ece9ee75b556a911f19f91c2f0d59ef40e7597",
        "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
        "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4",
        "5ba2c833c5d65e649e4b4fa4d426223f3300650f874e32c4451d9346ce6469e2"
      ],
      "inRoundDeterminedEvents": [
        "c899b3d71c1f520db816563ec9d7d0c4f15a47776d1e52e83bddfec13a440e7b",
        "05816a1560db947d6ff798e30909816f400f14230e9a06afac8f8b213127aa21",
        "cf440f61634b8b95c9a22657060ec63fd4323075838d159a7ae91e5287700a32",
        "33a123e5d474e8f3495a7c304f17184276715204ccb2887317f37bcb216b4681",
        "5b950e77941d01cdf246d00b1ece546bc95234b77d98b44c9187e2733afa696a",
        "abdbc2b5cc2c7a519b72bf7a164c58ebf892ab0c2df6468213705cc2f0da8561",
        "aa508c2187fca56f397ff75adc52b94e02f38122cdd48bd42105106e5e0f8e14",
        "16a36e86f6fed5d465ff332511a0ce1a863b55d364b25a7cdaa25db19abf9648",
        "2265f5336d7b6037b5b75ace727a6c482c37ae963dad3bd8eff402314e8548ab",
        "bed7abeac56e560a96b7fef4c846a691fe3deb2e4d1e5bbf1085b8d9e2c6e934"
      ],
      "peersInRound": 4,
      "roundCreated": 1,
      "roundReceived": -1,
      "witnesses": [
        "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
        "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
        "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
        "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57"
      ]
    },
    "2": {
      "committed": true,
      "decidedWitnesses": [
        "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
        "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
        "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
        "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea"
      ],
      "determinedEvents": [
        "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
        "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
        "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb",
        "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
        "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
        "f86ae46d947e2215ce53b1ae840af949b5f686e69ea2f6b7eaf3725619d4303e",
        "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75",
        "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359",
        "d94791a85f88d5f49c3cc06d5557316cf743d60149820c594f389a1b301ff021"
      ],
      "events": [
        "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
        "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
        "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb",
        "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
        "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
        "f86ae46d947e2215ce53b1ae840af949b5f686e69ea2f6b7eaf3725619d4303e",
        "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75",
        "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359",
        "d94791a85f88d5f49c3cc06d5557316cf743d60149820c594f389a1b301ff021"
      ],
      "inRoundDeterminedEvents": [
        "ab861dc170dc2e43224e45278d3d31a675b9ebc34c9b0f48c066ca1eeaed8ee6",
        "0cd20d37dbaa799d1d2f6f04adbab0b9e958b083f38e06512cdefadd20863f98",
        "080f626098377e96e40b2ff0260738034149998b08e5c086b940ae567580c32c",
        "c8361f9b468e68c86da024270e0949ce139cb704b8d7cce586681b99f3a7ea56",
        "1398b376fdcce25c5a5399367e76891e85121c010ec919cc243b1a519d95bbc6",
        "239fd09dd1c48679b74cec2120cd5e448b002c728c05e9b10f2c19f298fbdd57",
        "12a750139ca2e4c14287bb6ed9ece9ee75b556a911f19f91c2f0d59ef40e7597",
        "4e808094851fc2eac7a386fc7d64677b34bda5e41d366ec4943233f9e6f2cd63",
        "ed35195ae02792a34387364493a4c766809f13a5d2b597830d70db652bd1afa4",
        "5ba2c833c5d65e649e4b4fa4d426223f3300650f874e32c4451d9346ce6469e2"
      ],
      "peersInRound": 4,
      "roundCreated": 2,
      "roundReceived": -1,
      "witnesses": [
        "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
        "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
        "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
        "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea"
      ]
    },
    "3": {
      "committed": true,
      "decidedWitnesses": [
        "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
        "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
        "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
        "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6"
      ],
      "determinedEvents": [
        "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
        "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
        "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
        "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
        "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a",
        "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6",
        "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
        "a7dc9aa658db149b641d28252d72e0b081504170be70b919c22bcefc43e5b33c",
        "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
        "7f4ad165faba63f8891890e1704cf042727c76dfb8812ffaff566517cb8be642",
        "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c",
        "06663975f75f189f1d70bd14d8f22df264cd6a5c7575d6875183d0ec76432fbb"
      ],
      "events": [
        "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
        "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
        "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
        "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
        "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a",
        "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6",
        "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
        "a7dc9aa658db149b641d28252d72e0b081504170be70b919c22bcefc43e5b33c",
        "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
        "7f4ad165faba63f8891890e1704cf042727c76dfb8812ffaff566517cb8be642",
        "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c",
        "06663975f75f189f1d70bd14d8f22df264cd6a5c7575d6875183d0ec76432fbb"
      ],
      "inRoundDeterminedEvents": [
        "9685eb765661ea3b95f31e1bb3c3b5501d0c2acdf353feeaa4d8fe32f95f77fb",
        "9d574e1d3c5ed212edee33e2478e5a62cdecc5b5cb365479c4eb99e9d342aa38",
        "2f434ba53bd39e7933d7e12070c4a783c41b3f1c68d9f14008cb29f7c3871a1e",
        "e32ddc3033b526c2e907339aab9b1833cf3326fae99c70d08e72512dd7c96ecb",
        "8a214cef6d474c9ad7249b3267218f8f0b7a5ad3a0f3ff09c692251fe9b827ca",
        "ea644b359f0b0abde72ab7dbdc03c7d630537bdd0fd7ca1bbb99d41e7f446eea",
        "f86ae46d947e2215ce53b1ae840af949b5f686e69ea2f6b7eaf3725619d4303e",
        "0e1ef51633293b35ad3d62b4e963902899ed8420ddd37063f26b64217e66ad75",
        "3ded92c4648c479ce74d18b838a651e02940569dc5840edd87a7d52216256359"
      ],
      "peersInRound": 4,
      "roundCreated": 3,
      "roundReceived": -1,
      "witnesses": [
        "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
        "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
        "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
        "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6"
      ]
    },
    "4": {
      "committed": true,
      "decidedWitnesses": [
        "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
        "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
        "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
        "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5"
      ],
      "determinedEvents": [
        "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
        "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
        "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
        "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f",
        "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5",
        "bc215963d1a424a5f9707d565f07a5bcf79e19cde17372a9a6a914cd986f7fc9"
      ],
      "events": [
        "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
        "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
        "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
        "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f",
        "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5",
        "bc215963d1a424a5f9707d565f07a5bcf79e19cde17372a9a6a914cd986f7fc9"
      ],
      "inRoundDeterminedEvents": [
        "d94791a85f88d5f49c3cc06d5557316cf743d60149820c594f389a1b301ff021",
        "724f7bdf7e74a5fe64337203fb8b6ccf4adfc2919665e67a81f02e81752c1c97",
        "54bef1ccfde12b92ac87f0731d2611afac49f51b8e1e1767476eff666dc51a79",
        "9102326afa32b91a69f6abf5a9505b78f6828ffd9b5ab3d7a78ada019738046e",
        "d322de085a24ae58593ea47dd09157f88fb27454bf08582384f5693d97ed06f8",
        "c879dc6e7e8200d38565e3d604591f6a727273b5b566ee119ea7a22e7d1f888a",
        "08d1623c441b55a6989fce1086354967eb9f522e4cab47da49e9e1e640afbde6",
        "1701d0609e59cfd22e610b426ade95de13bfc292481a91c5276d5842d9262019",
        "a7dc9aa658db149b641d28252d72e0b081504170be70b919c22bcefc43e5b33c"
      ],
      "peersInRound": 4,
      "roundCreated": 4,
      "roundReceived": -1,
      "witnesses": [
        "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
        "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
        "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
        "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5"
      ]
    },
    "5": {
      "committed": true,
      "decidedWitnesses": [
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5"
      ],
      "determinedEvents": [
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
        "00ceeab4df7002aad9c625c69e81c47d07f71027ad3600787a73c7e91fdf8d61",
        "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024",
        "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e",
        "91bec90d2f59a91f2e7c08d17b5334af65f58b47672600b8bdb4a44a8b0d81c8"
      ],
      "events": [
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
        "00ceeab4df7002aad9c625c69e81c47d07f71027ad3600787a73c7e91fdf8d61",
        "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024",
        "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e",
        "91bec90d2f59a91f2e7c08d17b5334af65f58b47672600b8bdb4a44a8b0d81c8"
      ],
      "inRoundDeterminedEvents": [
        "553a0fddbb387723578263570e63a83955482ae44f45bac9a90c65ddc058329f",
        "7f4ad165faba63f8891890e1704cf042727c76dfb8812ffaff566517cb8be642",
        "b6e084c59b2e6e41557844ae40a6b32c2488e334a57793ac08d1fa35bf7bb53c",
        "06663975f75f189f1d70bd14d8f22df264cd6a5c7575d6875183d0ec76432fbb",
        "8c53e7b89615ad0a61a5c47204325872549d3a2d5af9d460f1345249e5782bcd",
        "1d96682bdb05ed312e0ce774ccefe0394472b88085413c3774c2df2ac7618c23",
        "04ec0e04721c79735378d4af0b53c3dd3e0d6ebf4ae52e90934524fbc7a3f5fd",
        "72ce87717c0cdc008a2bc8964e7a3ae01984b65f4baeec59d00519e8498a3e2f",
        "ad0608725cbbdbc36406d149067a32b0a77a524b5fff5183cc76c0d6b7f935b5",
        "bc215963d1a424a5f9707d565f07a5bcf79e19cde17372a9a6a914cd986f7fc9"
      ],
      "peersInRound": 4,
      "roundCreated": 5,
      "roundReceived": -1,
      "witnesses": [
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5"
      ]
    },
    "6": {
      "committed": true,
      "decidedWitnesses": [
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2"
      ],
      "determinedEvents": [
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855",
        "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
        "04ee0df547e7f6a0c65d15af049d47420008eafb8df8e37452d934c8e2499f14",
        "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
        "1d3a071aecf272a7b72d68659ffd251c94a39817614912fc97fc969725000774"
      ],
      "events": [
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855",
        "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
        "04ee0df547e7f6a0c65d15af049d47420008eafb8df8e37452d934c8e2499f14",
        "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2",
        "1d3a071aecf272a7b72d68659ffd251c94a39817614912fc97fc969725000774"
      ],
      "inRoundDeterminedEvents": [
        "ee29b54b234f20ebb7c2934e453cd5c732cc1b5fd0fc3928147f9dd9f5a4fdb1",
        "0683c2bb5f8f1c15900b8b2f8126993f9f056ebde4758997e996ded4557b72ad",
        "d91f856d4ffd88ddf00f3febfd01ff9068ac308271e6b6dc4b486c9ea3a3bf23",
        "90fce73cb7c144cf09bf1f8c6719765172f384716c0574b2c5c1248e921fc8a1",
        "37b5be61fefd1edea7761c41767c6c4e8bda09d7e7b73002b6ef98b481bb68a5",
        "00ceeab4df7002aad9c625c69e81c47d07f71027ad3600787a73c7e91fdf8d61",
        "d614cbb672fe000ee39c1919e5b034f2e55b702cafaff1a7cc5f37dcf7ad1024",
        "5d73ebde81987d4c7512a0432572a87d9d31a7b8074dde9c4846f6c74dc3429e"
      ],
      "peersInRound": 4,
      "roundCreated": 6,
      "roundReceived": -1,
      "witnesses": [
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2"
      ]
    },
    "7": {
      "committed": true,
      "decidedWitnesses": [
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0"
      ],
      "determinedEvents": [
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
        "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85",
        "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524"
      ],
      "events": [
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
        "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85",
        "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524"
      ],
      "inRoundDeterminedEvents": [
        "91bec90d2f59a91f2e7c08d17b5334af65f58b47672600b8bdb4a44a8b0d81c8",
        "899af38b9adba81c9243fc896f19eb12efdc8d9f03654932ccd036915267f308",
        "802ef7db01bbb818f15153b3c0a94b5cf04667714bbf1314f5a604ef552c9677",
        "3a7d0915bebcba1ecd5c9c5097038d46712fd908631a8c49ec7eb803eb9d59af",
        "fc29f17088f10d1df8502ae289be98fdf6de8b52549aa03cd02f7c92018d9855",
        "cc1e22142e7d545252f349a1d1dd84100e4441043f7485de6eeeb2f9eaea9e14",
        "04ee0df547e7f6a0c65d15af049d47420008eafb8df8e37452d934c8e2499f14",
        "9a1c712c3a26fe45003b72e3edbe78cefb712ced80a79cec15f40db1644b1e7b",
        "f167717fb2ed36e774225dd5b609cd208e028ba12cfc08946de444227e4e80d2"
      ],
      "peersInRound": 4,
      "roundCreated": 7,
      "roundReceived": -1,
      "witnesses": [
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0"
      ]
    },
    "8": {
      "committed": false,
      "decidedWitnesses": [
        "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
        "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
        "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
        "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
        "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
        "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
        "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
        "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
        "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
        "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
        "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
        "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
        "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a",
        "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a",
        "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a",
        "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a"
      ],
      "determinedEvents": [],
      "events": [
        "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
        "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
        "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
        "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a",
        "8abdf1580603d91a8e255690a4b7381a36aff7b0c4c0c6589831ddf165aca75c",
        "22b5894e02a73bb5dee8ae7db1fc6f2502052c6da5c20d77612682022bd4bdae"
      ],
      "inRoundDeterminedEvents": [
        "1d3a071aecf272a7b72d68659ffd251c94a39817614912fc97fc969725000774",
        "483b1a8835281f4735217c0119b7b26274f44576877be4e5cbf9f67481d8d293",
        "fe5ad2812dc8d3f184bc2efd82bcb603ee59cac271912408a5a0432d4916f5f9",
        "8aaf502a219414d94655682bf4c7a66df2ce87252e242f48691bb50b898d3ece",
        "f09d8479566a0c7cdb156fa8635e44990b471b4a641167201c79fed549ecd5f0",
        "3e781bcc10a62912f6fae532e0ce0e368b456b2ff739fc8b4bc293c73c34fc85",
        "2a36848a80644691f0e2f3c5b5fcb7871fe5b069108940563dfbfe9b50f78524"
      ],
      "peersInRound": 4,
      "roundCreated": 8,
      "roundReceived": -1,
      "witnesses": [
        "14a839c6693b8068f90616e2fd312dfbefc3a2099b1498093c7e15a8a74aa215",
        "039d35a39f1d47b9fbcf9e375f44c59313398d6379cb908517fbd7ea38197d44",
        "4bddd22de96ee7dad5296d79582f783b97d1a3d9779662b9afb05608228af05e",
        "908d72900e2475921b580e971e603ef224f1995cdf47e3022d12ee88ae3e6e8a"
      ]
    },
    "9": {
      "committed": false,
      "decidedWitnesses": [],
      "determinedEvents": [],
      "events": [
        "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc",
        "422446d7512f61f772230f96c25069087be68c6ec57af8e1f18be7a9fad55375",
        "d210ba50f39c0d38f61379d30c99f31cc7b3af39b7aa19320394f504fb3a40a5",
        "fa70213c8aaf9d8fdd6d9377a388260efb452ec9f6afadb591d7ca6782cb9a57",
        "726a2749e243fa32b5dbbbcde1ff60642830a8a6f7afba55458ac681a6908461",
        "6645ca87da6316d5bb2b8e48f6d382c9ffff5a74966c81debc183dc6bb84130d"
      ],
      "inRoundDeterminedEvents": [],
      "peersInRound": 4,
      "roundCreated": 9,
      "roundReceived": -1,
      "witnesses": [
        "74be068977dafbd3302b39fe6195b66b0cf507eb05c054bc422cca1035dcc6fc",
        "422446d7512f61f772230f96c25069087be68c6ec57af8e1f18be7a9fad55375",
        "d210ba50f39c0d38f61379d30c99f31cc7b3af39b7aa19320394f504fb3a40a5",
        "fa70213c8aaf9d8fdd6d9377a388260efb452ec9f6afadb591d7ca6782cb9a57"
      ]
    },
    "10": {
      "committed": false,
      "decidedWitnesses": [],
      "determinedEvents": [],
      "events": [
        "5985f6f8353e299ba80dec0a569d2757f733a25567a6a4f38f5f102770495ae6",
        "fa267bb037d77a0599298151783319ce7a4ff032983503ee466717e814e43207",
        "5eb00cfd65e6c6c1ae30f9a19426b50a9f3a89bddd63d7e0cc662c15c12c6ebf",
        "fafc221218d3b700c520f88d2d25775cd5135fa3964607b547671c197e990465"
      ],
      "inRoundDeterminedEvents": [],
      "peersInRound": 4,
      "roundCreated": 10,
      "roundReceived": -1,
      "witnesses": [
        "5985f6f8353e299ba80dec0a569d2757f733a25567a6a4f38f5f102770495ae6",
        "fa267bb037d77a0599298151783319ce7a4ff032983503ee466717e814e43207",
        "5eb00cfd65e6c6c1ae30f9a19426b50a9f3a89bddd63d7e0cc662c15c12c6ebf",
        "fafc221218d3b700c520f88d2d25775cd5135fa3964607b547671c197e990465"
      ]
    }
  }
}"""

    def test_something(self):
        decodedStore = StoreJSONDecoder().decodeFromJsonString(self.jsonStore)
        self.assertTrue(isinstance(decodedStore, Store))


if __name__ == '__main__':
    unittest.main()
