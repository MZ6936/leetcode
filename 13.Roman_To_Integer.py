class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        prev = None
        roman = {"V": 5,
                "L": 50,
                "D": 500,
                "M": 1000}
        for ch in s[::-1]:
            if(ch=='I'):
                if(prev=="V" or prev=="X"):
                    value-=1
                else:
                    value+=1
            elif(ch=='X'):
                if(prev=="L" or prev=="C"):
                    value-=10
                else:
                    value+=10
            elif(ch=='C'):
                if(prev=="D" or prev=="M"):
                    value-=100
                else:
                    value+=100
            elif(ch in roman):
                value+=roman[ch]
            prev = ch
        return value
