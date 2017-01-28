# (1) A reversi number is a number that reads the same forwards and backwards, such as 303. 
# The largest reversi number that is a product of two 2-digit numbers is 9009 = 91 x 99.

# Write a Python program to find the largest reversi number that is a product of two 3-digit numbers.

# Your output format should be "abc x def = ghiihg" (where the letters are replaced by digits).

# Traditional Method
def find_reversi():
	# Creates a list of the products of two 3-digit numbers. Returns the largest reversi within list.
	products = {} # products of 3-digit numbers
	for number in range(100, 1000):
		for other_number in range(100, 1000):
			product = number * other_number
			if is_reversi(product):
				products[product] = str(number) + " x " + str(other_number)
	max_reversi = max(products.keys())
	print(products[max_reversi] + " = " + str(max_reversi))

def is_reversi(product):
	# Checks whether a number is a reversi.
	str_product = str(product)
	return str_product == str_product[::-1]

##########################################################################################

# Main
def main():
	find_reversi()

if __name__ == '__main__':
	main()
