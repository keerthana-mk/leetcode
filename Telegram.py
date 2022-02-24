class Solution:
    def telegram(self,str,n):
        new_string =[]
        for i in range(0,len(str),n):
            if str[n + i] is not " ":
                new_string.append(str[i:n+i])
            else:
                trim
        print(new_string)
s = Solution()
n =15
str ="The quick brown fox jumped over the lazy dog"
s.telegram(str,n)