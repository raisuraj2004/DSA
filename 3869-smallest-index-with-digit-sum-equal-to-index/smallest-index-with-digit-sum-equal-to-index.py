class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            digit_sums = sum(map(int,str(nums[i])))
            if digit_sums == i:
                return i
            
        return -1


