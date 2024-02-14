class RandomizedSet:

    def __init__(self):
        self.tbl = {}
        self.arr = []
    def insert(self, val: int) -> bool:
        if val not in self.tbl:
            self.tbl[val]=len(self.arr)
            self.arr.append(val)
            #print(self.tbl)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.tbl:
            return False
        else:
            idx = self.tbl[val]            
            self.tbl.pop(val)
            
            if idx == len(self.arr)-1:
                self.arr.pop()    
            else:
                last_val = self.arr[-1]
                self.arr[idx] = self.arr[-1]
                self.arr.pop()
                self.tbl[last_val]=idx
            #print(self.arr)
            return True

    def getRandom(self) -> int:
        #l = list(self.tbl.keys())
        return self.arr[random.randrange(0, len(self.arr))]
        
            
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()