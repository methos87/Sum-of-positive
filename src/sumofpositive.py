#!/usr/bin/env python


def positive_sum(arr):
    return sum(filter(lambda i: i > 0, arr))


print(positive_sum([1, 2, 3, 4, 5])) # 15

