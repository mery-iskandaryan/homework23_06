def outer_function(x):
	def inner_function(factor):
		return(x*factor)
	return(inner_function(factor))

x = float(input('Enter a number: '))
factor = float(input('Enter a number(factor): '))
print(outer_function(x))