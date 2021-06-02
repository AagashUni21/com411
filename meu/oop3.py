from abc import ABC

class Shape2D(ABC):
  FAMILY = "2D"

  def __init__(self, name = "Shape2D"):
    self.name = none
  


class Rectangle(Shape2D):
  
  def __init__(self, name = "Rectangle"):
    super().__init__(name)
  
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def __repr__(self):
    return f'Rectangle(name = {self.name}, length={self.length}, width={self.width})'

  def __str__(self):
    return f'I am a {self.name} and I am {self.length} long and {self.width} wide.'

  def calculate_area:
    area = self.length*self.width
    return area
  
class Triangle(Shape2D):
  
  def __init__(self, name = "Triangle"):
    super().__init__(name)
  
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def __repr__(self):
    return f'Rectangle(name = {self.name}, base={self.base}, height={self.height})'

  def __str__(self):
    return f'I am a {self.name} and I am {self.base} wide and {self.height} tall.'

  def calculate_area:
    area = 0.5*self.length*self.width
    return area

class Square(Rectangle):
  
  def __init__(self, name = "Square"):
    super().__init__(name)
  
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def __repr__(self):
    return f'Square(name = {self.name}, length={self.length}, width={self.width})'

  def __str__(self):
    return f'I am a {self.name} and I am {self.length} long and {self.width} wide.'
