class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        number = 0
        for i,num in enumerate(digits):
            number += digits[-abs(i+1)] * (10**i)
        number += 1
        new = [int(digit) for digit in str(number)]
        return new