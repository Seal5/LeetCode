class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sVal = {}
        tVal = {}

        for i in range(len(s)):
            if s[i] not in sVal:
                sVal[s[i]] = 1
            else:
                sVal[s[i]] += 1
            if t[i] not in tVal:
                tVal[t[i]] = 1
            else:
                tVal[t[i]] += 1
        
        for i in s:
            if i not in tVal or sVal[i] != tVal[i]:
                return False
        return True
