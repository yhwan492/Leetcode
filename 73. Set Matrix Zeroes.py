# 73. Set Matrix Zeroes
# Python
# Time: 116ms
# Memory: 14MB
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        pos_j = set()
        for i,row in enumerate(matrix):
            p_i = False
            for j,elem in enumerate(row):
                if elem == 0:
                    p_i = True
                    pos_j.add(j)
            if p_i:
                for j in range(len(row)):
                    matrix[i][j] = 0
        for j in pos_j:
            for i in range(len(matrix)):
                matrix[i][j] = 0