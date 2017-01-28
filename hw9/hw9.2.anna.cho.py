from functools import reduce

# (2) Convert script (1) so that it uses functional programming 
# (e.g., list comprehension, map, reduce, and/or lambda), and has no if/while/for statements or recursion.

# List of all 3-digit numbers
three_dig_nums = range(100, 1000)

# Create a list of tuples containing combinations of three digit numbers
items = [(first,second) for first in three_dig_nums for second in three_dig_nums]

# Filter out the tuples that don't produce reversi
items = filter(lambda item: str(item[0] * item[1]) == str(item[0] * item[1])[::-1], items)
items = list(items)

# Map items to products
products = [item[0] * item[1] for item in items]

# Find the max product
max_product = max(products)

# Find the tuples that produce this product
max_item = filter(lambda item: item[0] * item[1] == max_product, items)
max_item = list(max_item)

# Print in the format "abc x def = ghiihg"
print("{} x {} = {}".format(max_item[0][0], max_item[0][1], max_product))