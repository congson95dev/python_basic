import json

class Item:
	def __init__(self, name, cargo_weight):
		self.name = name
		self.cargo_weight = cargo_weight

	def readData(self):
		print('read cargo successfully! Data:')
		print('{name} : {cargo_weight}'.format(name = self.name, cargo_weight = self.cargo_weight))

def readFile(fileName):
	with open(fileName, 'r+') as file:
		content = file.read()
		# format str to json by using json.loads
		dictresult = json.loads(content)
		return dictresult

cargoDict = readFile('/var/www/html/pythonlearning/practice/cargo1.txt')
for cargo in cargoDict:
	cargoItem = Item(cargoDict[cargo]['name'], cargoDict[cargo]['weight'])
	cargoItem.readData()


