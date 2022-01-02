import unittest

from project.hashgraph.helpers.ListHelper import ListHelper


class ListHelperTest(unittest.TestCase):
    def testListDiff(self):
        listA = ['eventA', 'eventC']
        listB = ['eventB', 'eventC']
        listDiff = ListHelper.getListDiff(listA, listB)
        self.assertTrue(len(listDiff) == 1 and listDiff.pop() == 'eventB')


if __name__ == '__main__':
    unittest.main()
