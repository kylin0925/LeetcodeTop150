class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        #print(s,words)
        if s=="" or len(words) == 0:
            return []
        m1 = {}
        for w in words:
            if w not in m1:
                m1[w]=1
            else:
                m1[w]+=1
        #print(m1)
        wordnum = len(words)
        lenword = len(words[0])
        res = []
        for i in range(0,len(s) - lenword*wordnum+1):
            #substr = s[i:wordnum * lenword + i]
            cnt = 0
            map2 = {}
            for j in range(wordnum):
                w = s[i+j*lenword: i+j*lenword + lenword]
                #print(w)
                if w in m1:
                    if w not in map2:
                        map2[w] = 1
                        cnt+=1
                    else:
                        map2[w] +=1
                        if map2[w] > m1[w]:
                            break
                        else:
                            cnt+=1
                else:
                    break
            if cnt == wordnum:
                res.append(i)
        return res