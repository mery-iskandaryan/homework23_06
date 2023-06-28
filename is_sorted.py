def is_sorted(ls):
	'''Takes in a list, returns 'True' if the list is sorted, 'False' otherwise'''
	counter = 0
	for i in range(len(ls)):
		if i != len(ls)-1:
			if ls[i] > ls[i+1]:
				pass
			else:
				counter +=1
	print('True' if counter == len(ls)-1 else 'False')

ls = input('Enter a list: ')
ls = ls.split(',')
is_sorted(ls)
