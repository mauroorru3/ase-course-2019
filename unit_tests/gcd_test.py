import calculator as c
import unittest


class TestGcd(unittest.TestCase):

    def test_gdc_integers_positive(self):
        result = c.gdc(1, 2)
        self.assertEqual(result, 1)

    def test_gdc_integers_positive1(self):
        result = c.gdc(8, 2)
        self.assertEqual(result, 2)

    def test_gdc_integers_positive2(self):
        result = c.gdc(8, 4)
        self.assertEqual(result, 4)

    def test_gdc_integers_positive3(self):
        result = c.gdc(17, 21)
        self.assertEqual(result, 1)

    def test_gdc_integers_negative(self):
        result = c.gdc(-1, -2)
        self.assertEqual(result, 1)

    def test_gdc_integers_pos_neg(self):
        result = c.gdc(1, -2)
        self.assertEqual(result, 1)

    def test_gdc_integers_neg_pos(self):
        result = c.gdc(-1, 2)
        self.assertEqual(result, 1)

    def test_gdc_zero_zero(self):
       self.assertRaises(ValueError, c.gdc, 0, 0)


if __name__ == '__main__':
    unittest.main()