import unittest
from immutability import A


class ImmutableClassTest(unittest.TestCase):

    def test_immutability(self):
        a = A("test")
        with self.assertRaises(ValueError):
            a.name = "another test"


if __name__ == '__main__':
    unittest.main()

