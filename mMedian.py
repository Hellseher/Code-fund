# Median

#A median is a numerical value separation the half of a list of numbers
# from the lower half. In a list where there are an odd number of entities,
# the median is the number found in the middle of the list. If the list
# contains an even number of entities, then there is no single middle value,
# instead the median empty becomes the average of the two numbers found in 
# the middle. For this mission, you are given a non-empty list of natural
# numbers (X). With it, you must separate the upper half of the numbers from 
# the lower half and find the median.
 

def checkiO(data):
	data_copy = data[:]
	data_copy.sort()
	total = len(data_copy)
	half = abs(total / 2)
	print data_copy
	if total % 2 != 0: return data_copy[half]
	else: return (data_copy[half - 1] + data_copy[half]) / 2.0
		
	return data_copy
	
print checkiO([3, 6, 20, 99, 10, 15, 2, 1])
