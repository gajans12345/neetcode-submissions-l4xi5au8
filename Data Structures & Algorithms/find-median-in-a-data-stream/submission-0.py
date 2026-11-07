class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) + len(self.maxHeap) == 0:  # first num
            heapq.heappush(self.minHeap, num * -1)
        elif len(self.minHeap) + len(self.maxHeap) == 1:
            if num > self.minHeap[0] * -1:
                heapq.heappush(self.maxHeap, num)
            else:
                smallest = heapq.heappop(self.minHeap) * -1
                heapq.heappush(self.minHeap, num * -1)
                heapq.heappush(self.maxHeap, smallest)
        else:
            if len(self.minHeap) == len(self.maxHeap):
                if num > self.maxHeap[0]:
                    curr = heapq.heappop(self.maxHeap)
                    heapq.heappush(self.maxHeap, num)
                    heapq.heappush(self.minHeap, curr * -1)
                else:
                    heapq.heappush(self.minHeap, num * -1)
            else:
                if num < self.minHeap[0] * -1:
                    curr = heapq.heappop(self.minHeap) * -1
                    heapq.heappush(self.minHeap, num * -1)
                    heapq.heappush(self.maxHeap, curr)
                else:
                    heapq.heappush(self.maxHeap, num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] * -1 + self.maxHeap[0]) / 2
        else:
            return self.minHeap[0] * -1