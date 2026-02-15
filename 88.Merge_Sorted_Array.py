class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while(n>0):
                nums1.pop()
                n -= 1

        for i,num in enumerate(nums1):
            try:
                if num >= nums2[0]:
                    nums1.insert(i,nums2[0])
                    nums2.pop(0)
            except:
                continue
        nums1.extend(nums2)