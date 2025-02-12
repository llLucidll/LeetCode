class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in checked.keys():
                return checked[check], i
            else:
                checked[n] = i
        
