x = 10
def my_function():
	global x
	print(f'This is global variable: {x}')
	x = 20
	print(f'This is local variable: {x}')
	

my_function()