class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        l=len(s)
        res = 0

        for i in range(l-k+1):
            a = int(s[i:i+k])
            if a != 0 and num % a == 0: 
                res+=1
        return res
           
