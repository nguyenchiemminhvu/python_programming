import logging
import unittest
from unittest import mock, TestCase

class TestSample(TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_sample(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

    def test_sum(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(2 + 2, 5)

class ToBeMocked:
    def do_something(self):
        return "Original do_something"

class TestMocking(TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    def test_mocking(self):
        with mock.patch.object(ToBeMocked, 'do_something', return_value="Mocked do_something"):
            obj = ToBeMocked()
            res = obj.do_something()
            self.assertEqual(res, "Mocked do_something")
            self.assertEqual(obj.do_something.call_count, 1)

if __name__ == '__main__':
    logging.info("Starting unit tests")
    unittest.main()
    logging.info("Unit tests completed")