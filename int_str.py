def int_str(num):
	'''Takes in an integer, returns the name of the integer in English'''
	if num < 1015:
		num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
			5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
			11: 'eleven', 12: 'twelve', 13: 'thirteen', 14 : 'fourteen',
			15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
			19 : 'nineteen', 20 : 'twenty',30 : 'thirty', 40 : 'forty',  
			50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety',1000: 'thousand'}
		if num <= 20:
			return(num_dict[num])

		elif num < 100:
			if num % 10 == 0:
				return(num_dict[num])
			else: 
				return(num_dict[num//10*10] + ' ' + num_dict[num%10])
		elif num < 1000:
			if num % 100 == 0:
				return(num_dict[num//100] + ' ' + 'hundred')
			else:
				return(num_dict[num//100] + ' ' + 'hundred' + ' ' + int_str(num-((num//100)*100)))
		elif num == 1000:
			return(num_dict[1000])
		else:
			return('one' + ' ' + snum_dict[1000] + ' ' + int_str(num-1000))
		


num = int(input('Enter a number below 1015: '))
print(int_str(num))
 
		