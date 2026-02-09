class Solution:
    def removeElement(self, nums: List[int], val: int):
        hashmap = []
        for i, num in enumerate(nums):
            if num == val:
                hashmap.append(i)
        length = len(hashmap)
        while length>0:
            nums.remove(val)
            length -= 1
        