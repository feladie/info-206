# Imports
import string
import getpass

##########################################################################

# Body

def user_input():
	"""Prompts the user for and returns a password."""
	return getpass.getpass("Create Password: ")

def check_conditions(password):
	"""Checks which of the four conditions have been met by the user's password."""
	count = 0;	# Number of conditions that have been met
	condition_met = []	# A list to store messages for the conditions that have been met
	condition_notmet = []	# A list to store the messages for the conditions that have not been met
# It must contain at least one uppercase and one lowercase letter:
# Source: http://stackoverflow.com/questions/17140408/if-statement-to-check-whether-a-string-has-a-capital-letter-a-lower-case-letter
	if any(character.isupper() for character in password):
		count += .5
		condition_met.append('CONTAINS at least one uppercase letter.')
	else:
		condition_notmet.append('NEEDS at least one uppercase letter.')
	if any(character.islower() for character in password):
		count += .5
		condition_met.append('CONTAINS at least one lowercase letter.')
	else:
		condition_notmet.append('NEEDS at least one lowercase letter.')
# It has at least one digit
	if any(character.isdigit() for character in password):
		count += 1
		condition_met.append('CONTAINS at least one digit.')
	else:
		condition_notmet.append('NEEDS at least one digit.')	
# It has at least one character that is not a letter or a digit
	special_char = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	if any(character in password for character in special_char):
		count += 1
		condition_met.append('CONTAINS at least one character that isn\'t a letter or a number.')
	else:
		condition_notmet.append('NEEDS at least one character that isn\'t a letter or a number.')
# It has a length of at least six characters
	if len(password) >= 6:
		count += 1
		condition_met.append('CONTAINS At least 6 characters.')
	else:
		condition_notmet.append('NEEDS at least 6 characters.')
# Output which strength of password:
	password_strength(count)
# Output which conditions are met or not met:
	for item in condition_met:
		print(item)
	for item in condition_notmet:
		print(item)
# Check if user password is in 'common.txt':
	try:
		in_common(password, common_list())
	except:
		print('\'common.txt\' could not be found.')

def password_strength(conditions):
	"""Checks the strength of user password. Prints the strength of each password."""
# If exactly no conditions are met: report that the password is "very weak":
	if conditions < 1:
		print('Password is very weak.')
# If exactly one condition is met: report that the password is "weak":
	elif conditions < 2:
		print('Password is weak.')
# If exactly two conditions are met: report that the password is "medium strength":
	elif conditions < 3:
		print('Password is medium strength.')
# If exactly three conditions are met: report that the password is "strong":
	elif conditions < 4:
		print('Password is high medium strength.')
	elif conditions >= 4:
		print('Password is strong.')

def create_passwords():
	"""Prompts the user for a password until the user types 'finish'"""
	# Souce for whitespace: https://docs.python.org/3.4/library/string.html
	password = user_input()
	while password != 'finish':
		if password == 'finish':
			break
		elif any(character in string.whitespace for character in password):
			print("Invalid password. Contains whitespace.")
			password = user_input()
		elif password == '':
			print("Invalid password. Try again.")
			password = user_input()
		else:
			check_conditions(password)
			password = user_input()

def common_list():
	"""Places each string in common.txt into a list and returns the list."""
	result = []
	with open('common.txt', 'r') as f:
		lines = f.readlines()
		for word in lines:
			result.append(word.strip())
		return result

def in_common(password, lst):
	"""Checks whether the given password is in common.txt."""
# Change all capital letters in the users password to lower case letters:
	lowercase_password = password.lower()
# Use the binary search algorithm to search whether the user's password is in the list of commont passwords:
	minimum = 0
	maximum = len(lst) - 1
	count = 0
	mid = minimum + (maximum - minimum) // 2
	search = lst[mid]
	warning = 'Warning: Your password is a common password.'

	while maximum - minimum > 1:
		count += 1
		if lst[mid] == lowercase_password:
			print(warning)
			print('Number of binary search comparisons: {}'.format(count))
			break
		elif lowercase_password < lst[mid]:
			maximum = mid - 1
			mid = minimum + (maximum - minimum) // 2
		elif lowercase_password > lst[mid]:
			minimum = mid + 1
			mid = minimum + (maximum - minimum) // 2
	else:
		count += 1
		if lst[minimum] == lowercase_password:
			print(warning)
		elif lst[maximum] == lowercase_password:
			count += 1
			print(warning)
		else:
			count += 1
			print('Not a common password.')
		print('Number of binary search comparisons: {}'.format(count))

##########################################################################################

# Main
def main():
	create_passwords()

if __name__ == '__main__':
	main()