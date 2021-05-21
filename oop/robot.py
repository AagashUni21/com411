class Robot:
#The class i.e. blueprint for my objects

  #Class attribute -> constant, visible to all objects of the class
  MAX_ENERGY = 100
  #Initialiser (special instance method, invoked only once, at creation)
  def __init__(self):
    #Instance attributes
      self.name = "Robot"
      self.age = 0
      self.energy = 0
      
  def display(self):
    print(f"Hello i am {self.name}")

