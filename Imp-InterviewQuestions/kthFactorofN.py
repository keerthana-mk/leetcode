# https://leetcode.com/problems/the-kth-factor-of-n/
# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
#
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list
# or return -1 if n has less than k factors.
#
# Example
# 1:
#
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factorslist is [1, 2, 3, 4, 6, 12], the3rdfactor is 3.
# Example 2:
#
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# Example3:
#
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors.We should return -1.
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors =[]
        print("n=",n)
        for i in range(1,n+1):
            if n%i==0:
                print(" i=",i)
                factors.append(i)
        # print(factors,len(factors))
        return factors[k-1] if k <= len(factors) else -1
'''
############################################################
'''
Approach 2: Heap, \mathcal{O}(\sqrt{N} \times \log{k})
Algorithm

Initialize max heap. Use PriorityQueue in Java and heap in Python. heap is a min-heap. Hence, to implement max heap, change the sign of divisor before pushing it into the heap.

Iterate by xx from 11 to \sqrt{N}:
If xx is a divisor of NN, push xx and its pair divisor n / xn/x into the heap of size kk.
Return the head of the heap if its size is equal to kk and -1−1 otherwise.
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # push into heap
        # by limiting size of heap to k
        def heappush_k(num):
            heappush(heap, - num)
            if len(heap) > k:
                heappop(heap)
            
        # Python heap is min heap 
        # -> to keep max element always on top,
        # one has to push negative values
        heap = []
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                heappush_k(x)
                if x != n // x:
                    heappush_k(n // x)
                
        return -heappop(heap) if k == len(heap) else -1 
Approach 3: Using Math, O(srt(N)) time complexity ; Space Complecity: O(min(k,sqrt(N))

Algorithm

Initialize a list divisors to store the divisors.

Iterate by x from 11 to \sqrt{N} 
N. If xx is a divisor of N, decrease k by one. Return x if k == 0.
We're here because the kth divisor is not yet found. Although divisors already contains all "independent" divisors. All other divisors are "paired" ones, 
i.e, the kth divisor could be computed as N / divisors[len(divisors) - k].

But before that, we need a small correction for the case when N is a perfect square. In that case, the divisor list contains a duplicate because \sqrt{N} 
N appears two times. To skip it, we have to increase kk by one.

Return N / divisors[len(divisors) - k] if k <= len(divisors) and -1 otherwise.

'''


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                k -= 1
                factors.append(i)
                if k == 0:
                    return i

        # if n is a perfect square there will be duplicate factors
        if int(n ** 0.5 * n ** 0.5) == n:
            k += 1
        return n // factors[len(factors) - k] if k <= n else -1


s = Solution()
n = 7
k = 2
print(s.kthFactor(n, k))
