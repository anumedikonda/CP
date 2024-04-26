class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l_s=len(s)
        windowSize=maxSize
        d={}
        while windowSize>=minSize:
            slidingWindowCount=l_s - windowSize +1
            index=0
            while slidingWindowCount>0:
                tmp=s[index:windowSize+index]
                st=set(tmp)
                if len(st) <=maxLetters:
                    if tmp not in d:
                        d[tmp]=1
                    else:
                        val=d[tmp]
                        val+=1
                        d[tmp]=val
                index+=1
                slidingWindowCount-=1
            windowSize-=1
        m=0
        if d:
            m=max(d.values())
        return m
