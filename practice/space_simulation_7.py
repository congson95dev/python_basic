import random

weight = input('Enter Weight:');
max_weight = input('Enter Max Weight:');
cargo_weight = input('Enter Cargo Weight:');

def launch(weight, max_weight, cargo_weight):
	chance_to_launch = random.uniform(0, 100) - 5 * float(cargo_weight) / (float(max_weight) - float(weight))
	if (chance_to_launch > 0):
		return True
	return False

try:
	chance_to_launch = launch(weight, max_weight, cargo_weight)
	if (chance_to_launch) :
		print ('launch successfully')
	else :
		print ('launch failed')
except Exception as e:
	print ('Something went wrong, issue: ' + str(e))