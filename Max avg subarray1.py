class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #s = sum(nums[:k])
        #ans = s

        #for i in range(k, len(nums)):
            #s += nums[i] - nums[i - k]
            #ans = max(ans, s)
            #return ans//
        if k==0:
            return 0
        windowSize=k
        slidingWindowCount = len(nums) - windowSize+1
        index=0
        s = sum(nums[0:windowSize])
        maxavg=float('-inf')
        while slidingWindowCount>0:
            if index>0:
                s=s-nums[index-1] + nums[index+windowSize-1]
            maxavg_tmp=s/k
            if maxavg_tmp>maxavg:
                maxavg=maxavg_tmp
            index+=1
            slidingWindowCount-=1
        return maxavg
