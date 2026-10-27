import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
   # negative so it acts like a max-heap
        counter = 0
        heap = []
        res = []
        for i in range(0,len(points)):
            x, y = points[i]
            dist = x * x + y * y 
            if counter == k:
                if heap[0][0] * -1 > dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, x, y))
            else:
                  # squared distance, no sqrt needed
                heapq.heappush(heap, (-dist, x, y))
                counter+=1
        while heap:
            next = heapq.heappop(heap)
            res.append([next[1],next[-1]])
        return res
        

        