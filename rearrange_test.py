#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase = "Lovecase, Ada"
        expected = "Ada Lovecase"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
