__author__ = 'etuka'

import unittest
import re
from robots import *

class RobotTestCase(unittest.TestCase):

  def setup(self):
    pass

  def test_buildEnvironment(self):
    input = """11 5
     1 1 E
     RLBFL
     2 3 S
     LFRFLLF"""
    factory = Factory(input)
    env = factory.build()

    self.assertEqual(env.mesa.width, 11)
    self.assertEqual(env.mesa.length, 5)

    self.assertEqual(env.machinesAndInstructions[0][0].position(), ([1,1], 'E'))
    self.assertEqual(env.machinesAndInstructions[0][1], "RLBFL")

  def test_mesaBounds(self):
    input = """1 1
     0 0 E
     FRLBFL
     0 0 S
     BLFRFLLF"""
    factory = Factory(input)
    environment = factory.build()

    mesa = environment.mesa

    (robot1, dir1) = environment.machinesAndInstructions[0]
    (robot2, dir2) = environment.machinesAndInstructions[1]

    self.assertEqual(robot1 in mesa, True)
    robot1.move(dir1[0])
    self.assertEqual(robot1 in mesa, False)

    self.assertEqual(robot2 in mesa, True)
    robot2.move(dir2[0])

    self.assertEqual(robot2 in mesa, False)


  def test_fallingForSameTrickTwice(self):
    input = """3 3
     1 1 E
     FFBBBFLB
     1 1 E
     FFBBBFLB
     1 1 E
     FFBBBFLB"""
    factory = Factory(input)
    env = factory.build()
    log = explore(env)

    def contains(line, pos = None, status = None, command = None):
      status_pattern = "%s" % status
      pos_pattern = "position \(%s,%s\), heading %s" % (pos[0][0], pos[0][1], pos[1])
      command_pattern = "(go|going) %s" % command

      status_result = True if status is None else re.match(status_pattern, line) is not None
      pos_result = True if pos is None else re.search(pos_pattern, line) is not None
      command_result = True if command is None else re.search(command_pattern, line) is not None

      return status_result and pos_result and command_result
    for line in log:
      print line

    self.assertEqual(True, contains(log[0], ([2,1],'E'), "INFO", None))
    self.assertEqual(True, contains(log[1], ([2,1],'E'), "ERROR", 'F'))
    self.assertEqual(True, contains(log[2], ([2,1],'E'), "INFO", None))
    self.assertEqual(True, contains(log[3], ([2,1],'E'), "WARNING", 'F'))
    self.assertEqual(True, contains(log[4], ([1,1],'E'), "INFO", None))




  def test_buildMesa(self):
    input = "11 5"
    factory = Factory("")
    mesa = factory.buildMesa(input)
    self.assertEqual(mesa.width, 11)
    self.assertEqual(mesa.length, 5)


  def test_buildRobot(self):
    input = "1 1 E"
    factory = Factory("")
    robot = factory.buildRobot(input)
    self.assertEqual(robot.position(), ([1,1], 'E'))

  def test_verifyLocation(self):
    robot = Robot(([1,1],'E'))

    self.assertEqual(([1,1], 'E'), robot.position())

  def test_right(self):
    robot = Robot(([1,1],'E'))
    robot.move('R')
    #print robot.position()
    self.assertEqual(([1,1], 'S'), robot.position())

  def test_left(self):
    robot = Robot(([1,1],'E'))
    robot.move('L')
    #print robot.position()
    self.assertEqual(([1,1], 'N'), robot.position())

  def test_forward(self):
    robot = Robot(([1,1],'E'))
    robot.move('F')
    #print robot.position()
    self.assertEqual(([2,1], 'E'), robot.position())

  def test_back(self):
    robot = Robot(([1,1],'E'))
    robot.move('B')
    self.assertEqual(([0,1], 'E'), robot.position())

  def readDirections(self):
    pass


if __name__ == "__main__":
  unittest.main()
