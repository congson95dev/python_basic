class Human:
	species = "H.Sapiens"

	def __init__(self, name): # __init__, co 4 dau gach duoi
		self.name = name
		self._age = 0

	def say(self, message):
		print("{name} : {message}".format(name = self.name, message = message))

	def sing(self):
		print("this is a sing function")
