# Python3 program for the above approach

# Function to calculate required
# maximum subarray sum
import sys


def maxSumSubarray(arr, k):
	maxSum = -sys.maxsize
	for i in range(len(arr)-k+1):
		map = {}
		unique = True
		for j in range(i, i+k):
			if arr[j] in map:
				unique = False
				break
			map[arr[j]] = True
		if unique:
			print(len(map))
			maxSum = max(maxSum, sum(map.keys()))
	return maxSum


# Driver Code
if __name__ == '__main__':

	# Given array arr[]
	# 1 2 3 7 3 5
	arr = [ 1, 2, 3, 7, 3, 5 ]

	# Function call
	ans = maxSumSubarray(arr, 3)

	# Print the maximum sum
	print(ans)

# This code is contributed by mohit kumar 29
