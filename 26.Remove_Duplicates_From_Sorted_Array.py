from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list(sorted(set(nums)))
        nums[:] = unique
        return len(nums)
        