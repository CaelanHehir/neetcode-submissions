class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for string in strs:
            assigned = False
            for sublist in anagrams:
                for assigned_string in sublist:
                    if sorted(string) == sorted(assigned_string):
                        sublist.append(string)
                        assigned = True
                        break
                if assigned:
                    break
            if not assigned:
                anagrams.append([string])
        return anagrams

        