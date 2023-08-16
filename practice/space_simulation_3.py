weight = input('Enter Weight:');
max_weight = input('Enter Max Weight:');
cargo_weight = input('Enter Cargo Weight:');

try:
	chance_of_explosion = 5 * float(cargo_weight) / (float(max_weight) - float(weight))

	if (chance_of_explosion >= 110) :
		print ('Launch failed')
	else :
		print ('Launch successfully')
except Exception as e:
	print ('Something went wrong, issue: ' + str(e))