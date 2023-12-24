# https://www.youtube.com/watch?v=3jdxYj3DD98&ab_channel=NeetCode

class Solution:
    def romanToInt(self, s: str) -> int:
        # read it character by character
        # if position of mapped value is less than next one
        # example (IV , I > V , I is 1, V is 5, value of next value - current)
        # but if value is VI then 5 is V < I , V + I = 6
        roman = {"I" : 1, "V" : 5, "X" : 10, 
        "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        result = 0
    
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result

