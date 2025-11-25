from cep import cep
import unittest

class TestCepFunctions(unittest.TestCase):
    def setUp(self):
        self.acc2d = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def test_cep_68(self):
        result = cep.cep_68(self.acc2d)
        self.assertEqual(result, 70)

    def test_cep_95(self):
        result = cep.cep_95(self.acc2d)
        self.assertEqual(result, 100)

    def test_cep_99(self):
        result = cep.cep_99(self.acc2d)
        self.assertEqual(result, 100)

    def test_cep_100(self):
        result = cep.cep_100(self.acc2d)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()