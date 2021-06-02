from abc import ABC, abstractclassmethod

# Initiating classes

class Shape2D(ABC):
  FAMILY = "2D"
    #assigning constant class attribute
  def init(self, name):
      self.name = ""

  @abstractclassmethod
  def calculate_area(self):
      return float(0.00)
      #return as float

class Rectangle(Shape2D):#inherit from Shape2D
  def __init__(self, name, length, width):#method
    self.name = str(name) 
    self.length = float(length) #instance attribute
    self.width = float(width)#instance attribute

  def __repr__(self):
      return "Name: {}\nLength:{}\nWidth:{}".format(self.name, self.length, self.width)#formal string representation

  def __str__(self):
      return f'I am a {self.name} and I am {self.length} long and {self.width} wide.'#informal string representation

  def calculate_area(self):
      return self.length * self.width #instance method to calculate_area note that
      # it will return float since both #instance attributes are float


class Triangle(Shape2D):#inherit from Shape2D
  def __init__(self, name, base, height):
      self.name = str(name) 
      self.base = float(base)#instance attribute
      self.height = float(height)#instance attribute

  def __repr__(self):
      return "Name: {}\nBase:{}\nHeight:{}".format(self.name, self.base, self.height)#formal string representation

  def __str__(self):
      return f'I am a {self.name} and I am {self.base} wide and {self.height} tall.'#informal string representation

  def calculate_area(self):
      return float(0.5 * self.base * self.height) 
       #instance method to calculate_area note that
      # it will return float since both #instance attributes are float

class Square(Rectangle):#inherit from Rectangle
  def __init__(self, name, length):
      self.name = str(name) 
      self.length = float(length)#instance attributes
    
  def __repr__(self):
      return "Name: {}\nLength:{}".format(self.name, self.length)
      #formal string representation
  def __str__(self):
      return f'I am a {self.name} and I am {self.length} long and wide.'
      #informal string representation
  def calculate_area(self):
      return float(self.length * self.length) 
      #instance method to calculate_area note that
      # it will return float since both #instance attributes are float

# Testing 
"""if __name__ == "__main__":
  square = Square("Aagash",100.00)
  print(square.calculate_area())

  triangle = Triangle("Drako",15.00, 20.00)
  print(triangle.calculate_area())"""