#!/usr/bin/env python


def positive_sum(arr):
	result = 0	
	for i in arr:
		if i >= 0:
			result += i
		else:
			result += 0
	return result




