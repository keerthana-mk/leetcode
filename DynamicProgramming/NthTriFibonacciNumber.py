# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
# Example
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
import time


class Solution:
    def tribonacci (self, n: int) -> int:
        fib_3 = [''] * 38
        fib_3[0],fib_3[1],fib_3[2]=0,1,1
        for i in range(3,n+1):
            fib_3[i]=fib_3[i-1]+fib_3[i-2]+fib_3[i-3]
        return fib_3[n]
        #
        # if n == 0 or n == 1:
        #     return n
        # if n == 2:
        #     return 1
        # fib_3[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        # return fib_3[n]


s = Solution()
starttime=time.time()
print(s.tribonacci(30))
endtime=time.time()
print("Final time:",endtime-starttime)
