class Solution:
    def myAtoi(self, s: str) -> int:
            if len(s) == 0: return 0
            ans = 0
            sign = 1
            number_started = False
            minNum = (-1) * (2 ** 31)
            maxNum = (2 ** 31 -1)
            
            for ch in s:
                
                if number_started == False:                    
                    if ch == ' ':
                        continue
                    if ch =='-':
                        number_started = True
                        sign = -1
                        continue
                    if ch == '+':
                        number_started = True
                        continue
                    if ch.isdigit():
                        number_started = True
                        
                if ch.isdigit():
                    ans = ans*10 + (ord(ch) - ord('0'))
                else:
                    break

            ans = sign * ans 
            
            if ans == 0:
                return 0   
            
            elif ans < minNum:
                return minNum
            
            elif ans > maxNum:
                return maxNum
            
            else:
                return ans
