class Solution:
    def balancedStringSplit(self, s: str) -> int:
        RLtag = 0
        Total = 0
        for i in s:
            if i == 'R':
                RLtag = RLtag + 1
            else:
                RLtag = RLtag - 1
            if RLtag == 0:
                Total = Total + 1
        return Total
