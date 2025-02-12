class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        #first split into words

        words = s.strip().split(" ")

        return len(words[-1])
    
        
        

        
