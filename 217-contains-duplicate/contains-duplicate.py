class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        repeated = set()

        for i in nums:
            if i in repeated:
                return True 
            else: 
                repeated.add(i)
        return False
        