class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        '''
         set1 for row hash
            row_n 0_0 , 0_1, 1_0, ..... ,should not repeat.
         set2 for col hash
            as the same as row
         set3 for 33box
            boxId_n 9x9 -> there are 3, 3x3 boxes
            0_1,0_2....
        '''
        map1 = {}
        map2 = {}
        map3 = {}

        for y in range(0,9):
            for x in range(0, 9):
                #print(x,y)
                if board[y][x] == '.':
                    continue
                if (map1.get(str(y) + board[y][x]) == None and
                    map2.get(str(x) + board[y][x]) == None and
                    map3.get(str(x/3)+str(y/3) + board[y][x]) == None):
                    map1[str(y) + board[y][x]] = 1
                    map2[str(x) + board[y][x]] = 1
                    map3[str(x/3)+str(y/3) + board[y][x]] = 1
                else:
                    return False
        return True