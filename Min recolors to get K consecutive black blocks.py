class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    if k==0:
        return 0
    if k==1:
        if "B" in blocks:
            return 0
        else:
            return 1
    windowSize=k
    slidingWindowCount = len(blocks) - windowSize+1
    index=0
    minimum = sys.maxsize
    while slidingWindowCount > 0:
        tmp = blocks[index:windowSize+index]
        minimum_tmp=0
        for i in tmp:
            if i=="W":
                minimum_tmp+=1
        if minimum_tmp < minimum:
            minimum=minimum_tmp
        index+=1
        slidingWindowCount-=1
    return minimum
