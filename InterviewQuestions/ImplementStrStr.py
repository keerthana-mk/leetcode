# Pattern Matchiing Algorithm - KMP used here
# Implement strStr().
#
# strstr - locate a substring ( needle ) in a string ( haystack ).
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
        def computeLPS(self,A, m, lps):
            l = 0
            lps[0]
            i = 1

            while i < m:
                if A[i] == A[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l != 0:
                        l = lps[l - 1]
                    else:
                        lps[i] = 0
                        i += 1

        def strStr(self, A, B):
            m = len(B)
            n = len(A)

            lps = [0] * m
            j = 0

            self.computeLPS(B,m,lps)
            i = 0
            while i < n:
                if B[j] == A[i]:
                    i += 1
                    j += 1

                if j == m:
                    return i - j
                elif i < n and B[j] != A[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return -1


s = Solution()
A = "bbbbbbbbab"
B = "baba"
print(s.strStr(A, B))
