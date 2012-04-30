import string

directions = {'E': (0, (1, 0)), 'S': (1, (0, -1)), 'W': (2, (-1, 0)), 'N': (3, (0, 1))}
invDirections = {0:'E', 1:'S', 2:'W', 3: 'N'}

def right(robot):
  idx = directions[robot.heading][0]
  robot.heading = invDirections[(idx + 1) % 4]

def left(robot):
  idx = directions[robot.heading][0]
  robot.heading = invDirections[(idx - 1) % 4]

def back(robot):
  inc = list(directions[robot.heading][1])
  robot.pos = [robot.pos[0] - inc[0], robot.pos[1] - inc[1]]

def forward(robot):
  inc = list(directions[robot.heading][1])
  robot.pos = [robot.pos[0] + inc[0], robot.pos[1] + inc[1]]

moveMap = {'R': right, 'L': left, 'F': forward, 'B': back}

def move(robot, instruction):
  return moveMap[instruction](robot)

class Mesa:

  def __init__(self, width, length):
    self.width = width
    self.length = length
    self.markers = set([])

  def __contains__( self, robot):
    def ge(lhs, rhs):
      return lhs[0] >= rhs[0] and lhs[1] >= rhs[1]
    def lt(lhs, rhs):
      return lhs[0] < rhs[0] and lhs[1] < rhs[1]
    return ge(robot.position()[0], [0,0]) and lt(robot.position()[0], [self.width, self.length])

  def addMarker(self, (positionString, instruction)):
    self.markers.add((positionString, instruction))


class Robot:

  def __init__(self, ((x,y), heading)):
    self.pos = [x,y]
    self.heading = heading

  def __str__(self):
    return "position (%s,%s), heading %s" % (self.pos[0], self.pos[1], self.heading)

  def toString(self):
    return "%i %i %s" % (self.pos[0],self.pos[1],heading)

  def position(self):
    return (self.pos, self.heading)

  def move(self, instruction):
    return moveMap[instruction](self)


class Factory:
  def __init__(self, input):
    self.lines = input.strip().split("\n")

  def buildMesa(self, input):
    numbers = input.strip().split()
    return Mesa(int(numbers[0]), int(numbers[1]))

  def buildRobot(self, input):
    robotParms = input.strip().split(' ')
    return Robot(((int(robotParms[0]), int(robotParms[1])), robotParms[2]))

  def build(self):
    mesa = self.buildMesa(self.lines[0])
    robots = []
    instructions = []
    for i in xrange(1,len(self.lines),2):
      robots.append( self.buildRobot(self.lines[i]))
      instructions.append(self.lines[i+1].strip())

    return Environment((mesa, robots, instructions))

class Environment:

  def __init__(self, (mesa, robots, instructions)):
    self.machinesAndInstructions = zip(robots, instructions)
    self.mesa = mesa


def explore(env):
  mesa = env.mesa
  i = 1
  result = []
  for (robot, instructions) in env.machinesAndInstructions:
    for instruction in instructions:
      pos = str(robot)
      if (pos, instruction) in mesa.markers:
        result.append( "WARNING: Robot %i at %s won't go %s.  Others have crashed attempting this." % (i, pos, instruction))
        continue
      robot.move(instruction)
      if(robot not in mesa):
        result.append( "ERROR: Robot %i crashed at %s, going %s." % (i, pos, instruction))
        mesa.addMarker((pos, instruction))
        break;
      else:
        result.append( "INFO: Robot %i at %s." % (i, str(robot)))
    i += 1
  return result

if __name__ == "__main__":
  input = """11 2
     1 1 E
     RLBFFFFL
     2 1 S
     LFRFLRFBBRFFFLFFRBLFB
     2 1 S
     LFRFLRFBBRFFFLFFRBLFB
     2 1 S
     LFRFLRFBBRFFFLFFRBLFB
     2 1 S
     LFRFLRFBBRFFFLFFRBLFB
     2 1 S
     LFRFLRFBBRFFFLFFRBLFB"""

  print "Building scenario..."
  factory = Factory(input)
  env = factory.build()
  print "Sending robots out to explore..."
  log = explore(env)
  for item in log:
    print item


