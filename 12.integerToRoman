class Solution:
    def intToRoman(self, num: int) -> str:
        stone = {
            1: "I", 
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        #Obvious cases:
        if num in stone.keys():
            return stone[num]
        
        string = str(num)
        length = len(string)
        factor = 10 ** (length - 1)
        roman = ""

        for digit in string:
            factor = 10 ** (length - 1)

            multiple = int(digit)

            if multiple * factor in stone.keys():
                roman += stone[multiple * factor]
            
            elif digit in "23":
                roman += multiple * stone[factor]
            elif digit in "678":
                multiple -= 5
                roman += stone[factor * 5] + multiple * stone[factor] 
            elif digit in "4":
                roman += stone[factor] + stone[factor * 5]
            elif digit in "9":
                roman += stone[factor] + stone[factor * 10]

            length -= 1

        return roman
