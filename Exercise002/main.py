def get_int():
	flag = True
	value = 0
	while flag:
		try:
			value = int(input("Enter your value: "))
			return value
		except ValueError:
			print('Error. Please enter correct digit! ', end='')


def get_sum(number1, number2):
	return number1 if number2 == 0 else get_sum(number1 + 1, number2 - 1)
	

value1 = get_int()
value2 = get_int()
print(f'Sum of {value1} + {value2} = {get_sum(value1, value2)}')

