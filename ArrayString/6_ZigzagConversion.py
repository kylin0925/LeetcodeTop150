class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zig = ["" for i in range(numRows)]
        dir = 1
        idx = 0
        for i in range(len(s)):
            zig[idx] += s[i]
            if idx == 0:
                dir = 1
            elif idx >= numRows -1:
                dir = -1
            idx+=dir
            
        ret = "" .join(zig)
        return ret
