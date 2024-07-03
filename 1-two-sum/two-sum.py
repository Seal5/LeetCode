class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in prev:
                return [prev[remainder], i]
            else:
                prev[n] = i 
