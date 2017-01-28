def daily_rainfall():
	"""Reads in rainfall.txt. Returns a list of the first element (i.e. a sequence of strings before the first space)
	of each line in the file. If a line begins with whitespace, it is not added to the returned list.
	Ignores elements that aren't real numbers or integers.
	"""
	result = []
	with open('rainfall.txt', 'r') as f:	# Read file
		list_of_lines = f.readlines()
		for line in list_of_lines:
			list_of_elements = line.split(" ")
			rainfall = list_of_elements[0]
			try:
				rainfall = float(rainfall)	# Check if the first element of the list is a real number
			except:
				continue
			else:
				result.append(rainfall)	# add to result list
	return result


def compute_average(lst):
	"""Computes the average of the daily rainfalls by reading in a list of those rainfalls.
	Outputs the average or an error message.
	If the list is empty, begins with a -999, or doesn't contain valid real numbers, outputs an error message.
	Ignores negative numbers within the list of daily rainfalls.
	Begins the calculation for the average when the end of the list is reached
	or when the list index has a value of -999.
	"""
	lst_length = len(lst)
	total = 0	# sum of daily rainfalls
	count = 0	# number of valid daily logs
	message = 'There are no valid rainfall inputs'	# Error message
	if lst_length > 0:
		if lst[0] != -999:	
			for item in lst:
				if item == -999:
					break
				elif item >= 0:
					total += item
					count += 1
			if count > 0:
				if total % count == 0:
					average = int(total / count)
				else:
					average = total / count 
				message = 'Average rainfall = {} inches'.format(average) 
	print(message) 


##############################################################################
def main():
	compute_average(daily_rainfall())

if __name__ == '__main__':
	main()