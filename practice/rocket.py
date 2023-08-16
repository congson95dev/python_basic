import json

from spaceship import SpaceShip

class Rocket(SpaceShip):
	def __init__(self, weight, max_weight):
		self.weight = weight
		self.max_weight = max_weight
		super().__init__()
	def launch(self): # must have self
		chance_to_launch = 100 - 5 * float(self.weight) / (float(self.max_weight) - float(100)) # missing rocket weight, so i will set it as 100
		if (chance_to_launch > 0):
			return True
		return False

def load_item(text_file):
	with open(text_file, 'r+') as file:
		content = file.read()
		# format str to json by using json.loads
		dictresult = json.loads(content)
		return dictresult

cargoDict = load_item('/var/www/html/pythonlearning/practice/cargo2.txt')
for cargo in cargoDict:
	cargoItem = Rocket(cargoDict[cargo]['weight'], cargoDict[cargo]['max_weight'])
	result = cargoItem.launch()
	print(result)