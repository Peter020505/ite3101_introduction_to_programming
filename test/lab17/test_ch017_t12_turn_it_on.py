import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t12_turn_it_on.py")
        expect_output = """0b10111111
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
