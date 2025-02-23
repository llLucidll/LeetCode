class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        halfway = length // 2
        i1, i2 = 0, 0
        prev, curr = 0, 0

        for _ in range(halfway + 1):
            prev = curr
            if i1 < len(nums1) and (i2 >= len(nums2) or nums1[i1] <= nums2[i2]):
                curr = nums1[i1]
                i1 += 1
            else:
                curr = nums2[i2]
                i2 += 1

        if length % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr
