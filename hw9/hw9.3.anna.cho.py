

# Reads in the file, returns a nested list of numbers.
def read_file(input):
	result = []
	try:
		with open(input, 'r') as f:
			lines = f.readlines()
			for line in lines:
				line = line.strip()
				numbers = line.split()
				for i in range(len(numbers)):			
					numbers[i] = int(numbers[i])
				result.append(numbers)
		return result
	except:
		print('File could not be opened.')

def get_sub_tri(row, triangle, lst=[]):
	if len(triangle) == 0:
		return [0]
	elif row  == 0: # Top of triangle
		if len(lst) > 0: 
			last_number = [triangle[row][0]]
			for item in lst[0]:
				last_number.append(item)
			lst = last_number
		else: # If triangle only contains one number
			lst.append(triangle[row][0]) 
		return lst
	elif row == len(triangle) - 1: # Bottom of triangle
		numbers = triangle[row]
		for number in numbers:
			lst.append([number])
		return get_sub_tri(row-1, triangle, lst)
	else: # Middle of triangle
		size = len(triangle[row])
		new_lst = []
		for item in range(size):
			a = lst[item]
			b = lst[item + 1]
			choice = [triangle[row][item]]
			if sum(a) >= sum(b):
				for items in a:
					choice.append(items)
			else:
				for items in b:
					choice.append(items)
			new_lst.append(choice)
		return get_sub_tri(row-1, triangle, new_lst)

# Prints the sum and the path in the specified format.
def print_result(lst):
	size = len(lst)
	total = sum(lst)
	result = ''
	for index in range(size - 1):
		result += "{} + ".format(lst[index])
	result += '{} = {}'.format(lst[-1], total)
	print(result)


##########################################################################################

# Main
def main():
	test = (read_file('maxtriangle.txt'))
	result = get_sub_tri(len(test)-1, test)
	print_result(result)

if __name__ == '__main__':
	main()