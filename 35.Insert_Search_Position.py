class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,num in enumerate(nums):
            if(target <= nums[i]):
                return i
                break
            elif(i == len(nums)-1 or nums[i] < target < nums[i+1]):
                return i+1
                break