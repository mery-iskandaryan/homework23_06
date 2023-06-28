counter = 0
def increment_counter():
	global counter;
	counter += 1
	return(counter)

print(f'Global counter is {counter}')
print(f'Local counter is {increment_counter()}')

print(f'Global counter is {counter}')
print(f'Local counter is {increment_counter()}')

print(f'Global counter is {counter}')
print(f'Local counter is {increment_counter()}')
