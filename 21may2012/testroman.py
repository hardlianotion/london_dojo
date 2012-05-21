import romannum

__author__ = 'etuka'

import unittest
from romannum import *



class RomanTest(unittest.TestCase):

  def test_one(self):
    self.assertEquals(convert(1), "I")

  def test_one(self):
    self.assertEquals(convert(0), "")

  def test_two(self):
    self.assertEqual(convert(2), "II")

  def test_three(self):
    self.assertEqual(convert(3), "III")

  def test_five(self):
    self.assertEqual(convert(5), "V")

  def test_four(self):
    self.assertEqual(convert(4), "IV")

  def test_six(self):
    self.assertEqual(convert(6), "VI")

  def test_seven(self):
    self.assertEqual(convert(7), "VII")

  def test_ten(self):
    self.assertEqual(convert(10), "X")

  def test_nine(self):
    self.assertEqual(convert(9), "IX")

  def test_49(self):
    self.assertEqual(convert(49), "XLIX")

  def test_61(self):
    self.assertEqual(convert(61), "LXI")

  def test_100(self):
    self.assertEqual(convert(100), "C")

  def test_2012(self):
    self.assertEqual(convert(2012), "MMXII")

  def test_1983(self):
    self.assertEqual(convert(1983), "MCMLXXXIII")

