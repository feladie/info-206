from functools import reduce

#### Take a list of numbers, square each element

my_nums = [1, 2, 3, 4, 5]
new_my_nums = []

### Imperatively
for item in my_nums:
	item = item **2
	new_my_nums.append(item)


### Functionally
new_my_nums = map(lambda item: item * item, my_nums)
new_my_nums = list(new_my_nums) # Must set to a variable because list() function only can drain list object once.

### Functionally convert this list to a list of strings from ints
# new_my_nums = map(lambda item: str(item*item), my_nums)
# new_my_nums = list(map(str, new_my_nums))

### Functionally flip the digits on all of the strings
# new_my_nums = list(map(reversed, new_my_nums))
# new_my_nums = list(map(lambda item: "".join(reversed(item)), new_my_nums))

### Take your list of squared numbers and make a list of only the even ones

### Imperatively
my_even_list = []
for num in new_my_nums:
	if num % 2 == 0:
		my_even_list.append(num)

### Functionally
func_even_list = list(filter(lambda x: x % 2 == 0, my_even_list)) # Filter is just map for functions that return True or False.

### Combine the answers from the first two to create a list of even squares in one line



### Sum the list of even squares

### Imperatively
accumulator = 0
for value in my_nums:
	accumulator += value


### Functionally
sum_list = reduce(lambda a, x: a + x, my_nums) # must import reduce 

count_list = reduce(lambda a, x: a+1, my_nums, 0)	# set a to zero.

### Functionally find the length of the list of even squares
# accumulator = 0
# for item in my_nums:
# 	item_squared = item * item
# 	if item_squared % 2 == 0:
# 		accumulator += item_squared

sum = reduce(lambda a, x: a + x, filter(lambda x: x % 2 == 0, map(lambda x: x*x, my_nums)))
print(sum)								   

# s = sum([x for x in [1,2,3,4,5] if x*x % 2 == 0])

### Consider the following list of dictionaries (looks like JSON)
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

### What is the total height of those with heights provided


### Imperatively


### Functionally



# With a comprehension


### How would we do this if this were a list of tuples instead?

people_tuples = [('Mary', 160), ('Isla', 80), ('Sam',)]

