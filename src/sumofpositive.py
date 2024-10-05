#!/usr/bin/env python


def positive_sum(arr):
	result = 0	
	for i in arr:
		if i >= 0:
			result += i
		else:
			result += 0
	return result


<<<<<<< HEAD

=======
print(positive_sum([-1, 2, 3, 4, -5])) # 9
print(positive_sum([])) # 0
print(positive_sum([0])) # 0
print(positive_sum([1, -2, 3, 4, 5])) # 13
>>>>>>> original

