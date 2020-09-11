class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        k = set()
        l = []
        for i in range(1,n):
            for j in range(i+1,n+1):
                if i/j in k:
                    continue
                k.add(i/j)
                l.append(str(i)+"/"+str(j))
    
        return l
