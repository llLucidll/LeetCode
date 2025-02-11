class Solution:
    def longestCommonPrefix(self, strs) -> str:
        #Given an array of strings I need to find the largest common prefix substring

        #Generate a substring and then update as we go through each word.

        longest = strs[0]

        for i in range(1, len(strs)):
            #if our longest prefix matches the prefix of current word
            if longest == strs[:len(longest)]:
                continue
            else:
                j = 0
                word = strs[i]
                while j < len(longest) and j < len(word):
                    if longest[j] == word[j]:
                        j+= 1
                    else:
                        break
                if j == 0:
                    return ""
                longest = longest[:j]
            
        
        return longest



            
        