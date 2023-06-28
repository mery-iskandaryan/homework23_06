import math
def calculate_area(radius):	
	'''Takes in the radius of a circle, returns the area of the circle'''
	while radius < 0:
		radius = float(input('Enter a positive number: '))
	pi = math.pi
	return(pi * radius * radius)

radius = float(input('Enter the radius of the circle: '))
print(f'The area of the circle is {calculate_area(radius)}.')