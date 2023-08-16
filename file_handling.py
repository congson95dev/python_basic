file = open('/var/www/html/pythonlearning/test.py', 'w');
file.write('this is a test')
file.close();

with open('/var/www/html/pythonlearning/test.py', 'w') as file2:
	file2.write('this is a test 2')

import json
dict1 = {'a' : 1, 'b' : 2}
# w+ Mean read and write. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
with open('/var/www/html/pythonlearning/test.py', 'w+') as file3:
	# file3.write(str(dict1)) # write as a string
	file3.write(json.dumps(dict1)) # write as a json

# r+ mean read and write.
with open('/var/www/html/pythonlearning/test.py', 'r+') as file4:
	# content4 = file4.read() # read a string file
	content4 = json.load(file4) # read a json file
	print(content4)