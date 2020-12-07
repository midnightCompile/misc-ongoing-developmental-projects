# Minimize Sum Of Array (Array Series#1)
#
# Task:
# Given an array of integers, find the minimum sum which is obtained
# from summing each two integers product.
#
# Notes:
# --Array/list will contain positives only
# --Array/list will always have even size

# Function to obtain minimum sum of array
def min_sum(arr):
    arr.sort()
    end = len(arr)-1
    min = 0
    i = 0
    while i < end:
        min += arr[i]*arr[end]
        i += 1
        end -= 1
    return min