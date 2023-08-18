class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	"""
	using getter and setter to handle the validate
	"""
	@property
	def width(self):
		return self._width # with this, it's actually not return the width, but return the _width
	
	@width.setter
	def width(self, width):
		if width < 10:
			raise ValueError("Width must be > 0")
		self._width = width

	# we can do the same setter and getter for height

	def area(self):
		return self.width * self.height
	
	def __str__(self):
		return "Rectangle str method, width: {0}, height: {1}".format(self.width, self.height)

	def __repr__(self):
		return "Rectangle repr method"
	
	def __eq__(self, other):
		if isinstance(other, Rectangle):
			return self.width == other.width and self.height == other.height
		return False
	
	def __lt__(self, other): # or __gt__ for greater than
		if isinstance(other, Rectangle):
			return self.area() < other.area()
		return False

r1 = Rectangle(10, 20)

print(r1.area())

print(r1) # this will trigger __str__ or __repr__ depend on which one is avaiable, it's prority more for __str__
print(str(r1)) # same as above

r2 = Rectangle(10, 20)
print(r1 is r2) # this will trigger __eq__, result: False, because although it's the same Class with the same value, but it's in difference memory
print(r1 == r2) # this will trigger __eq__, result: True, because it's have the same Class with the same value

r3 = Rectangle(100, 200)
print(r1 < r3) # this will trigger __lt__, result: True

# test setter and getter
r4 = Rectangle(100, 200)
print(r4) #before setter, result: Rectangle(100,200)
r4.width = 10 # setter
print(r4) # getter, result: Rectangle(10,200)
r4.width = -100 # setter, result: throw ValueError

r5 = Rectangle(-100, 20) # result: throw ValueError, because it's affected by validate we write in setter
