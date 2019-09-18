import unittest
import get_column_stats as cs
import random as ra


class TestColumnStats(unittest.TestCase):
    def test_getmean(self):
        self.assertEqual(cs.getmean([1]), 1)

        # gives a list of 100 random number 100 times
        for i in range(0, 100):
            randnum = ra.randint(1, 100)
            constlist = [randnum]*ra.randint(1, 100)
            self.assertEqual(cs.getmean(constlist), randnum)

        # ensure that TypeError is raised for inputs of wrong type
        self.assertRaises(TypeError, cs.getmean, 'string')
        self.assertRaises(TypeError, cs.getmean, None)

    def test_getstdev(self):
        self.assertEqual(cs.getstdev([1]), 0)

        # gives a list of 100 random number 100 times
        for i in range(0, 100):
            constlist = [ra.randint(1, 100)]*ra.randint(1, 100)
            self.assertEqual(cs.getstdev(constlist), 0)

        # ensure that TypeError is raised for inputs of wrong type
        self.assertRaises(TypeError, cs.getstdev, 'string')
        self.assertRaises(TypeError, cs.getstdev, None)


if __name__ == '__main__':
    unittest.main()
