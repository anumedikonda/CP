class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        total=0
        while left<=right:
            if left<right:
                total+=int(str(nums[left])+str(nums[right]))
            else:
                total+=nums[left]
            left+=1
            right-=1
        return total
