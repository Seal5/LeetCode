class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue

            temp = curMax*n
            curMax = max(curMax*n, n*curMin, n)
            curMin = min(temp, curMin*n, n)
            result = max(result, curMax)
        
        return result

