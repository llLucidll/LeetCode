class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Given an array of strings I need to find the largest common prefix substring

        #Generate a substring and then update as we go through each word.

        strs = sorted(strs)

        i = 0
        sub = ""

        while i < len(strs[0]) and i < len(strs[-1]):
            if strs[0][i] == strs[-1][i]:
                sub += strs[0][i]
            else:
                return sub

            i += 1
        return sub
