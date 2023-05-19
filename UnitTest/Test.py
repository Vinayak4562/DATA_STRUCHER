from unittest import TestCase
import unittest

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

# def test_always_passes():
#     assert True

# def test_always_fails():
#     assert False

# def test_always_fails():
#     assert False

if __name__ == "__main__":
    unittest.main()