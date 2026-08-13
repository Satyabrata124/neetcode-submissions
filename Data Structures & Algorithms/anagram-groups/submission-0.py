class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol=defaultdict(list)
        for s in strs:
            tempstr=''.join(sorted(s))
            sol[tempstr].append(s)
        return list(sol.values())