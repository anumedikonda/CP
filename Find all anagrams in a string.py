class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #ws=windowSize iS=iterSize
        wS=len(p)
        srcSize=len(s)
        if wS>srcSize:
            return []
        iS=srcSize - wS+1
        i=0
        p=sorted(p)
        res=[]
        while iS:
            x=s[i:wS+i]
            x=sorted(x)
            if x==p:
                res.append(i)
            iS-=1
            i+=1
        return res
