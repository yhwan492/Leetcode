# 120. Triangle
# Python
# Time: 53ms
# Memory: 17.1MB
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memo = {}
        def dp(val,i,depth):
            if depth == len(triangle):
                return val
            if (i,depth) in memo:
                return memo[(i,depth)]
            total_min = 0
            result = min(val+dp(triangle[depth][i],i,depth+1),val+dp(triangle[depth][i+1],i+1,depth+1))
            memo[(i,depth)] = result
            total_min += result
            return total_min
        return dp(triangle[0][0],0,1)