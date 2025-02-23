class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Generate all possible substrings
        #Start from an index and find the longest substring at that index. Do this for all indices of the string
        substrings = []
        substr = ""
        for i in range(0, len(s)):
            if s[i] not in substr:
                substr += s[i]
            else:
                substrings.append(len(substr)) #append our max length
                #Decide where to start new substring from by eliminating duplicate character
                ind = substr.index(s[i])
                #Start the substring from the character following the duplicate
                substr = substr[ind+1:] + s[i]
        substrings.append(len(substr))

        if substrings != []:
            return max(substrings)
        else:
            return 0

                
