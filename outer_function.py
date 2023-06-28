def outer_function(x):
	def inner_function(factor):
		return(x*factor)
	print(inner_function(float(input('Enter a factor: '))))

x = float(input('Enter a number: '))
outer_function(x)