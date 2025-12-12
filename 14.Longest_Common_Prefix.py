class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 1000
        for i in range(len(strs)-1):
            for j in range(len(strs[i])):
                if(j == len(strs[i]) or j == len(strs[i+1]) or strs[i][j] != strs[i+1][j]):
                    index = min(index,j)
                    break
        if(index==0):
            return ""
        else:
            return strs[0][:index]