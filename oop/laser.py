from tech import Tech

class Laser(Tech):

  MAX_RANGE = 100

  def __init__(self):
    self.range = Laser.MAX_RANGE

  def activate(self):
    print("This is laser. It has been activated")

  def deactivate(self):
    print("Laser has been deactivated")

  def fire(self, range):
    if range > Laser.MAX_RANGE:
      print(f"Fired at maximum distance of {Laser.MAX_RANGE}")
    else:
      print(f"Fired at a distance of {range}")