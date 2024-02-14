from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        #self.data.sort()
        n = len(self.data)
        if  n & 1 > 0:
            return self.data[n//2]
        else:
            med = (self.data[n//2] + self.data[n//2 - 1])/2
            return med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()