# 7. Reverse Integer
# Python
# Time: 25ms
# Memory: 13.5MB

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = int(x * (-1))
        s = str(x)
        ans = str(int(s[::-1]))
        if neg:
            ans = "-"+ans
        n = int(ans)
        if n < (-1)*(2**31) or n > (2**31)-1:
            return 0
        return n