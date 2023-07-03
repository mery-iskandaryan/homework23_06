import math
def power_of(n):
	def power(x):
		return(x**n)
	return(power(x))

x = float(input('Enter a number to calculate its n-th power: '))
n = float(input('Enter a number(power): '))

print(power_of(n))