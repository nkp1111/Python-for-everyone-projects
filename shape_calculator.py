class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      display = ""
      for i in range(self.height):
        for j in range(self.width):
          display += "*"
        display += "\n" 
    return display

  def get_amount_inside(self, shape):
    other_width, other_height = shape.width, shape.height
    rem_width, rem_height = self.width - other_width, self.height - other_height
    if (rem_width or rem_height) < 0:
      return 0 
    else:
      return self.get_area() // shape.get_area()

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
  def __init__(self, height):
    self.width = height
    self.height = height

  def set_side(self, height):
    self.width = height
    self.height = height

  def set_width(self, height):
    self.width = height
    self.height = height

  def set_height(self, height):
    self.width = height
    self.height = height

  def __str__(self):
    return f"Square(side={self.height})"
