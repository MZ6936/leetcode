class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,num in enumerate(nums):
            if num == target:
                return i
                break
        for i,num in enumerate(nums):
            if(target < nums[i]):
                return i
            elif(i == len(nums)-1):
                return i+1
                break
            elif(nums[i] < target < nums[i+1]):
                return i+1
                break
        