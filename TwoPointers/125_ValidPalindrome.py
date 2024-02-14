class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        #print(s)
        while i<j:
            if s[i].isdigit() == False and s[i].isalpha() ==False:
                i+=1
            if s[j].isdigit() == False and s[j].isalpha() ==False:
                j-=1
            if (s[i].isdigit() or s[i].isalpha()) and (s[j].isdigit() or s[j].isalpha()):
                #print(s[i].isdigit(), s[i].isalpha())
                #print(s[j].isdigit(), s[j].isalpha())
                if s[i] != s[j]:
                    print(i, s[i],j ,s[j])
                    return False
                i+=1
                j-=1
            #print(i, j)
        return True
