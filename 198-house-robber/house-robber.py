class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        best=[0]*n
        best[0]=nums[0]
        
        for i in range(1,n):
            best[i]=max(best[i-1],best[i-2]+nums[i])
        return best[n-1]

