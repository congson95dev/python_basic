from class1 import Human

class Superhero(Human):
	def __init__(self, name, power=["power1", "power2"]):
		self.power = power
		super().__init__(name) # don't call self in this function
