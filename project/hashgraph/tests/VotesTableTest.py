import unittest

from project.hashgraph.models.VotesTable import VotesTable


class VotesTableTest(unittest.TestCase):
    def testVoteInsertOK(self):
        votesTable = VotesTable()
        votesTable.setVote('x', 'y', True)
        self.assertTrue(votesTable.getVote('x', 'y'))


if __name__ == '__main__':
    unittest.main()
