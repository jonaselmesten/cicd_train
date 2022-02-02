import unittest


class SumTesting(unittest.TestCase):

    def test_sum_of_int_str(self):
        data = [1, 2, "3"]
        with self.assertRaises(TypeError):
            assert self.assertEqual(sum(data), 6)

    def test_sum_of_ints(self):
        data = [1, 2, 3]
        self.assertEqual(sum(data), 6)


if __name__ == '__main__':
    unittest.main()
