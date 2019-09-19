import unittest
import get_column_stats as cs
import random as ra


class TestColumnStats(unittest.TestCase):
    def test_getmean_none(self):
        self.assertRaises(TypeError, cs.getmean, None)

    def test_getmean_one_one(self):
        self.assertEqual(cs.getmean([1]), 1)

    # gives a list of 100 random number 100 times
    def test_getmean_random(self):
        for i in range(0, 100):
            randnum = ra.randint(1, 100)
            constlist = [randnum]*ra.randint(1, 100)
            self.assertEqual(cs.getmean(constlist), randnum)

    # ensure that TypeError is raised for inputs of wrong type
    def test_getmean_wrong_type(self):
        self.assertRaises(TypeError, cs.getmean, 'string')

    def test_getstdev_none(self):
        self.assertRaises(TypeError, cs.getstdev, None)

    def test_getstdev_one_one(self):
        self.assertEqual(cs.getstdev([1]), 0)

    # gives a list of 100 random number 100 times
    def test_getstdev_random(self):
        for i in range(0, 100):
            constlist = [ra.randint(1, 100)]*ra.randint(1, 100)
            self.assertEqual(cs.getstdev(constlist), 0)

    # ensure that TypeError is raised for inputs of wrong type
    def test_getstdev_wrong_type(self):
        self.assertRaises(TypeError, cs.getstdev, 'string')


if __name__ == '__main__':
    unittest.main()
