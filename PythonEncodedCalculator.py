# PythonEncodedCalculator.py
#
# This is a Python Encoded Calculator
# This program will do some mathematical calculations when using certain symbols as operators
# This program will continue until the user decides to exit the program
#
# Victor Tang	301281945	vwt5
# June 2017



# This sets the condition 'userON' to be true at the start of the program
userON = True


# Simple greeting to the program 
print ("Welcome to my Python Encoded Calculator!")


# Loop this program until 'userON' is no longer true
# The condition to change 'userON' as False will be when the user enters 'x' or 'X'
while userON:


# This print statement is split just so it is easier for me to read
# Every operator introduction begins indented in a new line
	print ("""\nThis Python Encoded Calculator can
			add: use the symbol $,
			subtract: use the symbol &,
			multiply: use the sybmol @,
			divide: use the symbol ?(result is a float),
			to find remainder: use the symbol !\n"""
		"The equation you enter must follow this syntax:\n\t"
		"<operand><space><operator><space><operand>.\n"
		"An <operand> is any interger you wish.\n"
		"An <operator> is any of the above 5 encoded operators this calculator can deal with.\n"
		"A <space> is a white space character.\n\n")


# Variable 'userInput' will be what the user enters
# If a valid equation is entered, the equation will be executed 
	userInput = input("\nPlease enter your equation below. If you wish to exit, please enter 'X' or 'x': \n")


# Shows what the user has entered
	print("\nThe equation you have entered is '{}'. \n".format(userInput))


# Split the information entered by the user into list of values
	userInput.split()


# Create a new variable called 'userEquation' which holds the value of the split 'userInput'
	userEquation = userInput.split()


# If either 'x' or 'X' is entered, the condition 'userON' will be set to False, which will terminate the loop this program is in
# When the user decides to cease further iteration of the calculator, the program will say 'BYE' to the user
	if userInput == 'X' or userInput =='x':
		userON = False
		print("\n\n~~~ BYE ~~~")


# If the user entered nothing and simply pressed the ENTER key, program will instruct to try again
	elif len(userEquation) == 0:
		if userInput == '':
			print("Have you simply pressed the Enter key? Please enter an equation next time! :)")


# If there is only one value in what the user entered
	elif len(userEquation) == 1:
		

# If the value the user entered is just one of the operater shown to the user by the program, user will be told to try again
		if userEquation[0] in ['$' or '&' or '@' or '?' or '!']:
			print("You have entered the equation '{}' which is not a complete equation since it only contains the operator {}.  Please try again.".format(userEquation[0], userEquation[0]))


# If the value the user entered is just a number, user will be told to try again
		elif userEquation[0].isdigit():
			print("You have entered the equation '{}' which is not a complete equation since it only contains the operand {}.  Please try again".format(userEquation[0], userEquation[0]))


# If the user entered value is neither number nor an operator symbol, the program assumes the user has entered a sequence of letters and the user will be instructed to try again
		else:
			print("You have entered the sequence of letters '{}'' which is not an equation. Please try again.".format("".join(userEquation)))	


# If there are 2 values in the equation the user entered
	elif len(userEquation) == 2:

		
# The user has not entered an equation according to the instructions provided.  The program will tell the user what they did wrong and give instruction to try again
		if userEquation[0].isdigit() and userEquation[1].isdigit():
			print("You have entered the equation '{} {}' which is not a complete equation since it only contains the operand {} and the operand {}. Please, try again.".format(userEquation[0], userEquation[1], userEquation[0], userEquation[1]))

		elif userEquation[0].isdigit() and userEquation[1] in ['$' or '&' or '@' or '?' or '!']:
			print("You have entered the equation '{} {}' which is not a complete equation since it only contains the operand {} and the operator {}. Please try again.".format(userEquation[0], userEquation[1], userEquation[0], userEquation[1]))

		elif userEquation[0] in ['$' or '&' or '@' or '?' or '!'] and userEquation[1].isdigit():
			print("You have entered the equation '{} {}' which is not a complete equation since it only contains the operator {} and the operand {}. Please try again.".format(userEquation[0], userEquation[1], userEquation[0], userEquation[1]))

		else:
			print("You have entered the equation '{} {}' which is not a complete equation since it only contains the operator {} and the operator {}. Please, try again.".format(userEquation[0], userEquation[1], userEquation[0], userEquation[1]))


# If the equation entered by the user has 3 values, then we execute the instructions in this section
	elif len(userEquation) == 3:


# Check if the first entered value and the third entered values are numbers.  
# If so, then convert them from string format into integer format where they will be able to be operated on mathetically
# Assingn the integer value into variables called 'operand_1' and 'operand_2'
		if userEquation[0].isdigit() and userEquation[2].isdigit():
			operand_1 = int(userEquation[0])
			operand_2 = int(userEquation[2])


# If the operator is one of the listed opeartor used in program, the user will be shown the equation they have entered and the result of the operation
# If operator is not listed in program, user will be asked to correct operator shown by the program
			if userEquation[1] == '$':
				print("The equation is {} = {}.".format(userInput, operand_1 + operand_2))
			elif userEquation[1] == '&':
				print("The equation is {} = {}.".format(userInput, operand_1 - operand_2))
			elif userEquation[1] == '@':
				print("The equation is {} = {}.".format(userInput, operand_1 * operand_2))
			elif userEquation[1] == '?':
				print("The equation is %s = %.2f" %(userInput, operand_1 / operand_2))
			elif userEquation[1] == '!':
				print("The equation is {} = {}".format(userInput, operand_1 % operand_2))
			else:
				print('Please enter an operator listed in the program')


# If the length of the user input is greater than 3 values, then the program will instruct the user to enter an equation within parameters of the user instructions. 
	else:
		print('Please enter an equation that follows the format in the instruction')