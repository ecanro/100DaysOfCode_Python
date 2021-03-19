from arts_pro import logo10


def add(num1, num2):
	return num1 + num2

def substract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2


operators = {
	"+": add,
	"-": substract,
	"*": multiply,
	"/": divide
}

#recursion: call a function itself
def calculator():
	print(logo10)
	num1 = float(input("What's the firts number?: "))
	for symbol in operators:
		print(symbol)
		
	#while loop for continue run the program
	should_continue = True

	while should_continue:
		operation_symbol = (input("Pick and operator from the lane above: "))
		num2 = float(input("What's the next number?: "))
		calculation_function = operators[operation_symbol]
		answer = calculation_function(num1, num2)

		print(f'{num1} {operation_symbol} {num2} = {answer}')
		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")== 'n':
			should_continue = False
			#print('New operation:')
			calculator()
		else:
			num1 = answer
calculator()
#other form, but low functional->:
# 		operation_symbol = (input("Pick another operation: "))
# 		num3 = int(input("What's the next number?: "))
# 		calculation_function = operators[operation_symbol]
# 		second_answer = calculation_function(firts_answer, num3)
# 		#second_answer = calculation_function(calculation_function(num1, num2), num3)

# 		print(f'{firts_answer} {operation_symbol} {num3} = {second_answer}')

