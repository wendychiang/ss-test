import unittest

from ss_test.sample_size import get_mean
from ss_test.sample_size import get_sample_size


class TestSampleSize(unittest.TestCase):
    def test_numpy(self):
        test_nums = [1, 2, 3, 4]
        result = get_mean(test_nums)
        self.assertEqual(2.5, result)

    def test_statsmodel(self):
        result = get_sample_size(0.5)
        self.assertEqual(
            64.0,
            result,
        )
