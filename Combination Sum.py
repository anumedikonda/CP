class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rst=[]
        self.dfs(candidates,target,[],rst)
        return rst
    def dfs(self,nums,target,path,rst):
        if target<0:
            return
        if target==0:
            rst.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:],target-nums[i],path+[nums[i]],rst)
