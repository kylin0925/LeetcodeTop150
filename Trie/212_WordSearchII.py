class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False
class Trie:
    def __init__(self):        
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        next = self.root 
        for c in word:            
            if c in next.child:                
                next = next.child[c]                
            else:                
                next.child[c] = TrieNode()                
                next = next.child[c]
        next.is_end=True           

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        visit = [[False for i in range(n)] for j in range(m)]

        ans = []
        char_list = []
        ans_dict = {}
        max_len = -1
        #print(m,n)
        def dfs(i,j,node):
            #print(i,j, char_list, visit[i][j]) 
            if len(ans) > len(words):
                return
            if len(char_list) > max_len:
                return                                                    
            if node.is_end:
                w = "".join(char_list)
                print("add",w)
                if w not in ans_dict:
                    ans.append(w)
                    ans_dict[w]=1
                    node.is_end=False

            c = board[i][j]
            if c in node.child and visit[i][j] == False:
                nd = node.child[c]
                char_list.append(c)
                visit[i][j] = True
                if i -1 >= 0 and visit[i-1][j] == False:
                    dfs(i-1,  j, nd)
                if i + 1 < m and visit[i+1][j] == False:
                    dfs(i+1,  j, nd)
                if j - 1 >=0 and visit[i][j-1] == False:
                    dfs(i  ,j-1, nd)
                if j + 1 < n and visit[i][j+1] == False: 
                    dfs(i  ,j+1, nd)
                
                if nd.is_end:
                    w = "".join(char_list)
                    #print("add",w)
                    if w not in ans_dict:
                        ans.append(w)
                        ans_dict[w]=1
                        nd.is_end=False
                char_list.pop()
                visit[i][j] = False

                

            
        trie = Trie()

        for w in words:
            trie.insert(w) 
            if len(w) > max_len:
                max_len = len(w)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.child:                                     
                    dfs(i,j,trie.root)
                    
        return ans

