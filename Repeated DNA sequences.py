class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l_s=len(s)
        windowSize=10
        count=0
        tmp={}
        slidingWindowCount=l_s - windowSize +1
        index=0
        while slidingWindowCount>0:
            tmpstr=s[index:windowSize+index]
            if tmpstr in tmp:
                val=tmp[tmpstr]
                val+=1
                tmp[tmpstr]=val
            else:
                tmp[tmpstr]=1
            index+=1
            slidingWindowCount-=1
        res=[]
        for i ,j in tmp.items():
            if j>1:
                res.append(i)
        return res
