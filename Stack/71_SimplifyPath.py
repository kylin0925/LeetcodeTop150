class Solution:
    def simplifyPath(self, path: str) -> str:
        plist=path.split("/")
        stack = []
        for p in plist:
            
            if p == "" or p == ".":                
                continue
            if p =="..":
                if len(stack)>0:
                    stack.pop()
                continue
                            
            stack.append(p)
        #print(plist,stack)    
        return "/"+"/".join(stack)
