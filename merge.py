def sort_list(ls):
	count = 0
	while count < len(ls) - 1:
		count = 0
		for i in range(len(ls)):
			if i != len(ls)-1:
				if ls[i] > ls[i+1]:
					temp  = ls[i+1]
					ls[i+1] = ls[i]
					ls[i] = temp
				else:
					count+=1
	return(ls)

def merge(ls1, ls2):
	for item in ls1:
		ls2.append(item)
	ls2 = sort_list(ls2)
	print(ls2)
	

ls1 = input('Enter the fist list: ')
ls1 = sort_list(ls1.split(','))
ls2 = input('Enter the second list: ')
ls2 = sort_list(ls2.split(','))

merge(ls1,ls2)