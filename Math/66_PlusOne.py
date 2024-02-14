class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1
        c = 0
        tmp = digits[i] + 1
        c = tmp//10
        digits[i] = tmp % 10
        i-=1
        while i>=0:
            tmp = digits[i] + c
            print(tmp)
            c = tmp//10
            digits[i] = tmp % 10
            i-=1
        if c:
            digits.insert(0, c)
        return digits
