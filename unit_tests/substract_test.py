import calculator as c
import unittest


class TestSubstract(unittest.TestCase):

    def test_substract_integers_positive(self):
        result = c.substract(1, 2)
        self.assertEqual(result, -1)

    def test_substract_integers_negative(self):
        result = c.substract(-1, -2)
        self.assertEqual(result, 1)

    def test_substract_integers_pos_neg(self):
        result = c.substract(1, -2)
        self.assertEqual(result, 3)

    def test_substract_integers_neg_pos(self):
        result = c.substract(-1, 2)
        self.assertEqual(result, -3)


if __name__ == '__main__':
    unittest.main()