class Solution:
    def romanToInt(self, s: str) -> int:
        now = 0
        ans = 0
        n = len(s)
        roman = {
                    "I":   1,
                    "V":   5,
                    "X":  10,
                    "L":  50,
                    "C":  100,
                    "D":  500,
                    "M":  1000}

        for i in range(n-1, -1, -1):
            r = roman[s[i]]
            if r < now:
                ans -=r
            else:
                ans +=r
            now = r
        return ans

        