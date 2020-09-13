class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) ; m = len(matrix[0]) ; c = set({})  ; r = set({})

        for j in range(m) :
            for i in range(n):
                if matrix[i][j] == 0 :
                    c.add(j)
                    r.add(i)
        for j in c :
            for i in range(n):
                matrix[i][j] = 0
                if i in r :
                    matrix[i] = [0]*m
                    r.remove(i)
