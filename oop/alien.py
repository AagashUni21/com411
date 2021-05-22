from inhabitant import Inhabitant

class Alien(Inhabitant):

  def __init__(self, name = "ET", age = 0):
    self.technology = []
    super().__init__(name, age)

  def __str__(self):
    return f"Alien {self.name} of age {self.age} and energy {self.energy} and following tech: {self.technology}"

  def pickup(self, tech):
    self.technology.append(tech)

  def drop(self, tech):
    self.technology.remove(tech)


if __name__ == "__main__":
  sam = Inhabitant()
  print(sam.age)
  et = Alien()
  print(et)
  et.pickup("torch")
  et.pickup("jet pack")
  et.pickup("human bone")
  print(et)
  if "laser" in et.technology:
    et.drop("laser")
  print(et)