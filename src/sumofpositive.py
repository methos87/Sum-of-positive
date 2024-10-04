def positive_sum(arr):
	result = 0	
	for i in range(len(arr)):
		if arr[i] >= 0:
			result += i
		else:
			result += 0
	return resutl

positive_sum([1, 2, 3, 4, 5]) # 15
