class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = x
        rev = 0
        while x > 0:
            # print("am i coming here")
            d = x % 10
            rev = rev * 10 + d
            x //= 10
        difference = rev - x
        # print(rev, x, type(rev))
        if y == rev:
            # print("hi")
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(x=121))
