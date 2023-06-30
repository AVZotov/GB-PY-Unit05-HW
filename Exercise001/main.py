def get_pow(number1, number2):
	if number2 == 1:
		return number1
	else:
		return number1 * get_pow(number1, number2 - 1)


def get_int():
	flag = True
	result = 0
	while flag:
		try:
			result = int(input("Enter your value: "))
			return result
		except ValueError:
			print('Error. Please enter correct digit! ', end='')


value1 = get_int()
value2 = get_int()
result = get_pow(value1, value2)

print(f'Value {value1} in pow {value2} = {result}')
	