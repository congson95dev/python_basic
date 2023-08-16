import json
with open('/var/www/html/pythonlearning/practice/cargo1.txt', 'r+') as file:
	content = file.read()
	print(content)
	# format str to json by using json.loads
	dictresult = json.loads(content)
	print(dictresult)
	print(type(dictresult))