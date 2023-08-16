weight = input('Enter Weight:');
max_weight = input('Enter Max Weight:');
cargo_weight = input('Enter Cargo Weight:');

sum_of_cargo_weight = 4000 + 9000 + float (cargo_weight)

try:
	chance_of_explosion = 5 * float(sum_of_cargo_weight) / (float(max_weight) - float(weight))
	dictresult = {
		'weight': weight, 
		'max_weight': max_weight,
		'sum_of_cargo_weight': sum_of_cargo_weight,
		'chance_of_explosion': chance_of_explosion
	}

	if (chance_of_explosion > 0) :
		print ('chance of explosion: ' + str(chance_of_explosion))
		print ('dictionary to store all data: ')
		print (dictresult)
	else :
		print ('chance of explosion is less than 0')
except Exception as e:
	print ('Something went wrong, issue: ' + str(e))