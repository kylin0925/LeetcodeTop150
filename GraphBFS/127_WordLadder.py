class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordmap = {}
        wordlen = len(beginWord)
        for word in wordList:
            for i in range(wordlen):
                tmp = word[0:i] + "_" + word[i+1:]
                if wordmap.get(tmp) == None:
                    wordmap[tmp] = [word]
                else:
                    ll = wordmap[tmp]
                    ll.append(word)
        #print(wordmap)
        q = collections.deque()

        q.append((beginWord, 1))
        hash = {beginWord:1}

        while len(q) > 0:
            wd = q.popleft()
            for i in range(wordlen):
                tmp = wd[0][0:i] + "_" + wd[0][i + 1:]
                if tmp in wordmap:
                    wds = wordmap[tmp]
                    for twd in wds:
                        if twd in hash:
                            continue
                        if twd == endWord:
                            return wd[1]+1
                        q.append((twd,wd[1]+1))
                        hash[twd]=1

        return 0
        