from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.inhabitants = []

  def __repr__(self):
    num_humans = 0
    num_robots = 0
    for inhabitant in self.inhabitants:
      if isinstance(inhabitant, Human):
        num_humans += 1
      elif isinstance(inhabitant, Robot):
        num_robots += 1

    return f"planet(humans={num_humans}, robots={num_robots})"

  def __str__(self):
    num_humans = 0
    num_robots = 0
    for inhabitant in self.inhabitants:
      if isinstance(inhabitant, Human):
        num_humans += 1
      elif isinstance(inhabitant, Robot):
        num_robots += 1
    return f"This planet has {num_humans} humans and {num_robots} robots"

  def add_inhabitant(self, inhabitant):
    self.inhabitants.append(inhabitant)

  def remove_inhabitant(self, inhabitant):
    self.inhabitants.remove(inhabitant)

if (__name__ == "__main__"):
  earth2 = Planet()
  print(repr(earth2))
  prins = Human("Prins")
  earth2.add_inhabitant(prins)
  print(repr(earth2))
  beep = Robot("Beep")
  earth2.add_inhabitant(beep)
  print(repr(earth2))
  print(earth2)