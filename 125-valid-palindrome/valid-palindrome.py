class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixedS = []
        sV = s.lower()
        for i in sV:
            if i == " ":
                continue
            if i.isalnum() == False:
                continue
            else:
                fixedS.append(i)
        
        left = 0
        right = len(fixedS) - 1
        while left < right:
            if(fixedS[left] != fixedS[right]):
                return False
            else:
                left+=1
                right-=1
        
        return True 
        