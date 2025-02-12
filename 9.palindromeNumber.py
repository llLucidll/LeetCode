class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringer = str(x)
        reverse = stringer[::-1]
        if reverse == stringer:
            return True
        else:
            return False
        
