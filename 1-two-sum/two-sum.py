class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}

        for i, value in enumerate(nums):
            comp=target - value
            
            if comp in hashmap:
                return [hashmap[comp],i]
            hashmap[value]=i