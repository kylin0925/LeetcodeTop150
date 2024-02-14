class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))
        b = a[::-1]
        return a==b
