class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        maxSum=nums[0]
        minSum=nums[0]
        curMax=0
        curMin=0
        for i in nums:
            curMax=max(i,curMax+i)
            maxSum=max(maxSum,curMax)
            curMin=min(i,curMin+i)
            minSum=min(minSum,curMin)
            print(curMax,maxSum,curMin,minSum)
            total+=i
        return max(maxSum, total-minSum) if maxSum>0 else maxSum
