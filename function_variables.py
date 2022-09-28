'''
Exercise of how variables work with functions
'''

my_variable = 'Alan'

# What what is the value of my_variable at this point?

def test_function(my_variable):
	my_variable = 'Bob'
	return my_variable

# What what is the value of my_variable at this point?

test_function(my_variable)	

# What what is the value of my_variable at this point?

test_function('John')

# What what is the value of my_variable at this point?

my_variable = test_function('Hector')

# What what is the value of my_variable at this point?

print("My name is", my_variable)	

''' 
============================ Explanation ============================
'''

my_variable = 'Alan' # Set the variable to 'Alan'.  Easy!

def test_function(my_variable): # Declare our function (good coding practice would have functions before any other code in same-file)
	# Note that my_variable is passed as a value (copy of the variable), not as a reference (actual variable).  test_function(other_variable) would still be test_function('Alan')

	my_variable = 'Bob'			# Assign a new value to the variable.  other_variable='Bob' would do the same thing if we were using test_function(other_variable)
	return my_variable			# Passes the value of the variable back out of the function 


test_function(my_variable)		# Since the function wasn't run yet, we're passing 'Alan' at this point.  my_variable doesn't change.  The function returns 'Bob' but it isn't assigned to anything at this line

test_function('John')			# Can pass a value to the function instead of a variable.

my_variable = test_function('Hector')  # This assigns the return value of the function to my_variable, which would = 'Bob' since the value changes in the function


print("My name is", my_variable)	# My name is Bob
