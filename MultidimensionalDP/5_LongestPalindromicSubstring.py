class Solution(object):
    def find_odd_len(self,s,i):
        slen = len(s)
        st = i -1
        e = i + 1

        while st >=0 and  e < slen:
            #print st,e
            if s[st] == s[e]:                
                st -=1
                e+=1                
            else:
                break
        return s[st+1:e]
    def find_even_len(self,s,i):
        slen = len(s)
        st = i-1
        e = i
        
        while st >=0 and  e < slen:
           #print "even ",st,e
            if s[st] == s[e]:
                st-=1
                e+=1
            else:
                break
        #print s[st+1:e]
        return s[st+1:e]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        maxlen = -1
        ans = []
        if slen == 1:
            return s
        for i in range(1,slen):
            s1 = self.find_odd_len(s,i)
            s2 = self.find_even_len(s,i)
            if len(s1)>len(s2) and len(ans) < len(s1):
                ans = s1[:]
            elif len(s1)<len(s2) and len(ans) < len(s2):
                ans = s2[:]
        return ans