class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = 0
        length = 0
        for i in reversed(s):
            if i == " " and flag == 0:
                continue
            elif i == " " and flag == 1:
                break
            else:
                flag = 1
                length += 1
            
        return length