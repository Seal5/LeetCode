class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        final = [1]*len(nums)

        lValue = 1
        for i in range(len(nums)):
            lValue *= nums[i]
            left[i] = lValue
        
        rValue = 1
        for i in range(len(nums)-1, -1, -1):
            rValue *= nums[i]
            right[i] = rValue
        
        for j in range(len(nums)):
            leftI = j-1 
            rightI = j+1
            if leftI == -1:
                lTotal = 1
            else:
                lTotal = left[leftI] 

            if rightI == len(nums):
                rTotal = 1
            else:
                rTotal = right[rightI]

            final[j] = lTotal * rTotal

        return final
            