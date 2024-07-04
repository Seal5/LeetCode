class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        for word in strs:
            sort = ''.join(sorted(word))
            if sort in final:
                final[sort].append(word)
            else:
                final[sort] = [word]
        
        return list(final.values())
                


