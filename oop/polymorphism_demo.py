class Shape:
  """
  A base class representing a geometric shape.
  """

  def area(self):
    """
    Abstract method to calculate the area of the shape.

    Raises:
      NotImplementedError: This method is not implemented in the base class and
        needs to be overridden by derived classes.
    """
    raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
  """
  A derived class representing a rectangle shape.
  """

  def __init__(self, length: float, width: float):
    """
    Initializes a Rectangle instance with length and width.

    Args:
      length: The length of the rectangle.
      width: The width of the rectangle.
    """
    self.length = length
    self.width = width

  def area(self):
    """
    Calculates and returns the area of the rectangle.

    Returns:
      The area of the rectangle (length x width).
    """
    return self.length * self.width


class Circle(Shape):
  """
  A derived class representing a circle shape.
  """

  def __init__(self, radius: float):
    """
    Initializes a Circle instance with radius.

    Args:
      radius: The radius of the circle.
    """
    self.radius = radius

  def area(self):
    """
    Calculates and returns the area of the circle.

    Returns:
      The area of the circle (pi * radius squared).
    """
    import math
    return math.pi * self.radius * self.radius
